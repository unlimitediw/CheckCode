import cv2
from tqdm import tqdm
import os
import numpy as np
import pandas as pd
curdir = '/Users/unlimitediw/PycharmProjects/CitiesPrediction/RoadImage'
savePath = '/Users/unlimitediw/PycharmProjects/CitiesPrediction/SavePath/'

def process_data(dir):
    cur_data = {}
    for img_name in tqdm(os.listdir(dir)):
        path = os.path.join(dir,img_name)
        img = cv2.imread(path,3)
        cur_data[img_name] = np.array(img)
    return cur_data

def tag_spilt_data(path,savePath,imgDic):
    curData = pd.read_csv(path).values
    curName = ''
    for i in range(len(curData)):
        if type(curData[i][0]) == str:
            curName = curData[i][0].split('.')[0] + '.jpg'
        print("!",type(curData[i][11]),curData[i][11])
        print("!!",type(curData[i][12]),curData[i][12])
        print("!!!",type(curName),curName)
        saveData = curData[i][11] +'_'+ curData[i][12] +'_'+ curName.split('_')[0] + '_' + str(curData[i][5]) + '.png'
        leftButtom = (curData[i][7],curData[i][8])
        width = curData[i][9]
        height = curData[i][10]
        #print(imgDic[curName].shape)
        #print(480-height-leftButtom[1],480-leftButtom[1],leftButtom[0],leftButtom[0]+width+1)
        curImg = imgDic[curName][leftButtom[1]:leftButtom[1]+height + 1,leftButtom[0]:leftButtom[0]+width+1,:]
        curImg = cv2.resize(curImg,(128,64))
        cv2.imwrite(savePath+saveData,curImg)

csvPath = ''
Dic = process_data(curdir)
for i in [2]:
    csvPath = '/Users/unlimitediw/PycharmProjects/CitiesPrediction/jsoncsvPath/000000' + str("%.2d" % i) + '.csv'
    tag_spilt_data(csvPath,savePath,Dic)