from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Answer(BaseModel):
    country: str
    answer: str

@app.get("/country/{name}")
def get_country(name: str):
    return get_country_data(name)

@app.post("/answer")
def submit_answer(data: Answer):
    correct = data.answer.lower() == get_country_data(data.country)["capital"].lower()
    return {
        "correct": correct,
        "capital": get_country_data(data.country)["capital"]
    }