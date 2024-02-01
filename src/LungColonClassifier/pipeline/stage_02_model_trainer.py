from LungColonClassifier import logger 
from LungColonClassifier.config.configuration import ConfigurationManager
from LungColonClassifier.components.model_trainer import Training 

STAGE_NAME = "Training Stage"
class TrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        train_config = config.get_training_config()
        train = Training(config=train_config)
        train.train()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has started <<<<<<<<<< ")
        train = TrainingPipeline()
        train.main()
        logger.info(f">>>>>>>>>>> {STAGE_NAME} has completed successfully <<<<<<<<< \n\n ==========")
    except Exception as e:
        logger.exception(e)
        raise e