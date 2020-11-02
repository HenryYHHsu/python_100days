import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# dir_data = './data/'

# f_app_train = os.path.join(dir_data, 'application_test.csv')
# app_train = pd.read_csv(f_app_train)


# test_data = app_train['AMT_GOODS_PRICE']

# # calculate variance
# test_data_var = test_data.var()
# test_data_avg = test_data.mean()

# print(test_data_var)
# print('============')
# print(test_data_avg)

# print('----直方圖----')
# plt.hist(test_data)
# plt.title("histogram") 
# plt.show()

#---------------------------------------

# plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")

# plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='r')
# plt.legend()
# plt.xlabel('bar number')
# plt.ylabel('bar height')

# plt.title('測試畫圖bar')

#plt.show()


# ------------

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('直方圖')
plt.legend()
plt.show()