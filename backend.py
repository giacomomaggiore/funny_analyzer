from fastapi import FastAPI, Path, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
import datetime as dt
import json
import yfinance as yf
import pandas as pd
import yfinance as yf
import datetime as dt
import random
import math
import numpy as np
from fastapi import FastAPI, Path, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
templates = Jinja2Templates(directory="templates")
import matplotlib.pyplot as plt
import google.generativeai as genai

import PIL.Image
import os
import base64

#--------------------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

#--------------------------------------------------------------
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
#--------------------------------------------------------------

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

start_date = "2020-01-01"
end_date = "2022-01-01"
benchmark = "IWDA.AS"

@app.get('/')
async def home(request: Request):
    context = {}
    return templates.TemplateResponse(name="home.html", request=request, context=context)


@app.get('/test')
async def test():
    return "ciao"


default_asset = ""

@app.get('/analyze/')
async def analyze(asset_1: str=default_asset, asset_2: str = default_asset, 
                  asset_3: str = default_asset, asset_4: str = default_asset,
                  percentage_1: int = 0, percentage_2: int = 0,
                  percentage_3: int = 0, percentage_4: int = 0,):
    portfolio_dict = {
        "asset_1": [asset_1, percentage_1],
        "asset_2" : [asset_2, percentage_2],
        "asset_3" : [asset_3, percentage_3],
        "asset_4" :[asset_4, percentage_4],
    }
    
    [x, y] = create_portfolio(portfolio_dict)
    funny_analysis = gemini_analysis(portfolio_dict, "graph.png")
    return (funny_analysis)
    
      


prova = {
    "asset_1":["IWDA.AS", 50],
    "asset_2": ["AAPL", 50],
}

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
    
    df_data = yf.download(asset_list, start=start_date, end=end_date)["Adj Close"]
    df_data.fillna(method='ffill', inplace=True)
    df_data.fillna(method='bfill', inplace=True)
    df_data_benchmark = yf.download(benchmark, start=start_date, end=end_date)["Adj Close"]
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
    
    
    portfolio_start_value = df_portfolio.iloc[0, 0]
    portfolio_end_value = df_portfolio.iloc[-1, 0]
    portfolio_length = len(df_portfolio)

    cagr_portfolio = (portfolio_end_value / portfolio_start_value) ** (1 / portfolio_length) - 1
    
    benchmark_start_value = df_portfolio.iloc[0, 1]
    benchmark_end_value = df_portfolio.iloc[-1, 1]
    benchmark_length = len(df_portfolio)
    
    cagr_benchmark = (benchmark_end_value / benchmark_start_value) ** (1 / benchmark_length) - 1
    
    plt.plot(df_portfolio)
    plt.legend(["Portfolio", "Benchmark (iShares MSCI World)"])
    plt.title("Portfolio vs Benchmark")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.figtext(0.28, 0.7, f"Portfolio CAGR: {math.floor(cagr_portfolio*10000)} \n Benchmark CAGR: {math.floor(cagr_benchmark*10000)}", 
                ha="center", fontsize=8, bbox={"facecolor":"gray", "alpha":0.5, "pad":5})
    plt.savefig('graph.png')
    
    
    return cagr_portfolio, cagr_benchmark


def gemini_analysis(portfolio_dict, photo_1_path):
    photo_1_path = photo_1_path  # Replace with the actual path to your first image

    photo_1 = PIL.Image.open(photo_1_path)

    #Choose a Gemini model.

    prompt = f"""This is my investment portfolio. 
    The blue line represents the value of my portfolio over time,
    while the orange line represents the value of the benchmark (iShares MSCI World).
    This is the allocation of my portfolio:
    Asset: {portfolio_dict['asset_1'][1]} :{portfolio_dict['asset_1'][0]}%
    Asset: {portfolio_dict['asset_2'][1]} :{portfolio_dict['asset_2'][0]}%
    Analyze it in a funny way please!
    you can do one of the following:
    - make comparison wih famous movies
    - make comparison with food
    - make comparison with animals
    - make comparison with famous people
    - make comparison with famous places
    Keep it short and make fun of the investor (less than 10000 characters)."""
    

    response = model.generate_content([prompt, photo_1])
    return response.text

