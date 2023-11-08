import logging
from typing import Dict, List, Tuple, Union
 
import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularDataset, TabularPredictor
 
import mlflow
 
def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    train ,test = train_test_split(data,test_size=0.5)    
    return test, test
 
 
def train_model(train: pd.DataFrame, test: pd.DataFrame) -> TabularPredictor:
    mlflow.create_experiment("penguins")
    mlflow.set_experiment("penguins")
    mlflow.autolog()
    classificator = TabularPredictor(label="species")
    classificator.fit(train)
    y_pred = classificator.evaluate(test)
    return classificator
    