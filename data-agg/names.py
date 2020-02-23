import pandas as pd
# data = pd.read_csv('../datasets/NASDAQ.txt', sep=" ", header=None)
data = pd.read_fwf('../datasets/NASDAQ.txt')

company

for index, row in data.iterrows():
    print(index)
    str1 = row[0]
    str2 = str1.split()
    print(str2[0])