import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

def preprocess_penguins(
        penguins: pd.DataFrame
) -> pd.DataFrame:
    #to encode
    penguins["island"]
    penguins["sex"]
    penguins["species"]
    return penguins

def create_model_input_table(
     preprocess_penguins: pd.DataFrame
) -> pd.DataFrame:
    model_input_table = preprocess_penguins.dropna()
    return model_input_table
