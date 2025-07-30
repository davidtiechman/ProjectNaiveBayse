from fastapi import FastAPI
from pydantic import BaseModel
from prediction import Naive_byase

app = FastAPI()
model = Naive_byase()

class InputData(BaseModel):
    age: int
    income: str
    student: str
    credit_rating: str

@app.post("/predict")
def predict(data: InputData):
    prob_yes, prob_no, prediction = model.naive_byase(
        data.age, data.income, data.student, data.credit_rating
    )
    return {
        "probability_yes": prob_yes,
        "probability_no": prob_no,
        "prediction": prediction
    }
