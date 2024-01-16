import os

from fastapi import FastAPI
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

app = FastAPI()


@app.post("/run-pipeline/")
def run_pipeline(island: str, bill_length_mm: float, bill_depth_mm: float, flipper_length_mm: float,
                 body_mass_g: float, sex: str):
    try:
        bootstrap_project(os.getcwd())

        req = f"island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex\n{island},{bill_length_mm},{bill_depth_mm},{flipper_length_mm},{body_mass_g},{sex}"

        extra_params = {
            'api_data_catalog': req
        }

        session = KedroSession.create("penguins", extra_params=extra_params)

        catalog = session.load_context().catalog
        catalog.save("api_data_catalog", req)

        session.run("serving")

        result = catalog.load("api_result")

        print(result)

        return {"result": result}
    except Exception as e:
        return {"error": e}
