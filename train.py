# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 07:35:02 2018

@author: Prashant
"""

# In[]
# Imports


import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense,Flatten,Dropout
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
import matplotlib.pyplot as plt
import os,shutil,glob





class DeepNetwork:
    """
        DeepNetwork

    """
    def __init__(self):
        pass

    @staticmethod
    def train(model, training_set, valid_set=None, epoc=600, batch=40):
        train_batches = ImageDataGenerator().flow_from_directory(
            training_set,
            target_size=(64,64),
            batch_size=batch
        )
        model.fit_generator(train_batches,steps_per_epoch=100,epochs=epoc)
        return model

    def load(self, path="model.bin"):
        return load_model(path)

    @staticmethod
    def save(model, path="model.bin"):
        model.save(path)

    @staticmethod
    def model(input_shape, output_shape,
              log=True,
              loss='categorical_crossentropy',
              optimizer='sgd'):
        """
        Create a model
        :raise: Parent exception
        """
        model = Sequential()
        model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
        model.add(Conv2D(32, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
     
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
     
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
     
        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(output_shape, activation='softmax'))
        model.compile(Adam(lr=.0001), loss='binary_crossentropy',metrics=['accuracy'])

        if log:
            model.summary()

        return model

    @staticmethod
    def shape(data):
        shape = data.shape
        data = np.reshape(data, (-1, 1))
        scaler = MinMaxScaler(feature_range=(-1, 1)).fit(data)
        data = scaler.transform(data)
        return np.reshape(data, shape)

    @staticmethod
    def __key_func(x):
        """
            __key_func(x): Sort the file and folder by alphabetical order.
        """
        pat = re.compile("(\d+)\D*$")
        mat = pat.search(os.path.split(x)[-1])
        if mat is None:
            return x
        return "{:>10}".format(mat.group(1))

    @staticmethod
    def pridict(model, value):
        return model.predict_classes(value)

emp_classes=len(os.listdir("trainparent"))

model = DeepNetwork.model((64,64,3), emp_classes)
model = DeepNetwork.train(model, "trainparent", epoc=1)
DeepNetwork.save(model)