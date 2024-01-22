"""Nodes for the preprocessing pipeline."""
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_penguins(
        penguins: pd.DataFrame
) -> pd.DataFrame:
    """Preprocess the penguins data by encoding categorical columns."""
    # to encode
    island_encoder = LabelEncoder()
    penguins["island"] = island_encoder.fit_transform(penguins["island"])
    sex_encoder = LabelEncoder()
    penguins["sex"] = sex_encoder.fit_transform(penguins["sex"])
    species_encoder = LabelEncoder()
    penguins["species"] = species_encoder.fit_transform(penguins["species"])

    # save label encoder to dictionary key = column name, value = encoder
    encoders = {
        "island": island_encoder,
        "sex": sex_encoder,
        "species": species_encoder
    }

    return penguins, encoders


def create_model_input_table(
        preprocessed_penguins: pd.DataFrame
) -> pd.DataFrame:
    """Create a model input table by dropping rows with missing values."""
    model_input_table = preprocessed_penguins.dropna()
    return model_input_table
