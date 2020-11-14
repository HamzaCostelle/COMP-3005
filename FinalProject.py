#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:20:30 2020

@author: hamzacostelle
"""
import pandas as pd
import datetime as dt
import requests
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt, mpld3
import numpy as np
import seaborn as sns
from mpld3 import plugins

url = 'https://www.weather.gov/bou/seasonalsnowfall'

response = requests.get (url)

soup = BeautifulSoup (response.text, "html.parser")

data = []

#Code isolates the required data 
allrows = soup.find_all("tr")
for row in allrows: 
    row_list = row.find_all("td")
    dataRow = []
    for cell in row_list: 
        dataRow.append(cell.text)
    data.append(dataRow)
data = data [6:50]   
    
df = pd.DataFrame(data)

#Code replaces column headers with the ones I want
colHeaders = df.iloc [0]
df = df [1:]
df.columns = colHeaders

#Code removes all unwanted values from the rows and removes all unwanted columns as well
df2 = df.dropna(axis = 0, how = 'any')
df2 = df.drop(['Departure', 'Total'], axis = 1)
df3 = df2.drop(df2.index [[0,1]])
df4 = df3.replace(['\n0.0\n','T'], 0.0, regex=True)


#Code converts columns to float
df4 = df4.rename(columns={'Snow':'Year'})
df4['Year']= df4[ 'Year'].str.split('-').str.get(-1)
df4.set_index('Year', inplace=True)
cols = df4.select_dtypes(exclude=['float']).columns
df4[cols] = df4[cols].apply(pd.to_numeric, downcast='float', errors='coerce')

#Code creates the desired charts

fig1 = sns.boxplot(data=df4)
plt.legend (loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Months', fontsize=12)
plt.ylabel ("Monthly Snowfall (Inches)", fontsize=12)
mpld3.show()

plt.style.use('seaborn')

fig2 = df4.plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.legend (loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Year', fontsize=20)
plt.ylabel ("Monthly Snowfall (Inches)", fontsize=20)
mpld3.show()

fig3 = df4.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.legend (loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Year', fontsize=20)
plt.ylabel ("Monthly Snowfall (Inches)", fontsize=20)
mpld3.show()

fig4 = df4.plot(kind = 'bar',stacked = True, figsize=(20,10), linewidth=5, fontsize=20)
plt.legend (loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Year', fontsize=20)
plt.ylabel ("Monthly Snowfall (Inches)", fontsize=20)
mpld3.show()





