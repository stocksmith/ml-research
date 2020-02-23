import pandas as pd
# data = pd.read_csv('../datasets/NASDAQ.txt', sep=" ", header=None)
data = pd.read_fwf('../datasets/output_list.txt')
print(data)