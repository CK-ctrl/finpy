import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)


# Here in DataReader, parameters are stock_tick, website/source, start, end.
df = web.DataReader('TSLA','yahoo',start,end)
# print(df.head())


# It seems that this is not working properly. There is some error while using pandas_datareader.
# Instead, I'll use my own web scrapper that will get all of the relevant data.

df.to_csv('tsla.csv')