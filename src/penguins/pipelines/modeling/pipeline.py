"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.13
"""

from kedro.pipeline import Pipeline,node, pipeline

from .nodes import split_data, train_model,evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=split_data,
                inputs=["model_input_table","params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
        node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="classificator",
                name="train_model_node",
            ),
        node(
                func=evaluate_model,
                inputs=["classificator", "X_test", "y_test"],
                outputs="none",
                name="evaluate_model_node",
            ),
    ])
