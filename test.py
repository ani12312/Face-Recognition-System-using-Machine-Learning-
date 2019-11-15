import keras
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
global forged
forged="forged"
def perfect(pred):
    arr=[]
    count_perfect=0
    count_forged=0
    for i in range(0,len(pred)):
        for j in range(i,len(pred)):
            if pred[i]==pred[j]:
                arr.append(pred[i])
    if(len(arr)>1):
        return (forged)
    else:
        return (arr[0])
def test_my_model():
    test_path="C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\yourdata"
    train_path="C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\trainparent"
    test_batches=ImageDataGenerator().flow_from_directory(
        test_path,
        target_size=(64,64),
        classes=os.listdir("C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\yourdata"),
        batch_size=40,
        shuffle=False
    )
    train_batches=ImageDataGenerator().flow_from_directory(
        train_path,
        target_size=(64,64),
        classes=os.listdir("C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\trainparent"),
        batch_size=40,
        shuffle=False
    )
    model=load_model("C:\\Users\\ANIRBAN MISRA\\Downloads\\my_model_train.h5")
    pred=model.predict_classes(test_batches,batch_size=None)
    pred=list(pred)
    print(pred)
    if len(pred)>5:
        pred1=perfect(pred)
    else:
        return (forged)
    if pred1!=forged:
        labels=train_batches.class_indices
        labels={value: key for key, value in labels.items()}
        return(labels[pred1])
    else:
        return (forged)