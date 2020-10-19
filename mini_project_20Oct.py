# -*- coding: utf-8 -*-
"""Mini Project 20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TbO4plEzxqwl2cm0mMAXwGa05MmZHltd
"""

import pandas as pd
import datetime
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

df = pd.read_excel('/content/drive/My Drive/python/NSE 1jan-18oct correct date.xlsx')

nifty = df

df.head()

df['Date'] = pd.to_datetime(df['Date'] , format='%Y-%m-%d')

df['Date'] = pd.to_datetime(df['Date'] , format='%d-%m-%Y')

df.info()

Date = df['Date']

df['Percentage Change'] = ((-df['Open'] + df['Close'])/100).astype(float)
df['Percentage Change']
df['Marker'] = np.nan

for i in range(len(nifty['Marker'])):
  if nifty['Percentage Change'][i] > 0:
    nifty['Marker'][i] ='Up'
  elif nifty['Percentage Change'][i] < 0:
    nifty['Marker'][i] = 'Down'
  elif nifty['Percentage Change'][i] == 0:
    nifty['Marker'][i] = 'Flat'

df['Marker'].nunique()
df = df.drop(columns=['Marker' ] , axis =1)

figdims = (15,10)
fig ,ax = plt.subplots(figsize=figdims)
sns.lineplot(x=nifty['Shares Traded'] , y=nifty['Turnover (Rs. Cr)'] , ax=ax)

figdims = (15,10)
fig , ax = plt.subplots(figsize=figdims)
sns.lineplot(y=nifty['Shares Traded'] , x=nifty['Percentage Change'] , ax=ax)

figdims = (15,10)
fig , ax = plt.subplots(figsize=figdims)
sns.lineplot(x=nifty['Percentage Change'] , y=nifty['Turnover (Rs. Cr)'] , ax=ax)

figdims =(15,10)
fig , ax= plt.subplots(figsize=figdims)
sns.lineplot(x='High' , y='Low' , data=nifty , ax=ax)

figdims =(15,10)
fig , ax= plt.subplots(figsize=figdims)
sns.lineplot(x='Percentage Change' , y='High' , data=nifty , ax=ax)

figdims =(15,10)
fig , ax= plt.subplots(figsize=figdims)
sns.lineplot(x='Percentage Change' , y='Low' , data=nifty , ax=ax)

figdims =(15,10)
fig , ax= plt.subplots(figsize=figdims)
sns.lineplot(x='Percentage Change' , y='Open' , data=nifty , ax=ax)

figdims =(15,10)
fig , ax= plt.subplots(figsize=figdims)
sns.lineplot(x='Percentage Change' , y='Close' , data=nifty , ax=ax)

nifty['Day'] = nifty['Date'].dt.day_name()

nifty = nifty[['Date', 'Day', 'Open', 'High', 'Low', 'Close', 'Shares Traded',
       'Turnover (Rs. Cr)', 'Percentage Change', 'Marker']]

nifty.to_excel('niftycorrect dataset.xlsx')

figdims = (15,10)
fig  , ax = plt.subplots(figsize=figdims)
sns.barplot(x='Day' , y='Shares Traded' , data= nifty , ax=ax)
plt.show()

figdims = (15,10)
fig , ax = plt.subplots(figsize=figdims)
sns.barplot(x='Day' , y='Turnover (Rs. Cr)', data=nifty , ax=ax)
plt.show()

figdims = (15,10)
fig , ax = plt.subplots(figsize=figdims)
sns.scatterplot(x='Day' , y='Turnover (Rs. Cr)',hue='Marker', data=nifty , ax=ax)
plt.show()

figdims = (15,10)
fig , ax = plt.subplots(figsize=figdims)
sns.scatterplot(x='Day' , y='Shares Traded',hue='Marker' ,data=nifty , ax=ax)
plt.show()

def Pivot_Convertor(a,b ,c ):
  d= []
  for i in range(len(a)):
    d.append((a[i] + b[i] + c[i])/1.5)
  return d

nifty['Pivoot'] = Pivot_Convertor(nifty['High'] , nifty['Close'] ,nifty['Low'])

nifty['Pivot'] = nifty['Pivoot']

nifty.head()

nifty.describe()

