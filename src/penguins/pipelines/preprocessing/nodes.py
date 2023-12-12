import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder



def preprocess_penguins(
        penguins: pd.DataFrame
) -> Tuple[pd.DataFrame, LabelEncoder,LabelEncoder,LabelEncoder]:
    #to encode
    island_encoder  = LabelEncoder()
    penguins["island"] = island_encoder.fit_transform(penguins["island"])
    sex_encoder = LabelEncoder()
    penguins["sex"] = sex_encoder.fit_transform(penguins["sex"])
    species_encoder  = LabelEncoder()
    penguins["species"] = species_encoder.fit_transform(penguins["species"])
    return penguins, island_encoder, sex_encoder, species_encoder


def create_model_input_table(
     preprocess_penguins: pd.DataFrame
) -> pd.DataFrame:
    model_input_table = preprocess_penguins.dropna()
    return model_input_table
