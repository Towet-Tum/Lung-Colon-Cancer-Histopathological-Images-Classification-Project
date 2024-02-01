from LungColonClassifier import logger
from LungColonClassifier.config.configuration import ConfigurationManager
from LungColonClassifier.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion"
class DataIngestionPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        ingestion_config = config.get_data_ingestion_config()
        ing = DataIngestion(config=ingestion_config)
        ing.download_file()
        ing.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has started <<<<<<<<<<<<<<< ")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has completed succefully <<<<<<<<<<<<<<< \n\n ========")
    except Exception as e:
        logger.exception(e)
        raise e
