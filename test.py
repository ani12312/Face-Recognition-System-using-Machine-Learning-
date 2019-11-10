import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
def test_my_model():
    test_path="C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\yourdata"
    test_batches=ImageDataGenerator().flow_from_directory(
        test_path,
        target_size=(64,64),
        classes=os.listdir("C:\\Users\\ANIRBAN MISRA\\Downloads\\originalimages_part1\\yourdata"),
        batch_size=40
    )
    model=load_model("C:\\Users\\ANIRBAN MISRA\\Downloads\\my_model_train.h5")
    pred=model.predict_classes(test_batches,batch_size=None)
    labels=test_batches.class_indices
    labels={value: key for key, value in labels.items()}
    return(labels[pred[0]])