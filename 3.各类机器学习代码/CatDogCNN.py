'''
Convolution kernel:
Identity-
0 0 0
0 1 0
0 0 0

Edge detection-
1  0  -1
0  0  0
-1 0  1

0  1  0
1  -4 1
0  1  0

-1  -1 -1
-1  8  -1
-1  -1 -1

Sharpen
0  1  0
1  -5 1
0  1  0
...
'''

import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm

Train_dir = '/Users/unlimitediw/PycharmProjects/CatDog/DOGandCat/train'
Test_dir = '/Users/unlimitediw/PycharmProjects/CatDog/DOGandCat/test'
IMG_SIZE = 100
LR = 0.001

MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR,'2conv-basic')

def label_img(img):
    word_label = img.split('.')[-3]
    if word_label == 'cat':return [1,0]
    elif word_label == 'dog': return [0,1]


def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(Train_dir)):
        label = label_img(img)
        path = os.path.join(Train_dir,img)
        # !! to Gray
        img = cv2.imread(path,3)
        #cv2.imwrite('kk.jpg',img)
        # !! resize
        img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
        training_data.append([np.array(img),np.array(label)])

    shuffle(training_data)
    np.save('train_data.npy',training_data)
    return training_data

def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(Test_dir)):
        path = os.path.join(Test_dir,img)
        img_num = img.split('.')[0]
        img = cv2.imread(path,3)
        img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
        testing_data.append([np.array(img),img_num])
    shuffle(testing_data)
    np.save('test_data.npy',testing_data)

a = create_train_data()
b = process_test_data()
train_data = np.load('train_data.npy')


import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data,dropout,fully_connected
from tflearn.layers.estimator import regression

# adding
import tensorflow as tf
tf.reset_default_graph()

convnet = input_data(shape=[None,IMG_SIZE,IMG_SIZE,3],name = 'input')

# let it be more deeper 50% -> 70% just add two more conv and pool steps.
# pading = same
convnet = conv_2d(convnet,32,5,activation='relu')
convnet = max_pool_2d(convnet,5)

convnet = conv_2d(convnet,64,5,activation='relu')
convnet = max_pool_2d(convnet,5)

convnet = conv_2d(convnet,32,5,activation='relu')
convnet = max_pool_2d(convnet,5)

convnet = conv_2d(convnet,64,5,activation='relu')
convnet = max_pool_2d(convnet,5)

convnet = conv_2d(convnet,32,5,activation='relu')
convnet = max_pool_2d(convnet,5)

convnet = conv_2d(convnet,64,5,activation='relu')
convnet = max_pool_2d(convnet,5)

convnet = fully_connected(convnet,1024,activation = 'relu')
convnet = dropout(convnet,0.8)

convnet = fully_connected(convnet,2,activation='softmax')
convnet = regression(convnet,optimizer = 'adam',learning_rate = LR,loss = 'categorical_crossentropy',name = 'targets')

model = tflearn.DNN(convnet,tensorboard_dir = 'log')

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    pass

# simple split
train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,3)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,3)
test_y = [i[1] for i in test]

# model.fit({'input':X},{'targets':Y},n_epoch=4,validation_set=({'input':test_x},{'targets':test_y}),snapshot_step=50000,show_metric=True,run_id=MODEL_NAME)

# model.save(MODEL_NAME)


import matplotlib.pyplot as plt

test_data = np.load('test_data.npy')
fig = plt.figure()

for num,data in enumerate(test_data[:12]):

    img_num = data[1]
    img_data = data[0]

    y = fig.add_subplot(3,4,num+1)
    orig = img_data
    data = img_data.reshape(IMG_SIZE,IMG_SIZE,3)
    model_out = model.predict([data])[0]
    if np.argmax(model_out) == 1: str_label = 'Dog'
    else: str_label = 'Cat'

    y.imshow(orig)
    plt.title(str_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)

'''
img = cv2.imread('/Users/unlimitediw/PycharmProjects/CatDogClassification/dogTest.jpeg', 0)
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

orig = np.array(img)
data = orig.reshape(IMG_SIZE,IMG_SIZE,1)
model_out = model.predict([data])[0]
if np.argmax(model_out) == 1: str_label = 'Dog'
else: str_label = 'Cat'
y.imshow(orig)
plt.title(str_label)
y.axes.get_xaxis().set_visible(False)
y.axes.get_yaxis().set_visible(False)
'''

plt.show()