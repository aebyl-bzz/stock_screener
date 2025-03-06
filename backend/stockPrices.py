from yahoo_fin import stock_info
import datetime as dt

tickers = stock_info.tickers_sp500()
# tickers basically id

start = dt.datetime.now() - dt.timedelta(days=180)
end = dt.datetime.now()
