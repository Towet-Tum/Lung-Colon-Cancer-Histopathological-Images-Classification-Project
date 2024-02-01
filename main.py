from LungColonClassifier import logger 
from LungColonClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has started <<<<<<<<<<<<<<< ")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has completed succefully <<<<<<<<<<<<<<< \n\n ========")
except Exception as e:
    logger.exception(e)
    raise e
