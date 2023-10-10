
import logging
from typing import Dict, List, Tuple, Union

import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split

import mlflow
from kedro_mlflow.io.metrics import MlflowMetricDataSet

def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:

    X = data[parameters["features"]]
    y = data["species"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> SVC:
    classificator = SVC()
    classificator.fit(X_train, y_train)
    return classificator


def evaluate_model(
    classificator: SVC, X_test: pd.DataFrame, y_test: pd.Series
) -> Dict[str, Union[float, List[float]]]:
    y_pred = classificator.predict(X_test)
    
    return{
        "Accuracy" : [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}],
        "Recall": [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}],
        "AUC" : [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}],
        "Precision" : [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}],
        "F1": [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}],
        "Time_sec" : [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}],
        "Confusion Matrix" : [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}]

    }
