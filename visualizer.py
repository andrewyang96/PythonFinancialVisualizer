from datetime import datetime as dt
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
import ystockquote as ysq


def plot(ticker, x,y):
    pyplot.close("all")
    fig, ax = pyplot.subplots(1)
    ax.plot(x,y)

    fig.autofmt_xdate()

    ax.fmt_xdata = mdates.DateFormatter("%Y-%m-%d")
    pyplot.title("Stock Prices for {0} From {1:%Y-%m-%d} to {2:%Y-%m-%d}".format(ticker.upper(), min(x), max(x)))
    pyplot.show()

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

def visualize(ticker, start, end):
    c = get_daily_closes(ticker, start, end)
    plot(ticker, *c)

if __name__ == "__main__":
    visualize("aapl", "2013-01-01", "2015-01-01")
