import os
from LungColonClassifier.constants import *
from LungColonClassifier.utils.common import read_yaml, create_directories 
from LungColonClassifier.entity.config_entity import DataIngestionConfig, TrainingConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion 
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_training_config(self) -> TrainingConfig:
        config = self.config.training 
        params = self.params 
        create_directories([config.root_dir])
        dataset = os.path.join("artifacts", "data_ingestion", "lung_colon_image_set")
        training_config = TrainingConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            dataset=Path(dataset),
            epochs=params.EPOCHS,
            imgsz=params.IMG_SZ,
            weights=params.WEIGHTS,
            channels=params.CHANNELS,
            lr=params.LEARNING_RATE,
            batch_size=params.BATCH_SIZE
        )
        return training_config