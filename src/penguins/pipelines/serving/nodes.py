import io
import pickle

import pandas as pd
from autogluon.tabular import TabularPredictor


def save_data(data: pd.DataFrame, classificator: TabularPredictor, encoders: pickle.OBJ) -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(data), sep=",")

    df["island"] = encoders["island"].transform(df["island"])
    df["sex"] = encoders["sex"].transform(df["sex"])

    pred = classificator.predict(df)
    pred = encoders["species"].inverse_transform(pred)[0]

    print(pred)

    return pred
