from fastapi import FastAPI
from pydantic import BaseModel

from .model import ReadabilityEvaluationModel


class Excerpt(BaseModel):
    text: str


app = FastAPI()
model = ReadabilityEvaluationModel()


@app.on_event("startup")
async def load_model():
    model.load_model()


@app.post("/")
async def evaluate_readability(excerpt: Excerpt) -> dict:
    text = excerpt.text
    prediction = model.predict(text)
    return {"readability": prediction}
