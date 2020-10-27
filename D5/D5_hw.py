# 把連結填入
target_url = 'https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt'

import requests
import pandas as pd
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

response = requests.get(target_url)
data = response.text

# 用 request 傳送回來的資料不會認得斷行符號
datasets = data[0:10000].split('\n')

image_lists = dict()

for data in datasets:
    temp = data.split('\t')
    image_lists[temp[0]] = temp[1]
    
df = pd.DataFrame.from_dict(image_lists, orient='index')


def img2arr_fromURLs(url_list, resize = False):
    img_list = []
    for url in url_list:
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200 :
            img = Image.open(BytesIO(response.content))
            img_list.append(img)
    return img_list

result = img2arr_fromURLs(df[0:5][0].values)

print("Total images that we got: %i " % len(result))

for im_get in result:
    plt.imshow(im_get)
    plt.show()