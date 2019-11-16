import keras
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

def test_my_model():
    test_path="yourdata"
    test_batches=ImageDataGenerator().flow_from_directory(
        test_path,
        target_size=(64,64)
    )
    train=ImageDataGenerator().flow_from_directory(
        "trainparent",
        target_size=(64,64)
    )
    model=load_model("model.h5")
    pred=model.predict_classes(test_batches, batch_size=None)
    print(train.filenames)
    return pred

print(test_my_model())