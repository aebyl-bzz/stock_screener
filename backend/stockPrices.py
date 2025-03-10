import yfinance as yf
from yahoo_fin import stock_info as si
import datetime as dt
import pandas as pd
import pandas_datareader as pdreader

tickers = si.tickers_sp500()
# tickers basically id
print(tickers)


start = dt.datetime.now() - dt.timedelta(days=180)
end = dt.datetime.now()

#GSPC ticker for sp500
sp500_df = yf.download('^GSPC', start=start, end=end)
sp500_df['Pct Change'] = sp500_df['Adj Close'].pct_change()


#retun of timeframe
sp500_return = (sp500_df['PCT Change'] + 1).cumprod()[-1]

return_list = []
final_dataframe = pd.DataFrame(columns=['Ticker', 'Latest_Price', 'Score', 'PE_Ratio', 'PEG_Ratio', 'SMA_100', 'SMA_150', 'SMA_200', '26_Week_Low', '26_Week_High'])
#Pe = Price to earnings ratio, PEG = price earnings growth ratio, SMA = Moving average

for ticker in tickers:
    df = pdreader.DataReader(ticker, 'yahoo', start, end)
    df.to_csv(f'stock_data/{ticker}.csv')

    df['Pct Change'] = df['Adj Close'].pct_change()
    stock_return = (df['Pct Change'] + 1).cumprod()[-1]

    returns_compared = round((stock_return / sp500_return), 2)
    return_list.append(returns_compared)

