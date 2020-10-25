import os
import numpy as np
import pandas as pd
import glob


path = os.getcwd()

origin_data = glob.glob(r'*.csv')[0] # 只讀第一個檔案

print ('#######################')
data  = pd.read_csv(origin_data) # 'application_test.csv 這個檔案'

# row / column
print (data.shape)
row = data.shape[0] # row
column = data.shape[1] #欄

# size row*col
print (data.size)

# 看前 n 行
print (data.head(4))

# 看後 n 行
print (data.tail(10))

