import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import yfinance as yf
import math
import os
import sys
import pandas as pd
pd.options.mode.chained_assignment = None


class suppress_stdout_stderr(object):
    '''
    Used to supress the verbose output of the inner workings of the FB prophet model
    '''
    def __init__(self):
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

    def __exit__(self, *_):
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])

def fb_predict(dfi, plot = False, days =1):
    '''
    This function takes in:
    dfi - A dataframe with just the column of close price named as Close and date as index 
    plot - Whether you want to plot the resulyts or not( Default is False)
    days - Number of days into the future you want to predict (Dafault is 1)

    This function returns:
    mean_err - The mean percentage error in calculations
    pred - A pandas datafrmae with predictions, upper and lower bounds

    '''
    df = dfi.copy()
    arr = [i for i in range(len(df))]
    ar = df.index
    df.index= arr
    df['ds'] = ar
    df = df[['ds', 'Close']]
    df.rename(columns = {"Close":'y'}, inplace = True)

    train_length = math.floor(0.1*len(df))
    train = df[:-train_length]
    test = df[-train_length:]
    m = Prophet(daily_seasonality = True) 
    with suppress_stdout_stderr():
        m.fit(train) 
    future = m.make_future_dataframe(periods=train_length) 
    prediction = m.predict(future)
    test_predict = prediction[-train_length:]
    test['predict'] = test_predict['trend']
    test['error'] =((test['y'] - test['predict'])/test['y'])*100
    mean_err = round(test['error'].mean(),3)
    mn = Prophet(daily_seasonality = True) 
    with suppress_stdout_stderr():
        mn.fit(df) 
    future = mn.make_future_dataframe(periods=days) 
    prediction = mn.predict(future)
    pred = pd.DataFrame(prediction[-days:][['ds','trend', 'yhat_upper', 'yhat_lower']])
    pred.rename(columns = {'ds' : 'Date', 'trend':'Guess', 'yhat_lower':'Lower Bound', 'yhat_upper':'Upper Bound'}, inplace = True)
    pred.set_index(np.arange(1,len(pred)+1), inplace = True)
    if plot:
        m.plot(prediction)
        plt.title("Prediction of the AZPN Stock Price using the Prophet")
        plt.xlabel("Date")
        plt.ylabel("Close Stock Price")
        plt.show()
    return mean_err, pred

#Sample Run 
# symbol = "AZPN"
# days = 5
# stock = yf.Ticker(symbol)
# df = stock.history(period="max")
# df = df[['Close']]
# me , pred= fb_predict(df, days = days)
# print("\n The prediction for {} after {} days is :\n".format(symbol, days))
# print(pred)
# print("\n Mean Percentage Error : ", me)



