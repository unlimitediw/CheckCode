import sys
from PIL import Image
import numpy as np
from tqdm import tqdm
import cv2
import os
curdir = '/Users/unlimitediw/PycharmProjects/ImageSearchGen/SavePath/'



from matplotlib import cm
def pil_grid(images, max_horiz = 5):
    n_images = len(images)
    n_horiz = min(n_images, max_horiz)
    h_sizes, v_sizes = [0] * n_horiz, [0] * (n_images // n_horiz + 1)
    for i, im in enumerate(images):
        print(i,type(im))
        h, v = i % n_horiz, i // n_horiz
        h_sizes[h] = max(h_sizes[h], im.shape[1])
        print(v,len(v_sizes))
        v_sizes[v] = max(v_sizes[v], im.shape[0])
    h_sizes, v_sizes = np.cumsum([0] + h_sizes), np.cumsum([0] + v_sizes)
    im_grid = Image.new('RGB', (h_sizes[-1], v_sizes[-1]), color='white')
    print(type(im_grid),type(images[0]))
    for i, im in enumerate(images):
        im = Image.fromarray(im.astype('uint8'), 'RGB')
        box = (h_sizes[i % n_horiz],v_sizes[i // n_horiz])
        im_grid.paste(im, box)
    return im_grid

ImageDic = {}
imagelist = []
count = 0

for img_name in tqdm(os.listdir(curdir)):
    imgKey = img_name.split('_')[0] + '_' + img_name.split('_')[1]
    path = os.path.join(curdir, img_name)
    img = cv2.imread(path, 3)
    if imgKey not in ImageDic:
        ImageDic[imgKey] = [img]
    else:
        ImageDic[imgKey].append(img)

for key in ImageDic.keys():
    print(key)
    BigIMG = pil_grid(ImageDic[key],max_horiz=10)
    BigIMG.save("/Users/unlimitediw/PycharmProjects/ImageSearchGen/CarResult/"+ key + '.png')

