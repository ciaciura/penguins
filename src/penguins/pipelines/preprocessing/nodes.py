"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.13
"""
import pandas as pd

def preprocess_penguins(
        penguins: pd.DataFrame
) -> pd.DataFrame:
    
    return penguins

def create_model_input_table(
     preprocess_penguins: pd.DataFrame
) -> pd.DataFrame:
    model_input_table = preprocess_penguins.dropna()
    return model_input_table
