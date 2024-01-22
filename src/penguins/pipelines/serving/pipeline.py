"""
This is a boilerplate pipeline 'serving'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline

from penguins.pipelines.serving.nodes import save_data


def create_pipeline() -> Pipeline:
    """Create the kedro serving pipeline."""
    return pipeline([
        node(
            func=save_data,
            inputs=["api_data_catalog", "classificator", "encoders"],
            outputs="api_result",
            name="save_data_node",
        )
    ])
