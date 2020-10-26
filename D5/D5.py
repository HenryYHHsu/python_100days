import pandas as pd
import numpy as np

data = dict()
data = [{"國家":'Taiwan', "人口": np.random.randint(10000)},
        {"國家":'Japan', "人口": np.random.randint(10000)},
        {"國家":'Korea', "人口": np.random.randint(10000)}]
data_frame = pd.DataFrame(data)

# 找出人口最多的國家
max_popluar_id = data_frame['人口'].idxmax()
# #loc指向的是index的名稱
print(data_frame.loc[max_popluar_id]) 
#iloc指向的是index的位置
print(data_frame.iloc[max_popluar_id]) 

print (data_frame.groupby(by='人口').max())