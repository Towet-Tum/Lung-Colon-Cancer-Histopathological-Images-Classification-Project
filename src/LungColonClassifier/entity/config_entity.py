from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    model_path: Path
    dataset: Path
    epochs: int
    imgsz: tuple
    batch_size: int
    lr: float
    weights: str
    channels: int


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    dataset: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
