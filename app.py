import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import classification_report, roc_curve, auc
from preprocessing import preprocess_data  # Importando a função de pré-processamento

# Carregar o modelo treinado
@st.cache_resource
def load_model():
    with open("models/credit_risk_model.pkl", "rb") as file:
        loaded_model = pickle.load(file)
    return loaded_model

# Função para carregar dados
@st.cache_data
def load_data():
    return pd.read_csv("data/cr_loan2.csv")

# Configuração inicial
st.title("Credit Risk Analysis Application")
st.sidebar.header("Options")

# Seções do aplicativo
option = st.sidebar.selectbox("Choose Section", ["Home - Model Prediction", "Data Analysis"])

if option == "Home - Model Prediction":
    st.header("Welcome to Credit Risk Analysis App")
    st.write("Explore credit risk modeling and business insights interactively.")
    
    st.write("Model Prediction")
    model = load_model()
    
    st.write("Input Data:")
    # Formulário para entrada de dados
    
    #Age
    age = st.number_input("Age", value=None, min_value=18, max_value=100)
    
    #Income
    income = st.number_input("Income", value=50000)
    
    #House situation
    person_home_ownership = st.selectbox(
        "What is your home:",
        ("MORTGAGE", "OTHER", "OWN", "RENT")
    )
    
    #Time Employed
    person_emp_length = st.number_input("Total Time Employed", value=None, min_value=0, max_value=30)
    
    # Caixa de seleção para escolher a intenção do empréstimo
    loan_intent = st.selectbox(
        "Choose the loan intent:",
        ("DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE")
    )
    
    #Classificação do Empréstimo
    loan_grade = st.radio(
    "Loan Grade",
    options=["A", "B", "C", "D", "E"],  # As classificações de empréstimo
    index=0  # Padrão para A
    )
    
    loan_amount = st.number_input("Loan Amount", value=20000)
    
    #Taxa de Juros do Empréstimo
    loan_int_rate = st.slider(
    "Loan Interest Rate (%)",
    min_value=1.0,
    max_value=30.0,
    value=10.0,
    step=0.1
    )

    #Percentage of the loan amount requerid in relationship of the income
    loan_percent_income = loan_amount / income
    
    #Yes in case of past default and Not otherwise
    cb_person_default = st.selectbox(
        "Already default in the past:",
        ("Y", "N")
    )
    
    #Comprimento do Histórico de Crédito da Pessoa
    cb_person_cred_hist_length = st.number_input("Tempo total que tem de histórico de crédito", value=0, min_value=0, max_value=50)

    data_dict = {
    "person_age": age,
    "person_income": income,
    "person_emp_length": person_emp_length,
    "loan_amnt": loan_amount,
    "loan_int_rate": loan_int_rate,
    "loan_percent_income": loan_percent_income,
    "cb_person_cred_hist_length": cb_person_cred_hist_length,
    }
    
    # One-hot encoding for person_home_ownership
    for home_type in ["MORTGAGE", "OTHER", "OWN", "RENT"]:
        data_dict[f"person_home_ownership_{home_type}"] = True if person_home_ownership == home_type else False

    # One-hot encoding for loan_intent
    for intent in ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"]:
        data_dict[f"loan_intent_{intent}"] = True if loan_intent == intent else False

    # One-hot encoding for loan_grade
    for grade in ["A", "B", "C", "D", "E", "F", "G"]:
        data_dict[f"loan_grade_{grade}"] = True if loan_grade == grade else False

    # One-hot encoding for cb_person_default_on_file
    for default in ["N", "Y"]:
        data_dict[f"cb_person_default_on_file_{default}"] = True if cb_person_default == default else False

    # Convert the dictionary to a DataFrame
    data = pd.DataFrame([data_dict])
    
    #data.info()

    # Previsão
    if st.button("Predict"):
        # Pré-processamento  
        user_data = preprocess_data(data)  # Chamando o pré-processamento
        
        prediction = model.predict(user_data)
        
        prediction_prob = model.predict_proba(user_data)
        
        print(prediction)
        print(prediction_prob)
    
        # Resultado da previsão
        if prediction[0] == 1:
            # Não aprovado (default)
            st.markdown(
                '<p style="color: white; background-color: red; padding: 10px; font-size: 18px; font-weight: bold;">Credit Not Approved</p>', 
                unsafe_allow_html=True
            )
        else:
            # Aprovado
            st.markdown(
                '<p style="color: white; background-color: green; padding: 10px; font-size: 18px; font-weight: bold;">Credit Approved</p>', 
                unsafe_allow_html=True
            )
    
elif option == "Data Analysis":
    st.header("Dataset Overview")
    data = load_data()
    st.write("Dataset Sample:")
    st.dataframe(data.head(10))
    st.write("Summary Statistics:")
    st.write(data.describe())

#elif option == "Evaluation":
    
    #st.header("Model Evaluation")
    #data = load_data()
    #model = load_model()
    
    #X = data.drop("loan_status", axis=1)  # Ajuste para o nome real do target
    #y = data["loan_status"]
    #y_pred = model.predict(X)
    
    #report = classification_report(y, y_pred, output_dict=True)
    #st.write("Classification Report:")
    #st.dataframe(pd.DataFrame(report).transpose())
    
    #fpr, tpr, _ = roc_curve(y, model.predict_proba(X)[:, 1])
    #roc_auc = auc(fpr, tpr)
    
    #st.write("ROC Curve:")
    #st.line_chart({"FPR": fpr, "TPR": tpr})
    #st.write(f"AUC: {roc_auc:.2f}")