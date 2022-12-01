from sklearn.model_selection import train_test_split
from tqdm import tqdm
import pandas as pd
import os
import copy
import util as util

def read_raw_data(config: dict) -> pd.DataFrame:
    # Create variable to store raw dataset
    raw_dataset = pd.DataFrame()

    # Raw dataset dir
    raw_dataset_dir = config["dataset_dir"]

    # Look and load add CSV files
    for i in tqdm(os.listdir(raw_dataset_dir)):
        raw_dataset = pd.concat([pd.read_csv(raw_dataset_dir + i), raw_dataset])
    
    # Return raw dataset
    return raw_dataset

def check_data(input_data, params, api = False):
    input_data = copy.deepcopy(input_data)
    params = copy.deepcopy(params)

    if not api:
        # Check data types
        assert input_data.select_dtypes("object").columns.to_list() == params["object_columns"], "an error occurs in object column(s)."

        assert input_data.select_dtypes("int").columns.to_list() == params["int_columns"], "an error occurs in int column(s)."
    else:
        # In case checking data from api
        int_columns = params["predictors"]

        # Check data types
        # assert input_data.select_dtypes("int").columns.to_list() == \
            # int_columns, "an error occurs in int column(s)."

        assert input_data.USMER.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in USMER range."
        assert input_data.MEDICAL_UNIT.between(params["range_medical_unit"][0], params["range_medical_unit"][1]).sum() == len(input_data), "an error occurs in MEDICAL_UNIT range."
        assert input_data.PATIENT_TYPE.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in PATIENT_TYPE range."
        assert input_data.INTUBED.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in INTUBED range."
        assert input_data.PNEUMONIA.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in PNEUMONIA range."
        assert input_data.AGE_BIN.between(params["range_age_bin"][0], params["range_age_bin"][1]).sum() == len(input_data), "an error occurs in AGE_BIN range."
        assert input_data.PREGNANT.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in PREGNANT range."
        assert input_data.DIABETES.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in DIABETES range."
        assert input_data.COPD.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in COPD range."
        assert input_data.ASTHMA.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in ASTHMA range."
        assert input_data.INMSUPR.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in INMSUPR range."
        assert input_data.HIPERTENSION.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in HIPERTENSION range."
        assert input_data.OTHER_DISEASE.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in OTHER_DISEASE range."
        assert input_data.CARDIOVASCULAR.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in CARDIOVASCULAR range."
        assert input_data.OBESITY.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in OBESITY range."
        assert input_data.RENAL_CHRONIC.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in RENAL_CHRONIC range."
        assert input_data.TOBACCO.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in TOBACCO range."
        assert input_data.CLASIFFICATION_FINAL.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in CLASIFFICATION_FINAL range."
        assert input_data.ICU.between(params["range_boolean"][0], params["range_boolean"][1]).sum() == len(input_data), "an error occurs in ICU range."

if __name__ == "__main__":
    # 1. Load configuration file
    config_data = util.load_config()

    # 2. Read all raw dataset
    raw_dataset = read_raw_data(config_data)

    # 3. Reset index
    raw_dataset.reset_index(
        inplace = True,
        drop = True
    )

    # 4. Save raw dataset
    util.pickle_dump(
        raw_dataset,
        config_data["raw_dataset_path"]
    )

    # 5. Data already cleaned, just dump to cleaned dataset
    util.pickle_dump(
        raw_dataset,
        config_data["cleaned_raw_dataset_path"]
    )

    # 6. Check data definition
    check_data(raw_dataset, config_data)

    # 7. Splitting input output
    x = raw_dataset[config_data["predictors"]].copy()
    y = raw_dataset["DATE_DIED"].copy()

    # 8. Splitting train test
    x_train, x_test, \
    y_train, y_test = train_test_split(
        x, y,
        test_size = 0.3,
        random_state = 42
    )

    # 9. Splitting test valid
    x_valid, x_test, \
    y_valid, y_test = train_test_split(
        x_test, y_test,
        test_size = 0.5,
        random_state = 42
    )

    # 10. Save train, valid and test set
    util.pickle_dump(x_train, config_data["train_set_path"][0])
    util.pickle_dump(y_train, config_data["train_set_path"][1])

    util.pickle_dump(x_valid, config_data["valid_set_path"][0])
    util.pickle_dump(y_valid, config_data["valid_set_path"][1])

    util.pickle_dump(x_test, config_data["test_set_path"][0])
    util.pickle_dump(y_test, config_data["test_set_path"][1])
