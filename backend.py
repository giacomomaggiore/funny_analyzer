from fastapi import FastAPI, Path, Request

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
import datetime as dt
import yfinance as yf
import pandas as pd
import yfinance as yf
import datetime as dt
import math
import numpy as np
from fastapi import FastAPI, Path, Request

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
templates = Jinja2Templates(directory="templates")
import matplotlib.pyplot as plt
import google.generativeai as genai

import os


#--------------------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
api_key = "AIzaSyACo6M0CZ5lgz-sBiWpqBEBMA_Y4sRti5Y"

#--------------------------------------------------------------
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
#--------------------------------------------------------------

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

start_date = "2020-01-01"
end_date = "2022-01-01"
benchmark = "IWDA.AS"
risk_free = 0.044

@app.get('/')
async def home(request: Request):
    context = {}
    return templates.TemplateResponse(name="home.html", request=request, context=context)


@app.get('/test')
async def test():
    return "ciao mamo"


default_asset = ""

@app.get("/analyze")
@app.get('/analyze/')
async def analyze(asset_1: str=default_asset, asset_2: str = default_asset, 
                  asset_3: str = default_asset, asset_4: str = default_asset,
                  percentage_1: int = 0, percentage_2: int = 0,
                  percentage_3: int = 0, percentage_4: int = 0, 
                  asset_5: str = default_asset,percentage_5: int = 0,
                  portfolio_value: str = default_asset,
                  salary: str = default_asset,
                  age: str = default_asset,
                  country: str = default_asset,
                  job: str = default_asset):
    portfolio_dict = {
        "asset_1": [asset_1, percentage_1],
        "asset_2" : [asset_2, percentage_2],
        "asset_3" : [asset_3, percentage_3],
        "asset_4" :[asset_4, percentage_4],
        "asset_5" : [asset_5, percentage_5]
    }
    
    personal_info__dict = {
        "Portfolio value": portfolio_value,
        "Salary": salary,
        "Age": age,
        "Country": country,
        "Job": job,
    }
    for key, value in personal_info__dict.items():
        if value == default_asset:
            personal_info__dict.pop(key)

    
    
    results = create_portfolio(portfolio_dict)
    funny_analysis = gemini_analysis(portfolio_dict, results, personal_info__dict)
    return (funny_analysis)
    
      


prova = {
    "asset_1":["IWDA.AS", 50],
    "asset_2": ["AAPL", 50],
}
def volatility(df):
  return df.pct_change(fill_method=None).std() * np.sqrt(252)
def cagr(df):
  return ((df.iloc[-1] / df.iloc[0]) ** (1 / (len(df) / 252)) - 1)*100
def sharpe_ratio(df, risk_free):
  average_return = float(df.pct_change(fill_method=None).mean()) * 252

  sigma = volatility(df)
  print(average_return)
  sharpe_ratio = (average_return - risk_free * 0.01) / sigma

  sharpe_ratio = '%.3f'%(sharpe_ratio)
  sharpe_ratio = float(sharpe_ratio)

  return sharpe_ratio

def create_portfolio(portfolio_dict):
    print("creato!")
    print(portfolio_dict)
    
    asset_list = []
    amount_splits = []
    total_amount = 1000000
    for key, value in portfolio_dict.items():
        if value[0] != "none" and value[1] != 0:
            
            asset_list.append(value[0])
            
            amount_splits.append(value[1] * total_amount / 100)
    
    print(asset_list)
    print(amount_splits)
    df_data = yf.download(asset_list, start=start_date, end=end_date)
    print(df_data)
    df_data = df_data["Close"]
    #return df_data.iloc[0, 0]
    df_data.fillna(method='ffill', inplace=True)
    df_data.fillna(method='bfill', inplace=True)
    df_data_benchmark = yf.download(benchmark, start=start_date, end=end_date)["Close"]
    n_shares_benchmark = math.floor(total_amount / df_data_benchmark.iloc[0])
    n_shares_per_asset = np.zeros(len(asset_list))
    print("eccomi")
    
    for i in range(len(asset_list)):
        print(i)
        print(df_data.iloc[0, i])
        n_shares_per_asset[i] = math.floor(amount_splits[i] / df_data.iloc[0, i])
    
    for j in range(len(asset_list)):
        df_data.iloc[:, j] = df_data.iloc[:, j] * n_shares_per_asset[j]
    
    df_data["portfolio_value"] = df_data.sum(axis=1)
    cash_portfolio = total_amount - df_data["portfolio_value"].iloc[0]
    df_data["portfolio_value"] = df_data["portfolio_value"] + cash_portfolio
    df_portfolio = pd.DataFrame( index = df_data.index)
    df_portfolio["Portfolio"] = df_data["portfolio_value"] 
    df_portfolio["Benchmark"] = df_data_benchmark * n_shares_benchmark
    df_portfolio.fillna(method='ffill', inplace=True)
    df_portfolio.fillna(method='bfill', inplace=True)
    cash_benchmark = total_amount - df_portfolio["Benchmark"].iloc[0]
    df_portfolio["Benchmark"] = df_portfolio["Benchmark"] + cash_benchmark
    
    
    

    #calculate performance metrics
    
    cagr_benchmark = cagr(df_portfolio["Benchmark"])
    cagr_portfolio = cagr(df_portfolio["Portfolio"])
    sharpe_ratio_portfolio = sharpe_ratio(df_portfolio["Portfolio"], risk_free)
    sharpe_ratio_benchmark = sharpe_ratio(df_portfolio["Benchmark"], risk_free)
    
    results = {
        "cagr_portfolio": cagr_portfolio,
        "cagr_benchmark": cagr_benchmark,
        "sharpe_ratio_portfolio": sharpe_ratio_portfolio,
        "sharpe_ratio_benchmark": sharpe_ratio_benchmark
    }
    
    return results
    
    """
    plt.plot(df_portfolio)
    plt.legend(["Portfolio", "Benchmark (iShares MSCI World)"])
    plt.title("Portfolio vs Benchmark")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.figtext(0.28, 0.7, f"Portfolio CAGR: {math.floor(cagr_portfolio*10000)} \n Benchmark CAGR: {math.floor(cagr_benchmark*10000)}", 
                ha="center", fontsize=8, bbox={"facecolor":"gray", "alpha":0.5, "pad":5})
    plt.savefig('graph.png')
    """
    
    


def gemini_analysis(portfolio_dict, results, personal_info_dict):


    #Choose a Gemini model.

    prompt = f"""
    
    This is the allocation of my portfolio:
    Asset: {portfolio_dict['asset_1'][1]} :{portfolio_dict['asset_1'][0]}%
    Asset: {portfolio_dict['asset_2'][1]} :{portfolio_dict['asset_2'][0]}%
    
    and this was the performance of my portfolio compared to the benchmark:
    CAGR: {results['cagr_portfolio']}
    Sharpe Ratio: {results['sharpe_ratio_portfolio']}
    CAGR Benchmark: {results['cagr_benchmark']}
    Sharpe Ratio Benchmark: {results['sharpe_ratio_benchmark']}
    
    These are my personal information:
    {personal_info_dict}
    
    Analyze it in a funny way please!
    you can:
    - make comparison wih famous movies
    - make fun of the investor
    - make comparison with food
    - make comparison with animals
    - make comparison with famous people
    - make comparison with famous places
    ."""
    

    response = model.generate_content([prompt],
        generation_config = genai.GenerationConfig(
        max_output_tokens=100,
        temperature=2,
    ) )
    return response.text

