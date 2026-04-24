from pathlib import Path

import joblib
from sklearn.datasets import load_iris


MODEL_PATH = Path("models/iris_model.joblib")


def load_model(path: Path = MODEL_PATH):
    return joblib.load(path)


def predict(model, features: dict[str, float]) -> str:
    iris = load_iris()

    input_data = [
        [
            features["sepal_length"],
            features["sepal_width"],
            features["petal_length"],
            features["petal_width"],
        ]
    ]

    prediction_id = model.predict(input_data)[0]

    return iris.target_names[prediction_id]
