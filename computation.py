import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as web
from datetime import datetime
from scipy import stats
from dateutil.relativedelta import relativedelta

today = datetime.today().strftime('%Y-%m-%d')

def changeCol(df, col, name):
    df = df.rename(columns = {col : name})
    return df

def norm_dist(symbol,df):
    '''
    This function takes:
    symbol - The symbol of the underlying stock
    df- pandas dataframe with just the column of close price with title Adj Close
    Returns a dataframe with the normally distributed values of the stock data. 
    '''
    df =changeCol(df, "Adj Close","Noarmallized {}".format(symbol))
    #Normalizing the Ditribution
    df =(df)/df.iloc[0]-1
    return df

def daily_return(symbol,df):
    '''
    This function takes:
    symbol - The symbol of the underlying stock
    df- pandas dataframe with just the column of close price with title Adj Close
    Returns a dataframe with the daily of the stock data. 
    '''
    df_return = df.pct_change()
    df_return.iloc[0] = 0
    df_return = changeCol(df_return,"Adj Close", "Daily Returns of {}".format(symbol))
    return df_return

def cumulative_return(symbol,df):
    '''
    This function takes:
    symbol - The symbol of the underlying stock
    df- pandas dataframe with just the column of close price with title Adj Close
    Returns a dataframe with the cumulative returns of the stock data. 
    '''
    df_cr = df
    df_cr= changeCol(df_cr,'Adj Close',"Cumulative Returns of  {}".format(symbol))
    df_cr[1:] = (df[1:]/df.iloc[0])-1
    df_cr.iloc[0] = 0
    return df_cr
def bollinger_bands(symbol,df, rolling_range = 20):
    '''
    This function takes:
    symbol - The symbol of the underlying stock
    df- pandas dataframe with just the column of close price with title Adj Close
    rolling_range - The amount of days to calculate the rolling mean
    Returns a dataframe with the the SMA, Upper Band and Lower Band for the stock data. 
    '''
    #Moving stats 
    rm = pd.DataFrame(df['Adj Close'].rolling(rolling_range).mean())
    rstd = pd.DataFrame(df.rolling(rolling_range).std())
    ub = pd.DataFrame(rm+ 2*rstd)
    lb = pd.DataFrame(rm- 2*rstd)

    rm = changeCol(rm,'Adj Close',"Rolling Mean")
    rstd = changeCol(rstd,'Adj Close',"Rolling Deviation")
    ub = changeCol(ub,'Adj Close',"Upper Bound")
    lb = changeCol(lb,'Adj Close',"Lower Bound")
    df_bb = df.join([rm,rstd,ub,lb])

    return df_bb
def beta(symbol):
    '''
    This function takes:
    symbol - Name of stock ticker
    returns - Beta value of the stock
    '''
    end =  datetime.now()
    start = end - relativedelta(years=5)
    start = start.strftime('%m-%d-%Y')
    ls = start.split('-')
    ls[1] = "01"
    start = '-'.join(ls)
    df = pd.DataFrame(web.get_data_yahoo(symbol, start = start, end = end,interval='m')['Adj Close'])
    df = changeCol(df, "Adj Close", "Price")
    
    df_spy = pd.DataFrame(web.get_data_yahoo('SPY', start = start, end = end,interval='m')['Adj Close'])
    df_spy = changeCol(df_spy, "Adj Close", "S&P")
    
    df_spy= df_spy.pct_change()
    df = df.pct_change()

    df = df.join(df_spy)
    df = df.dropna()

    X = df['S&P']
    Y = df['Price']
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    print("5Y monthly Beta for {}:".format(symbol), round(slope,3))
    return slope



