import logging
from typing import Dict, List, Tuple, Union
 
import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularDataset, TabularPredictor
 
import mlflow
 
def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    train ,test = train_test_split(data,test_size=0.2)    
    return test, test
 
 
def train_model(train: pd.DataFrame, test: pd.DataFrame) -> TabularPredictor:
    mlflow.set_experiment("penguins")
    mlflow.autolog()
    classificator = TabularPredictor(label="species",log_to_file=False,problem_type="multiclass",eval_metric="accuracy")
    classificator.fit(train, time_limit=120)
    y_pred = classificator.evaluate(test)
    return classificator
    