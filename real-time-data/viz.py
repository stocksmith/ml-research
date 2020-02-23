import matplotlib
import matplotlib.pyplot as plt
import pylab as pl
import pandas pd
matplotlib.style.use('ggplot')

msft = pd.read_csv(filepath_or_buffer = "../datasets/msft.csv")

for index, row in a.iterrows():

plt.figure(figsize=(10,5))
pl.plot(timestamps, magnitude_result, 'r-',color="red",label='unfiltered')
plt.title("Three Axis Acceleration")
pl.grid()
pl.show()