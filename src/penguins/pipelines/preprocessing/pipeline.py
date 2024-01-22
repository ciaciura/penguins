"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.13
"""

from kedro.pipeline import Pipeline, node, pipeline

from penguins.pipelines.preprocessing.nodes import preprocess_penguins, create_model_input_table


def create_pipeline() -> Pipeline:
    """Create the kedro preprocessing pipeline."""
    return pipeline([
        node(
            func=preprocess_penguins,
            inputs="penguins",
            outputs=["preprocessed_penguins", "encoders"],
            name="preprocess_penguins_node",
        ),
        node(
            func=create_model_input_table,
            inputs="preprocessed_penguins",
            outputs="model_input_table",
            name="create_model_input_table_node",
        )
    ])
