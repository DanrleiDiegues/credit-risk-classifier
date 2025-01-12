import uvicorn ##ASGI
from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Load the model:
with open("./models/credit_risk_model.pkl", "rb") as f:
    model = pickle.load(f)

# 2. Load the scaler:
with open("./preprocessing/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# 3. Create the FastAPI application:
app = FastAPI()

from pydantic import BaseModel

# 4. Define the Schema for the Entry data:
class LoanData(BaseModel):
    person_age: int
    person_income: int
    person_emp_length: float
    loan_amnt: int
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: int
    person_home_ownership_MORTGAGE: int
    person_home_ownership_OTHER: int
    person_home_ownership_OWN: int
    person_home_ownership_RENT: int
    loan_intent_DEBTCONSOLIDATION: int
    loan_intent_EDUCATION: int
    loan_intent_HOMEIMPROVEMENT: int
    loan_intent_MEDICAL: int
    loan_intent_PERSONAL: int
    loan_intent_VENTURE: int
    loan_grade_A: int
    loan_grade_B: int
    loan_grade_C: int
    loan_grade_D: int
    loan_grade_E: int
    loan_grade_F: int
    loan_grade_G: int
    cb_person_default_on_file_N: int
    cb_person_default_on_file_Y: int
    
# 5. Create an endpoint to recieve the data, to make the prediction and return the result. Opens automatically on http://127.0.0.1:8000
@app.post("/predict") 
async def predict(data: LoanData):
    # Converter os dados para um DataFrame pandas
    data_dict = data.dict()
    df = pd.DataFrame([data_dict])
    
    # Pré-processar os dados com o StandardScaler carregado
    X_slr = scaler.transform(df)
    
    # Fazer a predição
    prediction = model.predict(X_slr)[0]
    
    # Retornar o resultado como um dicionário
    result = {
        "prediction": int(prediction)
    }
    
    return result

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)
# uvicorn main:app --reload

'''
0.0.0.0: Torna sua aplicação acessível a partir de qualquer dispositivo na sua rede, incluindo outros computadores. Isso é útil para testes em diferentes dispositivos ou para implantar em um servidor.
127.0.0.1: Torna sua aplicação acessível apenas a partir do seu próprio computador (localhost). Isso é útil para desenvolvimento e testes locais.
'''