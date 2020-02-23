import yfinance as yf
import pandas as pd

msft = yf.Ticker("MSFT")
print(msft)

# get stock info
msft.info

"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}
"""

# get historical market data, here max is 5 years.
a = msft.history(period="100")

a.to_csv('out.csv')