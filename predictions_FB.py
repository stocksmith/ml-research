import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import yfinance as yf
import math
import os
import sys
from sklearn.metrics import mean_squared_error


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

def fb_error(df):
    train_length = math.floor(0.1*len(df))
    train = df[:-train_length]
    test = df[-train_length:]
    error_check = Prophet(daily_seasonality = True) 
    with suppress_stdout_stderr():
        error_check.fit(train) 
    future = error_check.make_future_dataframe(periods=train_length) 
    prediction = error_check.predict(future)
    test_predict = prediction[-train_length:]
    test['predict'] = test_predict['trend']
    test['error'] =((test['y'] - test['predict'])/test['y'])*100
    mean_err = round(test['error'].mean(),3)
    return mean_err


def fb_predict(df, plot: bool=False, days: int=1, verbose: bool=True, error= False):
    '''
    :param dfi - A dataframe with just the column of close price named as Close and date as index 
    :param plot - Whether you want to plot the resulyts or not( Default is False)
    :param days - Number of days into the future you want to predict (Dafault is 1)
    :param verbose - If you want the output of the model workings 

    :type dfi - pandas.dataframe
    :type plot - Boolean Value
    :type days - Integer
    :type verbose - Boolean Value

    :return mean_err - The mean percentage error in calculations
    :return pred - A pandas datafrmae with predictions, upper and lower bounds

    :rtype mean_err - float
    :rtype pred - pandas.dataframe
    '''
    pd.options.mode.chained_assignment = None
    arr = [i for i in range(len(df))]
    ar = df.index
    df.index= arr
    df['ds'] = ar
    df = df[['ds', 'Close']]
    df.rename(columns = {"Close":'y'}, inplace = True)

    if error:
        mean_err = fb_error(df)

    predictions = Prophet(daily_seasonality = True) 
    if not verbose:
        with suppress_stdout_stderr():
            predictions.fit(df) 
    future = predictions.make_future_dataframe(periods=days) 
    prediction = predictions.predict(future)
    pred = pd.DataFrame(prediction[-days:][['ds','trend', 'yhat_upper', 'yhat_lower']])
    pred.rename(columns = {'ds' : 'Date', 'trend':'Guess', 'yhat_lower':'Lower Bound', 'yhat_upper':'Upper Bound'}, inplace = True)
    pred.set_index(np.arange(1,len(pred)+1), inplace = True)
    if plot:
        predictions.plot(prediction)
        plt.title("Prediction of the AZPN Stock Price using the Prophet")
        plt.xlabel("Date")
        plt.ylabel("Close Stock Price")
        plt.show()
    if error:
        return mean_err, pred
    else:
        return pred





