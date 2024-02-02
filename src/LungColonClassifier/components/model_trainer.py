import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.applications import Xception
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adamax
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.models import Model
from LungColonClassifier.utils.common import load_data, process_data
from LungColonClassifier.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_callbacks(self):
        callbacks = []

        # ModelCheckpoint
        checkpoint = ModelCheckpoint(
            filepath=self.config.model_path,
            verbose=1,
            monitor="val_accuracy",
            mode="max",
        )
        callbacks.append(checkpoint)

        # Import ReduceLROnPlateau if not imported earlier
        reduce_lr = ReduceLROnPlateau(
            monitor="val_loss", factor=0.2, patience=3, min_lr=1e-6, verbose=1
        )
        callbacks.append(reduce_lr)

        # Import EarlyStopping if not imported earlier
        early_stopping = EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True, verbose=1
        )
        callbacks.append(early_stopping)

        return callbacks

    def train(self):
        data = load_data(self.config.dataset)
        train_gen, valid_gen, test_gen = process_data(data)

        img_size = (224, 224)
        channels = 3
        img_shape = (img_size[0], img_size[1], channels)
        class_count = len(list(train_gen.class_indices.keys()))

        # Create Xception base model
        base_model = Xception(
            input_shape=img_shape, include_top=False, weights="imagenet"
        )

        base_model.trainable = True

        x = base_model.output

        x = GlobalAveragePooling2D()(x)

        y = Dense(256, activation="relu")(x)

        predictions = Dense(class_count, activation="softmax", name="final")(y)

        model_Xception = Model(inputs=base_model.input, outputs=predictions)

        model_Xception.compile(
            optimizer=Adamax(learning_rate=0.001),
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )

        callbacks = self.get_callbacks()
        model_Xception.fit(
            train_gen, epochs=10, validation_data=valid_gen, callbacks=[callbacks]
        )
