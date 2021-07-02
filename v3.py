# Handling Data and Graphing


import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df.tail())
print(df.head())


ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
ax1 = plt.subplot2grid((6,1),(0,0), rowspan=1, colspan=1, sharex=ax1) #sharex=x2 will make x2 common between both graps.

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.intsex, df['Volume'])

plt.show()
