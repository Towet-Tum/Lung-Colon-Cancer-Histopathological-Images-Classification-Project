from LungColonClassifier import logger
from LungColonClassifier.config.configuration import ConfigurationManager
from LungColonClassifier.components.model_evaluator import Evaluation

STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n >>>>>>>>>> {STAGE_NAME} has started <<<<<<<<<< \n\n")
        evaluator = EvaluationPipeline()
        evaluator.main()
        logger.info(
            f">>>>>>>>> {STAGE_NAME} has completed succefully <<<<<<<<<<< \n\n  ============="
        )
    except Exception as e:
        logger.exception(e)
        raise e
