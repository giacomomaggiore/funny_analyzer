import pandas as pd
import json

# Specify the path to your CSV file
csv_file = "/Users/giacomomaggiore/Desktop/flat-ui__data-Sun Dec 15 2024.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)
list_tickers = df["Symbol"].tolist()
# Print the DataFrame
print(list_tickers)

# Specify the path to your JavaScript file
js_file = "ticker_list.js"

# Convert the list to a JSON string
json_data = json.dumps(list_tickers)

# Write the JSON string to the JavaScript file
with open(js_file, "w") as file:
    file.write(f"const list_tickers = {json_data};")
    
list_tickers = ["A", "AAPL", "ABBV", "ABNB", "ABT", "ACGL", "ACN", "ADBE", "ADI", "ADM", "ADP", "ADSK", "AEE", "AEP", "AES", "AFL", "AIG", "AIZ", "AJG", "AKAM", "ALB", "ALGN", "ALL", "ALLE", "AMAT", "AMCR", "AMD", "AME", "AMGN", "AMP", "AMT", "AMTM", "AMZN", "ANET", "ANSS", "AON", "AOS", "APA", "APD", "APH", "APTV", "ARE", "ATO", "AVB", "AVGO", "AVY", "AWK", "AXON", "AXP", "AZO", "BA", "BAC", "BALL", "BAX", "BBY", "BDX", "BEN", "BF.B", "BG", "BIIB", "BK", "BKNG", "BKR", "BLDR", "BLK", "BMY", "BR", "BRK.B", "BRO", "BSX", "BWA", "BX", "BXP", "C", "CAG", "CAH", "CARR", "CAT", "CB", "CBOE", "CBRE", "CCI", "CCL", "CDNS", "CDW", "CE", "CEG", "CF", "CFG", "CHD", "CHRW", "CHTR", "CI", "CINF", "CL", "CLX", "CMCSA", "CME", "CMG", "CMI", "CMS", "CNC", "CNP", "COF", "COO", "COP", "COR", "COST", "CPAY", "CPB", "CPRT", "CPT", "CRL", "CRM", "CRWD", "CSCO", "CSGP", "CSX", "CTAS", "CTLT", "CTRA", "CTSH", "CTVA", "CVS", "CVX", "CZR", "D", "DAL", "DAY", "DD", "DE", "DECK", "DELL", "DFS", "DG", "DGX", "DHI", "DHR", "DIS", "DLR", "DLTR", "DOC", "DOV", "DOW", "DPZ", "DRI", "DTE", "DUK", "DVA", "DVN", "DXCM", "EA", "EBAY", "ECL", "ED", "EFX", "EG", "EIX", "EL", "ELV", "EMN", "EMR", "ENPH", "EOG", "EPAM", "EQIX", "EQR", "EQT", "ERIE", "ES", "ESS", "ETN", "ETR", "EVRG", "EW", "EXC", "EXPD", "EXPE", "EXR", "F", "FANG", "FAST", "FCX", "FDS", "FDX", "FE", "FFIV", "FI", "FICO", "FIS", "FITB", "FMC", "FOX", "FOXA", "FRT", "FSLR", "FTNT", "FTV", "GD", "GDDY", "GE", "GEHC", "GEN", "GEV", "GILD", "GIS", "GL", "GLW", "GM", "GNRC", "GOOG", "GOOGL", "GPC", "GPN", "GRMN", "GS", "GWW", "HAL", "HAS", "HBAN", "HCA", "HD", "HES", "HIG", "HII", "HLT", "HOLX", "HON", "HPE", "HPQ", "HRL", "HSIC", "HST", "HSY", "HUBB", "HUM", "HWM", "IBM", "ICE", "IDXX", "IEX", "IFF", "INCY", "INTC", "INTU", "INVH", "IP", "IPG", "IQV", "IR", "IRM", "ISRG", "IT", "ITW", "IVZ", "J", "JBHT", "JBL", "JCI", "JKHY", "JNJ", "JNPR", "JPM", "K", "KDP", "KEY", "KEYS", "KHC", "KIM", "KKR", "KLAC", "KMB", "KMI", "KMX", "KO", "KR", "KVUE", "L", "LDOS", "LEN", "LH", "LHX", "LIN", "LKQ", "LLY", "LMT", "LNT", "LOW", "LRCX", "LULU", "LUV", "LVS", "LW", "LYB", "LYV", "MA", "MAA", "MAR", "MAS", "MCD", "MCHP", "MCK", "MCO", "MDLZ", "MDT", "MET", "META", "MGM", "MHK", "MKC", "MKTX", "MLM", "MMC", "MMM", "MNST", "MO", "MOH", "MOS", "MPC", "MPWR", "MRK", "MRNA", "MS", "MSCI", "MSFT", "MSI", "MTB", "MTCH", "MTD", "MU", "NCLH", "NDAQ", "NDSN", "NEE", "NEM", "NFLX", "NI", "NKE", "NOC", "NOW", "NRG", "NSC", "NTAP", "NTRS", "NUE", "NVDA", "NVR", "NWS", "NWSA", "NXPI", "O", "ODFL", "OKE", "OMC", "ON", "ORCL", "ORLY", "OTIS", "OXY", "PANW", "PARA", "PAYC", "PAYX", "PCAR", "PCG", "PEG", "PEP", "PFE", "PFG", "PG", "PGR", "PH", "PHM", "PKG", "PLD", "PLTR", "PM", "PNC", "PNR", "PNW", "PODD", "POOL", "PPG", "PPL", "PRU", "PSA", "PSX", "PTC", "PWR", "PYPL", "QCOM", "QRVO", "RCL", "REG", "REGN", "RF", "RJF", "RL", "RMD", "ROK", "ROL", "ROP", "ROST", "RSG", "RTX", "RVTY", "SBAC", "SBUX", "SCHW", "SHW", "SJM", "SLB", "SMCI", "SNA", "SNPS", "SO", "SOLV", "SPG", "SPGI", "SRE", "STE", "STLD", "STT", "STX", "STZ", "SW", "SWK", "SWKS", "SYF", "SYK", "SYY", "T", "TAP", "TDG", "TDY", "TECH", "TEL", "TER", "TFC", "TFX", "TGT", "TJX", "TMO", "TMUS", "TPL", "TPR", "TRGP", "TRMB", "TROW", "TRV", "TSCO", "TSLA", "TSN", "TT", "TTWO", "TXN", "TXT", "TYL", "UAL", "UBER", "UDR", "UHS", "ULTA", "UNH", "UNP", "UPS", "URI", "USB", "V", "VICI", "VLO", "VLTO", "VMC", "VRSK", "VRSN", "VRTX", "VST", "VTR", "VTRS", "VZ", "WAB", "WAT", "WBA", "WBD", "WDC", "WEC", "WELL", "WFC", "WM", "WMB", "WMT", "WRB", "WST", "WTW", "WY", "WYNN", "XEL", "XOM", "XYL", "YUM", "ZBH", "ZBRA", "ZTS"]
etf=[["iShares Core S&P 500","CSSPX",0.07,False],["iShares Core MSCI World","SWDA",0.20,True],["iShares Core MSCI Emerging Markets IMI","EIMI",0.18,True],
     ["iShares Nasdaq 100","CSNDX",0.33,False],["iShares MSCI ACWI","IUSQ",0.20,True],["Vanguard FTSE All-World","VWCE",0.22,True],
     ["iShares Core DAX","EXS1",0.16,False],["Lyxor Core STOXX Europe 600 (DR)","MEUD",0.07,True],["iShares Core MSCI Europe","SMEA",0.12,True],
     ["Xtrackers MSCI USA","XD9U",0.07,False],["Xtrackers MSCI Emerging Markets","XMME",0.18,True],["iShares Core EURO STOXX 50","CSSX5E",0.10,True],
     ["iShares Edge MSCI World Value Factor","IWVL",0.30,True],["iShares Core MSCI Japan IMI","SJPA",0.15,False],["iShares Core MSCI EMU","CSEMU",0.12,True],
     ["iShares Edge MSCI World Minimum Volatility","MVOL",0.30,True],["iShares Edge MSCI Europe Value Factor","IEVL",0.25,True],
     ["iShares Core MSCI Pacific ex Japan","CSPXJ",0.20,True],["Xtrackers S&P 500 Equal Weight","XDEW",0.20,False],["iShares MSCI World Small Cap","IUSN",0.35,True],
     ["iShares Edge MSCI World Quality Factor","IWQU",0.30,True],["iShares MSCI EM Asia","CSEMAS",0.20,True],["UBS ETF (LU) MSCI UK","UKGBPB",0.20,False],
     ["SPDR S&P 400 US Mid Cap","SPY4",0.30,False],["iShares Edge S&P 500 Minimum Volatility","MVUS",0.20,False],
     ["UBS ETF (LU) MSCI Switzerland 20/35","SW2CHB",0.20,False],["SPDR Russell 2000 US Small Cap","R2US",0.30,False],["iShares MSCI Canada","CSCA",0.48,False],
     ["Xtrackers MSCI China","XCS6",0.65,False],["Amundi CAC 40","C40",0.25,False],["Xtrackers MSCI Europe Small Cap","XXSC",0.30,True],
     ["Vanguard FTSE North America","VNRA",0.10,True],["Amundi ETF MSCI Europe Value Factor","VCEU",0.23,True],["Amundi MSCI Europe Quality Factor","QCEU",0.23,True],
     ["iShares MSCI Australia","SAUS",0.50,False],["Amundi ETF MSCI World ex EMU","CM9",0.35,True],
     ["Franklin FTSE Korea","FLXK",0.09,False],["WisdomTree US Quality Dividend Growth","DGRA",0.33,False],["Lyxor MSCI Brazil","BRA",0.65,False],
     ["Lyxor MSCI Emerging Markets Ex China","EMXC",0.15,True],["Vanguard FTSE Emerging Markets","VFEA",0.22,True],["iShares Edge MSCI World Size Factor","IWSZ",0.30,False],
     ["Amundi Japan Topix","XAMY",0.20,False],["Vanguard FTSE Developed Europe ex UK","VERE",0.10,False],["Fidelity US Quality Income","FUSA",0.25,False],
     ["Franklin FTSE China","FLXC",0.19,False],["iShares MSCI UK Small Cap","SXRD",0.58,False],["Franklin FTSE India","FLXI",0.19,False],
     ["iShares Nikkei 225","CSNKY",0.48,False],["Amundi MSCI Nordic","CN1",0.25,False],["iShares Edge MSCI Europe Multifactor","IFSE",0.45,True],
     ["Amundi MSCI Europe Minimum Volatility Factor","MIVO",0.23,True],["iShares MSCI EMU Large Cap","EMUL",0.49,True],["Xtrackers MSCI North America High Dividend Yield","XDND",0.39,False],
     ["Amundi ETF MSCI Switzerland","18MN",0.25,False],["iShares MSCI EMU Mid Cap","IS3H",0.49,True],["iShares MSCI Korea","CSKR",0.65,False],
     ["SPDR MSCI Europe Small Cap","SMCX",0.30,True],["Xtrackers MSCI Mexico","XMEX",0.65,False],["Lyxor MSCI Eastern Europe ex Russia","EST",0.50,False],
     ["iShares Edge MSCI USA Size Factor","QDVC",0.20,False],["SPDR MSCI USA Value Weighted","ZPRU",0.20,False],["Xtrackers MSCI Taiwan","XMTW",0.65,False]]

with open("select.txt", "w") as file:
    for ticker in etf:
        file.write("<option value=" + ticker[1]+".MI" + ">"+ ticker[0]+"</option>" + "\n")

