import os
import pandas as pd
import numpy as np
import json
import pickle

path = os.getcwd()

data = []

with open(path+'/example.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '').split(',') # 將每句最後的 /n 取代成空值後，再以逗號斷句
        data.append(line)


df = pd.DataFrame(data[1:]) # 選取資料
df.columns = data[0] # data[0] 為欄位名稱


df.to_json(path+'/example_01.json')

df.set_index('id', inplace=True)
df.to_json(path+'/example_02.json', orient='index')



with open(path+'/example_02.json', 'r') as f:
    j2 = json.load(f)

# 一個專門儲存 numpy array 的檔案格式 使用 npy 通常可以讓你更快讀取資料喔!

array = np.array(data[1:])
np.save(arr=array, file= path+'/example.npy')
array_back = np.load(path+'/example.npy')

#存成 pickle 檔
#什麼都包，什麼都不奇怪的 Pickle
with open(path+'/example.pkl', 'wb') as f:
    pickle.dump(file=f, obj=data)
with open(path+'/example.pkl', 'rb') as f:
    pkl_data = pickle.load(f)

print(pkl_data)



