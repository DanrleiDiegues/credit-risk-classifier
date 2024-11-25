# preprocessing.py
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):   
    """
    Função para normalizar as colunas do dataset usando StandardScaler.
    
    Parâmetros:
    - data: pd.DataFrame contendo os dados de entrada.

    Retorna:
    - pd.DataFrame com as colunas normalizadas.
    """
    print(data)
    
    # Aplicando o StandardScaler
    
    with open('preprocessing/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    data_slr = scaler.transform(data)
    
    print(pd.DataFrame(data_slr).head())
    
    return data_slr
