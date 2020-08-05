import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as web
from scipy import stats
import seaborn as sns
from datetime import datetime

pd.options.display.float_format = '{:.5f}'.format

def get_data_close(symbol, start, end):
    df = pd.DataFrame(web.DataReader(symbol, data_source='yahoo', start = start, end = end)['Adj Close'])
    return df

def changeCol(df, col, name):
    df = df.rename(columns = {col : name})
    return df

def norm_dist(symbol, start,end =  datetime.today().strftime('%Y-%m-%d'),plot = False):
    df = get_data_close(symbol, start, end)
    df =changeCol(df, "Adj Close","Noarmallized {}".format(symbol))
    #Normalizing the Ditribution
    df =(df)/df.iloc[0]-1
    if plot:
        df.plot()
        plt.show()
    return df

def daily_return(symbol, start,end =  datetime.today().strftime('%Y-%m-%d'), plot= False):
    df_exp = get_data_close(symbol, start, end)
    df_exp.dropna(inplace = True)
    df_return = df_exp.pct_change()
    df_return.iloc[0] = 0
    df_return = changeCol(df_return,"Adj Close", "Daily Returns {}".format(symbol))
    print(df_return.head())
    if plot:
        df_return['Daily Return'] = df_return['Daily Return']
        df_return['Daily Return'].plot(title = "Daily Returns")
        plt.show()
    return df_return

def cumulative_return(symbol, start,end =  datetime.today().strftime('%Y-%m-%d'),plot=False):
    df_exp = get_data_close(symbol,start,end)
    df_cr = df_exp
    df_cr= changeCol(df_cr,'Adj Close',"Cumulative Return {}".format(symbol))
    df_cr[1:] = (df_exp[1:]/df_exp.iloc[0])-1
    df_cr.iloc[0] = 0
    if plot:
        df_cr['Cumulative Return'] = df_cr['Cumulative Return']
        df_cr.plot(title = "Cumulative Return")
        plt.show()
    return df_cr

def bollinger_bands(symbol, start,end =  datetime.today().strftime('%Y-%m-%d'), rolling_range = 20, plot = False):
    df = get_data_close(symbol,start,end)

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

    if plot:
        ax = df.plot(title = "Bollinger Bounds")
        rm.plot(label = "Rolling Mean", ax=ax)
        ub.plot(label = "Upper Bound", ax=ax)
        lb.plot(label = "Lower Bound", ax=ax)
        plt.show()
    return df_bb
    
def beta(symbol):
    start = '06/01/2015'
    end =  datetime.today().strftime('%m-%d-%Y')
    
    df = pd.DataFrame(web.get_data_yahoo(symbol, start = start, end = end,interval='m')['Adj Close'])
    df = changeCol(df, "Adj Close", "Price")
    
    df_spy = pd.DataFrame(web.get_data_yahoo('SPY', start = start, end = end,interval='m')['Adj Close'])
    df_spy = changeCol(df_spy, "Adj Close", "S&P")
    
    df_spy= df_spy.pct_change()
    df = df.pct_change()

    df = df.join(df_spy)
    df = df.dropna()
    print(df)

    X = df['S&P']
    Y = df['Price']
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    print("5Y monthly Beta for {}:".format(symbol), round(slope,3))
    return slope
'''
Things to be provided:
Start date in format - "YYYY-MM-DD"
For Example:
start = "2015-01-01"
Symbol : Stock Symbol
For Example:
"AAPL"
end - A date at which you want to end the date range, it is assumed to be today by default
Plot - Whether you want to plot the results or not. False by default
'''


#bollinger_bands("AZPN", "2015-01-01", plot = True)


