import matplotlib
import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

matplotlib.style.use('ggplot')

msft = pd.read_csv(filepath_or_buffer = "msft.csv")

timestamps = []
data_open = []

for index, row in msft.iterrows():
    timestamps.append(row['Date'])
    data_open.append(row['Open'])


test = find_peaks(data_open)

peaks = test[0]

peak_arr = np.zeros(len(data_open))

# peaks
x = []
# timestamps for those peaks
y = []

for i in peaks:
    peak_arr[i] = data_open[i]
    x.append(data_open[i])
    y.append(timestamps[i])

plt.figure(figsize=(10,5))
pl.plot(timestamps, data_open, 'r-',color="red",label='unfiltered')
plt.plot(y,x,ls="", color="blue",marker="o", label="points")
plt.title("MSFT Stock")
pl.grid()
pl.show()