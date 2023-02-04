#!/usr/bin/python

import os.path
from yahoo_fin import stock_info as si
import datetime
import pytz

#path to stock prices
save_path ='/home/holden/.config/polybar/scripts/stocks'

NYCtz = pytz.timezone('America/New_York')
open_time = datetime.time(9,30,0)
close_time = datetime.time(16,0,0)

def time_in_range(start,end, current):
    return start <= current <= end

tickers = ['SPY', 'AAPL', 'AMZN', 'TSLA']


now = datetime.datetime.now(NYCtz).time()

market_open = time_in_range(open_time, close_time, now)

try:
    stock_string = ""
    for ticker in tickers:
        current_price = round(si.get_live_price(ticker),2)
        prev_data = si.get_data(ticker, start_date='01/01/2023')
        if market_open:
            prev_close = prev_data.iloc[len(prev_data)-1]['close']
        else:
            prev_close = prev_data.iloc[len(prev_data)-2]['close']
        
        per_change = round(((current_price-prev_close)/(prev_close))*100,2)
        stock_string += ticker + ":$" + str(current_price) + " (" + str(per_change) + "%) "

      
    path = os.path.join(save_path,"current_stocks.txt")         
    f = open(path, "w")
    f.write(stock_string)
    f.close()
    
      
      
except Exception as e:
    print(e)
    print ('Something went wrong!')

