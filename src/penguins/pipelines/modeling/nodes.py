import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split


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
):
    y_pred = classificator.predict(X_test)
    score = precision_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a precision score of %.3f on test data.", score)
