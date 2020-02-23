import matplotlib
import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd
matplotlib.style.use('ggplot')

msft = pd.read_csv(filepath_or_buffer = "msft.csv")

timestamps = []
data_open = []

for index, row in msft.iterrows():
    timestamps.append(row['Date'])
    data_open.append(row['Open'])

plt.figure(figsize=(10,5))
pl.plot(timestamps, data_open, 'r-',color="red",label='unfiltered')
plt.title("MSFT Stock")
pl.grid()
pl.show()