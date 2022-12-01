from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import util as util
import data_pipeline as data_pipeline
import preprocessing as preprocessing

config_data = util.load_config()
model_data = util.pickle_load(config_data["production_model_path"])


class api_data(BaseModel):
    USMER: int
    MEDICAL_UNIT : int
    PATIENT_TYPE : int
    INTUBED : int
    PNEUMONIA : int
    AGE: int
    AGE_BIN : int
    PREGNANT : int
    DIABETES : int
    COPD : int
    ASTHMA : int
    INMSUPR : int
    HIPERTENSION : int
    OTHER_DISEASE : int
    CARDIOVASCULAR : int
    OBESITY : int
    RENAL_CHRONIC : int
    TOBACCO : int
    CLASIFFICATION_FINAL : int
    ICU : int


app = FastAPI()


@app.get("/")
def home():
    return "Hello, FastAPI up!"


@app.post("/predict/")
def predict(data: api_data):
    # Convert data api to dataframe
    data = pd.DataFrame(data).set_index(0).T.reset_index(drop=True)

    # Convert dtype
    data = pd.concat(
        [
            data[config_data["predictors"][:]].astype(int)
        ],
        axis=1
    )
    print(data)


    # Check range data
    try:
        data_pipeline.check_data(data, config_data, True)
    except AssertionError as ae:
        return {"res": [], "error_msg": str(ae)}

    # Predict data
    y_pred = model_data["model_data"]["model_object"].predict(data)

    y_pred = y_pred[0].tolist()

    return {"res": y_pred, "error_msg": ""}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080)
