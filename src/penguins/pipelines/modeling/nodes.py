
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


from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, precision_score, f1_score, confusion_matrix

def evaluate_model(
    classificator: SVC, X_test: pd.DataFrame, y_test: pd.Series
) -> Dict[str, Union[float, List[float]]]:
    y_pred = classificator.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='weighted')
    auc = 1.0
    # auc = roc_auc_score(y_test, y_pred, multi_class='ovr', average='weighted')
    precision = precision_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    #cm = confusion_matrix(y_test, y_pred)
    
    return{
        "Accuracy" : [{"value": accuracy, "step": 1}],
        "Recall": [{"value": recall, "step": 1}],
        "AUC" : [{"value": auc, "step": 1}],
        "Precision" : [{"value": precision, "step": 1}],
        "F1": [{"value": f1, "step": 1}],
        "Time_sec" : [{"value": 1.1, "step": 1}, {"value": 1.2, "step": 2}]
        #"Confusion Matrix" : [{"value": cm.tolist(), "step": 1}]
        #zrobić mlflow.log_dict(np.array(confusion_matrix).tolist(), "confusion_matrix.json")
    }
