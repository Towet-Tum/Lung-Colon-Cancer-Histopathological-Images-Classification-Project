import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from LungColonClassifier.utils.common import load_data, process_data, save_json
from LungColonClassifier.entity.config_entity import EvaluationConfig


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        df = load_data(self.config.dataset)
        _, _, test_gen = process_data(df)
        self.model = self.load_model(self.config.path_of_model)
        ts_length = len(test_gen)
        test_batch_size = min(32, ts_length)
        test_steps = ts_length // test_batch_size
        self.score = self.model.evaluate(test_gen, steps=test_steps, verbose=1)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                mlflow.keras.log_model(
                    self.model, "model", registered_model_name="XceptionModel"
                )
            else:
                mlflow.keras.log_model(self.model, "model")
