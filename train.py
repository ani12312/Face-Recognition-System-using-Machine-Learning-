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
def train_my_model():
    train_path="C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\trainparent"
    train_batches=ImageDataGenerator().flow_from_directory(
        train_path,
        target_size=(64,64),
        classes=os.listdir("C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\trainparent"),
        batch_size=40
    )
    
    model=my_model(train_batches)
    model.save("C:\\Users\\ANIRBAN MISRA\\Downloads\\my_model_train.h5")
def my_model(train_batches):
    nclasses=len(os.listdir("C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\trainparent"))
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(64,64,3)))
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
    model.add(Dense(nclasses, activation='softmax'))#number of classes=53
    model.compile(Adam(lr=.0001), loss='binary_crossentropy',metrics=['accuracy'])
    model.fit_generator(train_batches,steps_per_epoch=100,epochs=600)
    return model

