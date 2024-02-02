from LungColonClassifier import logger
from LungColonClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from LungColonClassifier.pipeline.stage_02_model_trainer import TrainingPipeline
from LungColonClassifier.pipeline.stage_03_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has started <<<<<<<<<<<<<<< \n\n")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(
        f"\n\n >>>>>>>>> {STAGE_NAME} has completed succefully <<<<<<<<<<<<<<< \n\n ========"
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"
try:
    logger.info(f"\n\n >>>>>>>>> {STAGE_NAME} has started <<<<<<<<<< \n\n")
    train = TrainingPipeline()
    train.main()
    logger.info(
        f">>>>>>>>>>> {STAGE_NAME} has completed successfully <<<<<<<<< \n\n =========="
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f"\n\n >>>>>>>>>> {STAGE_NAME} has started <<<<<<<<<< \n\n")
    evaluator = EvaluationPipeline()
    evaluator.main()
    logger.info(
        f">>>>>>>>> {STAGE_NAME} has completed succefully <<<<<<<<<<< \n\n ==========="
    )
except Exception as e:
    logger.exception(e)
    raise e
