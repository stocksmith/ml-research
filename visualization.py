import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as web
from scipy import stats
import seaborn as sns
from datetime import datetime
import computation as cp

def plot_norm(symbol , df):
    df = cp.norm_dist(symbol,df)
    df.plot()
    plt.title("The normal distribution of {}".format(symbol))
    plt.legend()
    plt.show()

def plot_daily(symbol,df):
    df = cp.daily_return(symbol,df)
    df['Daily Returns of {}'.format(symbol)].plot(title = "Daily Returns of {}".format(symbol))
    plt.legend()
    plt.show()

def plot_cumulative(symbol,df):
    df = cp.cumulative_return(symbol,df)
    df['Cumulative Returns of {}'.format(symbol)].plot(title = "Cumulative Returns of {}".format(symbol))
    plt.legend()
    plt.show()

def plot_bb(symbol, df):
    df = cp.bollinger_bands(symbol,df)
    ax = df["Adj Close"].plot(title = "Bollinger Bounds")
    df["Rolling Mean"].plot(label = "Rolling Mean", ax=ax)
    df["Upper Bound"].plot(label = "Upper Bound", ax=ax)
    df["Lower Bound"].plot(label = "Lower Bound", ax=ax)
    plt.legend()
    plt.show()

def plot_alpha_beta(symbols, df1, df2):
    '''
    Parameters:
    symbols = list of 2 symbols to find correlation
    df1 = Dataframe for first symbol
    df2 - Dataframe for second symbol
    Sample Run
    symbol = ['GOOG', "AAPL"]
    start = "2015-01-01"
    end = datetime.today().strftime('%Y-%m-%d')
    df1 = pd.DataFrame(web.get_data_yahoo(symbol[0], start = start, end = end)['Adj Close'])
    df2 = pd.DataFrame(web.get_data_yahoo(symbol[1], start = start, end = end)['Adj Close'])
    plot_alpha_beta(symbol,df1, df2)
    '''
    df1 = df1.rename(columns = {"Adj Close" : symbol[0]})
    df2 = df2.rename(columns = {"Adj Close" : symbol[1]})
    df_return = df1.join(df2)
    title = symbol[1] + ' vs ' + symbol[0]
    beta , alpha = np.polyfit(df_return[symbol[0]] , df_return[symbol[1]] , 1)
    df_return.plot(kind = 'scatter', x = symbol[0], y = symbol[1], edgecolor = 'black', title  = title)
    plt.plot(df_return[symbol[0]] , beta*df_return[symbol[0]] + alpha , color='red')
    print("Correlation of " , symbol[0], ' and ',  symbol[1], ' is: ')
    print(np.array(df_return.corr(method='pearson'))[0,1])
    plt.show()




