import pandas as pd
# data = pd.read_csv('../datasets/NASDAQ.txt', sep=" ", header=None)
data = pd.read_fwf('../datasets/NYSE.txt')

company_list = []

for index, row in data.iterrows():
    print(index)
    str1 = row[0]
    str2 = str1.split()
    company_list.append(str2[0])

print("success")
print(company_list)