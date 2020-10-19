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

df['Marker']

df['Marker'].nunique()

df.head()

df = df.drop(columns=['Marker' ] , axis =1)

nifty.head()

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

nifty.describe()

nifty['Percentage Change'].sum()

from datetime import  datetime

nifty['Day'] = nifty['Date'].dt.day_name()

nifty.head()

nifty.columns

nifty = nifty[['Date', 'Day', 'Open', 'High', 'Low', 'Close', 'Shares Traded',
       'Turnover (Rs. Cr)', 'Percentage Change', 'Marker']]

nifty.head()

nifty.tail()

nifty.to_excel('niftycorrect dataset.xlsx')

figdims = (15,10)

fig  , ax = plt.subplots(figsize=figdims)
sns.barplot(x='Day' , y='Shares Traded' , data= nifty , ax=ax)
plt.show()

nifty['Day'].nunique()

nifty['Day'].isnull().sum()

nifty.Date[23]

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
