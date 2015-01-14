from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ystockquote as ysq

def setup(start, end, tickers):
    plt.close("all")
    plt.title("Stock Prices for {0} From {1} to {2}".format([ticker.upper() for ticker in tickers], start, end))
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=30)

# returns tuple
def get_daily_closes(ticker, start, end):
    data = ysq.get_historical_prices(ticker, start, end)
    dates = []
    adj_closes = []

    # extract Adj Close from each date in [start,end]
    keys = data.keys()
    keys.sort()
    for key in keys:
        dates.append(key)
        adj_closes.append(data[key]["Adj Close"])

    # convert all dates from str to datetime
    dates[:] = [str2datetime(date) for date in dates]
    
    return (dates, adj_closes)

# returns datetime
def str2datetime(s):
    split = s.split("-")
    split[:] = [int(e) for e in split]
    return dt(*split)

def visualize(tickers, start, end):
    setup(start, end, tickers)
    for ticker in tickers:
        c = get_daily_closes(ticker, start, end)
        plt.plot(*c, label=ticker.upper())
    plt.legend()
    plt.show()

if __name__ == "__main__":
    visualize(['spy', 'vfinx'], "2014-01-01", "2015-01-01")
