from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


MODEL_PATH = Path("models/iris_model.joblib")


def load_data():
    return load_iris()


def train_model():
    iris = load_data()

    model = LogisticRegression(max_iter=200)
    model.fit(iris.data, iris.target)

    return model


def save_model(model, path: Path = MODEL_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


if __name__ == "__main__":
    trained_model = train_model()
    save_model(trained_model)
