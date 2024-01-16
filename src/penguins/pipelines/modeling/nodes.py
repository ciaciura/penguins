from typing import Dict, Tuple

import mlflow
import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    train ,test = train_test_split(data,test_size=0.2)    
    return test, test
 
 
def train_model(train: pd.DataFrame, test: pd.DataFrame) -> TabularPredictor:
    mlflow.set_experiment("penguins")
    classificator = TabularPredictor(label="species",log_to_file=False,problem_type="multiclass",eval_metric="accuracy")
    classificator.fit(train, time_limit=120)
    y_pred = classificator.evaluate(test)
    for key,value in classificator.fit_summary()["model_performance"].items():
        mlflow.log_metric(f"{key}_accuracy",value)
    return classificator
    