# -*- coding: utf-8 -*-
"""2nd_half_cnn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-OS06GV8w3ROt--XvRsswaTaRhplWCr0
"""

import tensorflow as tf
import matplotlib.pyplot as plt

import numpy as np
from tensorflow import keras


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
#x_train = np.expand_dims(x_train, axis = 3)
x_train.shape
#y_train = np.expand_dims(y_train, axis = 1)
#type(x_train)
y_train.shape
plt.imshow(x_train[2])

import os
import tensorflow as tf
#strides is a list containing no. of col and no. of rows to skip
def ConvNet(img):
    print(img.shape)
    conv1 = tf.layers.conv2d(img, filters = 8, kernel_size=[2,2], activation = tf.nn.leaky_relu, use_bias = True, padding = 'same', strides=[2,2])
    print(conv1.shape)
    pool1 = tf.layers.max_pooling2d(conv1, pool_size=[2,2], strides=[2,2])
    print(pool1.shape)
    conv2 = tf.layers.conv2d(pool1, filters = 16, kernel_size=[2,2], activation = tf.nn.leaky_relu, use_bias = True, padding = 'same', strides=[2,2])
    print(conv2.shape)
    pool2 = tf.layers.max_pooling2d(conv2, pool_size=[4,4], strides=[2,2])
    print(pool2.shape)
    flat_img = tf.layers.flatten(pool2)
    print(flat_img.shape)
    dense1 = tf.layers.dense(flat_img, 64)  #1st hiddden layer, 64 is number of neurons to which the output of first layer should go
    print(dense1.shape)
    dense2 = tf.layers.dense(dense1, 1)     #OUTPUT LAYER
    #print(dense2)
    return dense2

#POOLING DOESN"T WORK ON 3rd DIMENSION
#None is the batch size(COuld be anything)
x = tf.placeholder(dtype=tf.float32, shape=[None, 32, 32, 3])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])
y_pred = ConvNet(x)
error = tf.reduce_sum(tf.squared_difference(y,y_pred))  #reduce_sum takes the average of all errors in one batch and sends it for back-prop
learning_rate = 0.001
trainer = tf.train.AdamOptimizer(learning_rate).minimize(error)       #one of the versions of back-prop, but better
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
#     x_train = np.expand_dims(x_train,axix = 3)
    for i in range(0,10):
      loss,_ = sess.run([error,trainer],feed_dict = {x:x_train,y:y_train})
      print('Epoch: {0},loss: {1}'.format(i,loss))
#    saver.save(sess,"./my-model")
