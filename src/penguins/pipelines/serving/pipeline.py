"""
This is a boilerplate pipeline 'serving'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import save_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=save_data,
            inputs=["api_data_catalog", "classificator","encoders"],
            outputs="new_api_data",
            name="save_data_node",
        )
    ])
