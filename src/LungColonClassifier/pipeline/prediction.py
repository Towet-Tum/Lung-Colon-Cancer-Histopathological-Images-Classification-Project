import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from LungColonClassifier.utils.common import load_data, process_data
from tensorflow.keras.preprocessing.image import load_img


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def makePrediction(self):
        train_dataset = os.path.join(
            "artifacts", "data_ingestion", "lung_colon_image_set"
        )
        df = load_data(train_dataset)
        train_gen, _, _ = process_data(df)
        model = load_model("artifacts/training/lung.model.Xception.h5")
        img = image.load_img(self.filename, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        clas = np.argmax(model.predict(img))
        label_names = train_gen.class_indices
        dict_class = dict(zip(list(range(len(label_names))), label_names))
        name = dict_class[clas]
        print(f"Label name ::: {label_names}")
        print(f"the Dictrionary:::: {dict_class}")
        print(f"The class name ::: {clas}")
        return name


if __name__ == "__main__":
    img = "artifacts/data_ingestion/lung_colon_image_set/lung_image_sets/lung_n/lungn4.jpeg"

    pred = PredictionPipeline(img)
    result = pred.makePrediction()
    print(f"The output of predictions:: {result}")
