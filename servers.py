import pandas as pd
from fastapi import FastAPI, Request, UploadFile,File
import uvicorn
from pydantic import BaseModel
from wirtes_to_file import WiresToFile
from formula_calculation import FormulaCalculation
import os
wires = WiresToFile()
# יצירת מופע של האפליקציה
app = FastAPI()
class Customer(BaseModel):
    age: int
    income: str
    student: str
    credit_rating: str
@app.post("/predict")
async def predict(customer: Customer,use_partial_data: bool):
    calculation = FormulaCalculation(str(use_partial_data).lower())
    statsu_yes, statsu_no, result = calculation.formula_calculation(
        customer.age,customer.income,
        customer.student,customer.credit_rating
    )
    model_results = statsu_yes,statsu_no,result
    wires.wires_to_file([customer.age,customer.income,customer.student,customer.credit_rating],model_results,use_partial_data,use_partial_data)
    return {
        "statistics_yes": statsu_yes,
        "statistics_no": statsu_no,
        "will_buy": result
    }
# @app.post("/predict/file")
# async def predict_file(file: UploadFile = File(...)):
#     all_results = []
#     try:
#         for index,row in df.iterrows():
#             age = calculation.parse_age(row['age'])
#             income = row['income']
#             student = row['student']
#             credit_rating = row['credit_rating']
#             stat_yes, stat_no, results = calculation.formula_calculation(
#                 age, income, student, credit_rating
#             )
#             all_results.append({'row': index,"parameters": {"age": age,
#             "income" : income,'student' : student,'credit_rating': credit_rating,},
#                 'statistics_yes': stat_yes,
#                 'statistice_no': stat_no,
#                 'will_buy': results})
#     except Exception as e:
#         all_results.append({'row': index,'error': str(e)})
#     return {'results':all_results}
# הרצה מקומית של האפליקציה
if __name__ == "__main__":
    uvicorn.run("servers:app", host="127.0.0.1", port=8000,reload=True)
