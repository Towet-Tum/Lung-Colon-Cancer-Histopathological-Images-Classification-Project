import pandas as pd 
import os
import tensorflow as tf
from tensorflow.keras.applications import Xception 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adamax
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau 
from tensorflow.keras.models import Model 
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config 


    def load_data(self):
        
        filepaths = []
        labels = []
        # Get a list of subdirectories 
        folds = os.listdir(self.config.dataset)
        # Iterate over each fold in the dataset 
        for fold in folds:
            foldpath = os.path.join(self.config.dataset, fold)
            flist = os.listdir(foldpath)
        # Iterate over each file in the current fold
            for f in flist:
                f_path = os.path.join(foldpath, f)
                filelist = os.listdir(f_path)
        # Iterate over each file in the current fold
                for file in filelist:
                    fpath = os.path.join(f_path, file)
                    filepaths.append(fpath)
        # Determine the label based on the subdirectory (f)
                    if f == 'colon_aca':
                        labels.append('Colon Adenocarcinoma')

                    elif f == 'colon_n':
                        labels.append('Colon Benign Tissue')

                    elif f == 'lung_aca':
                        labels.append('Lung Adenocarcinoma')

                    elif f == 'lung_n':
                        labels.append('Lung Benign Tissue')

                    elif f == 'lung_scc':
                        labels.append('Lung Squamous Cell Carcinoma')

        # Concatenate data paths with labels into one dataframe
        Fseries = pd.Series(filepaths, name= 'filepaths')
        Lseries = pd.Series(labels, name='labels')
        df = pd.concat([Fseries, Lseries], axis= 1) 
        return df
    

    def process_data(self, df):

        labels = df['labels']
        train_df, temp_df = train_test_split(df, train_size=0.8, shuffle=True, random_state=123, stratify=labels)
        valid_df, test_df = train_test_split(temp_df, train_size=0.5, shuffle=True, random_state=123, stratify=temp_df['labels'])
        
        batch_size = 32
        img_size = (224,224)
        channels = 3
        img_shape = (img_size[0], img_size[1], channels)

        # Create ImageDataGenerator  for training and testing
        tr_gen = ImageDataGenerator()
        ts_gen = ImageDataGenerator()

        # Training data generator
        train_gen = tr_gen.flow_from_dataframe(train_df, x_col='filepaths', y_col='labels',
                                            target_size=img_size, class_mode='categorical',
                                            color_mode='rgb', shuffle=True, batch_size=batch_size)

        # Validation data generator
        valid_gen = ts_gen.flow_from_dataframe(valid_df, x_col='filepaths', y_col='labels',
                                            target_size=img_size, class_mode='categorical',
                                            color_mode='rgb', shuffle=True, batch_size=batch_size)

        # Testing data generator
        test_gen = ts_gen.flow_from_dataframe(test_df, x_col='filepaths', y_col='labels',
                                            target_size=img_size, class_mode='categorical',
                                            color_mode='rgb', shuffle=False, batch_size=batch_size)
        return train_gen, valid_gen, test_gen

    def get_callbacks(self):
        callbacks = []

        # ModelCheckpoint
        checkpoint = ModelCheckpoint(filepath=self.config.model_path, verbose=1, monitor='val_accuracy', mode='max') 
        callbacks.append(checkpoint) 

        # Import ReduceLROnPlateau if not imported earlier
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6, verbose=1)
        callbacks.append(reduce_lr)

        # Import EarlyStopping if not imported earlier
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1)
        callbacks.append(early_stopping)

        return callbacks 
        
    def train(self):
        data = self.load_data()
        train_gen, valid_gen, test_gen = self.process_data(data)
        

        img_size = (224,224)
        channels = 3
        img_shape = (img_size[0], img_size[1], channels)
        class_count = len(list(train_gen.class_indices.keys()))


        # Create Xception base model
        base_model = Xception(input_shape=img_shape, include_top=False, weights='imagenet')

        base_model.trainable = True

        x = base_model.output

        x = GlobalAveragePooling2D()(x)

        y = Dense(256, activation='relu')(x)

        predictions = Dense(class_count, activation='softmax', name='final')(y)

        model_Xception = Model(inputs=base_model.input, outputs=predictions)  


        model_Xception.compile(optimizer=Adamax(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy']) 


        callbacks=self.get_callbacks() 
        model_Xception.fit(train_gen,epochs=10,validation_data=valid_gen,callbacks=[callbacks])
        
        