import pandas as pd
from autogluon.tabular import TabularPredictor


def save_data(data: pd.DataFrame, classificator: TabularPredictor) -> pd.DataFrame:
    return classificator.predict(data)
