from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kedro.io import DataCatalog, MemoryDataset
from kedro.runner import SequentialRunner
from src.penguins.pipelines.serving.pipeline import create_pipeline


class PipelineInput(BaseModel):
    input_value: int


# Create the pipeline
pipeline = create_pipeline()

# Set up the DataCatalog with the input value from the request
io = DataCatalog({"api_data_catalog": MemoryDataset()})
io.save("api_data_catalog", "Adelie,Torgersen,39.1,18.7,181,3750,MALE")
# Run the pipeline and get the result
result = SequentialRunner().run(pipeline, catalog=io)

print(result)
# return {"result": result}
