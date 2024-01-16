from src.penguins.pipelines.serving.pipeline import create_pipeline
from fastapi import FastAPI, HTTPException
from kedro.io import DataCatalog, MemoryDataset

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.post("/run-pipeline/")
def run_pipeline(island: str, bill_length_mm: float, bill_depth_mm: float, flipper_length_mm: float,
                 body_mass_g: float, sex: str):
    # Create the pipeline
    pipeline = create_pipeline()

    # Set up the DataCatalog with the input value from the request
    io = DataCatalog({"api_data_catalog": MemoryDataset()})
    io.save("api_data_catalog",
            f"island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex\n{island},{bill_length_mm},{bill_depth_mm},{flipper_length_mm},{body_mass_g},{sex}")
    # Run the pipeline and get the result
    result = SequentialRunner().run(pipeline, catalog=io).to_dict(orient="records")["predictions"]
    return {"result": result}
