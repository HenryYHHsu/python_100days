
import matplotlib.pyplot as plt
import os
import numpy as np
import skimage.io as skio



path = os.getcwd()

img1 = skio.imread(path+'/example.jpg')
# plt.imshow(img1)
# plt.show()


from PIL import Image
img2 = Image.open(path+'/example.jpg') # 這時候還是 PIL object
img2 = np.array(img2)
# plt.imshow(img2)
# plt.show()


import cv2
# pip install opencv-python
img3 = cv2.imread(path+'/example.jpg')
# cv2.cvtColor() method is used to convert an image from one color space to another. 
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# plt.imshow(img3)
# plt.show()

#將影像存成 mat
import scipy.io as sio
sio.savemat(file_name= path+'/example.mat', mdict={'img': img1})
mat_arr = sio.loadmat(path+'/example.mat')
print(mat_arr.keys())
mat_arr = mat_arr['img']
print(mat_arr.shape)
# plt.imshow(mat_arr)
# plt.show()



