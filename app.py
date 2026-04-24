from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict


app = FastAPI()
model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_iris(request: PredictRequest) -> PredictResponse:
    prediction = predict(model, request.model_dump())

    return PredictResponse(prediction=prediction)
