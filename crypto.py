#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:02:12 2020

@author: hamzacostelle
"""


#Import the requests library
import requests
#Import the datetime library
from datetime import datetime

TICKER_API_URL = 'https://api.cryptowat.ch/markets/bitfinex/'

headers = ['Closetime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'CloseVolume']

def get_crypto_data(crypto): # make the api call to the crypto watch API for the passed in crypto

    resp = requests.get(f'{TICKER_API_URL}{crypto}/ohlc')
    doc = resp.json()
    return doc['result']['604800'] #Back to 2013

data = get_crypto_data('btcusd')

#Can get the date like this:
#print(datetime.fromtimestamp(data[-1][0]))

#Close price over time
# closePrices = [] #y variable

# for l in data: 
#     closePrices.append(l[4])
   
times = [] #x variable

for l in data: 
    times.append (l[0])
    
import matplotlib.pyplot as plt

# plt.plot (times, closePrices)
# plt.xlabel ('Timestamp')
# plt.ylabel ('Closing Price (USD)')
# plt. show ()

#Chart with low , high, open and close

closePrices = []
openPrices = []
lowPrices = []
highPrices = []
times = []

for l in data: 
    times.append(datetime.fromtimestamp(l[0]))
    openPrices.append(l[1])
    highPrices.append(l[2])
    lowPrices.append(l[3])
    closePrices.append(l[4])
    
close = plt.plot(times, closePrices, 'b-', label = 'Close Prices')
open = plt.plot(times, openPrices, 'g-', label = 'Open Prices')
low = plt.plot(times, lowPrices, 'y-', label = 'Low Prices')
high =plt.plot(times, highPrices, 'r-', label = 'High Prices')
plt.xlabel ('Date')
plt.ylabel ('Closing Price (USD)')
plt.title ('Bitoin Prices in USD Over Time')
plt.legend ()
plt. show ()



