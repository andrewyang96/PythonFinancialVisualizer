import sys
from visualizer import *

if __name__ == "__main__":
    ticker = sys.argv[1]
    try:
        start = sys.argv[2]
        end = sys.argv[3]
        visualize([ticker], start, end)
    except IndexError:
        from datetime import datetime as dt
        visualize(ticker, "1900-01-01", "{:%Y-%m-%d}".format(dt.today()))
    
