import pandas as pd
import numpy as np
import util as util
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE

def load_dataset(config_data: dict) -> pd.DataFrame:
    # Load every set of data
    x_train = util.pickle_load(config_data["train_set_path"][0])
    y_train = util.pickle_load(config_data["train_set_path"][1])

    x_valid = util.pickle_load(config_data["valid_set_path"][0])
    y_valid = util.pickle_load(config_data["valid_set_path"][1])

    x_test = util.pickle_load(config_data["test_set_path"][0])
    y_test = util.pickle_load(config_data["test_set_path"][1])

    # Concatenate x and y each set
    train_set = pd.concat(
        [x_train, y_train],
        axis = 1
    )
    valid_set = pd.concat(
        [x_valid, y_valid],
        axis = 1
    )
    test_set = pd.concat(
        [x_test, y_test],
        axis = 1
    )

    # Return 3 set of data
    return train_set, valid_set, test_set

def nan_detector(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # handle USMER
    set_data.USMER.replace([97, 98, 99], np.nan, inplace = True)

    # handle SEX
    set_data.SEX.replace([97, 98, 99], np.nan, inplace = True)

    # handle PATIENT_TYPE
    set_data.PATIENT_TYPE.replace([97, 98, 99], np.nan, inplace = True)

    # handle INTUBED
    set_data.INTUBED.replace([97, 98, 99], np.nan, inplace = True)

    # handle PNEUMONIA
    set_data.PNEUMONIA.replace([97, 98, 99], np.nan, inplace = True)

    # handle PREGNANT
    set_data.PREGNANT.replace([97, 98, 99], np.nan, inplace = True)

    # handle DIABETES
    set_data.DIABETES.replace([97, 98, 99], np.nan, inplace = True)

    # handle COPD
    set_data.COPD.replace([97, 98, 99], np.nan, inplace = True)

    # handle ASTHMA
    set_data.ASTHMA.replace([97, 98, 99], np.nan, inplace = True)

    # handle INMSUPR
    set_data.INMSUPR.replace([97, 98, 99], np.nan, inplace = True)

    # handle HIPERTENSION
    set_data.HIPERTENSION.replace([97, 98, 99], np.nan, inplace = True)

    # handle OTHER_DISEASE
    set_data.OTHER_DISEASE.replace([97, 98, 99], np.nan, inplace = True)

    # handle CARDIOVASCULAR
    set_data.CARDIOVASCULAR.replace([97, 98, 99], np.nan, inplace = True)

    # handle OBESITY
    set_data.OBESITY.replace([97, 98, 99], np.nan, inplace = True)

    # handle RENAL_CHRONIC
    set_data.RENAL_CHRONIC.replace([97, 98, 99], np.nan, inplace = True)

    # handle TOBACCO
    set_data.TOBACCO.replace([97, 98, 99], np.nan, inplace = True)

    # handle ICU
    set_data.ICU.replace([97, 98, 99], np.nan, inplace = True)

    return set_data

def rus_fit_resample(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # Create sampling object
    rus = RandomUnderSampler(random_state = 26)

    # Balancing set data
    x_rus, y_rus = rus.fit_resample(
        set_data.drop("DEATH", axis = 1),
        set_data.DEATH
    )

    # Concatenate balanced data
    set_data_rus = pd.concat(
        [x_rus, y_rus],
        axis = 1
    )

    # Return balanced data
    return set_data_rus

def ros_fit_resample(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # Create sampling object
    ros = RandomOverSampler(random_state = 11)

    # Balancing set data
    x_ros, y_ros = ros.fit_resample(
        set_data.drop("DEATH", axis = 1),
        set_data.DEATH
    )

    # Concatenate balanced data
    set_data_ros = pd.concat(
        [x_ros, y_ros],
        axis = 1
    )

    # Return balanced data
    return set_data_ros

def sm_fit_resample(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # Create sampling object
    sm = SMOTE(random_state = 112)

    # Balancing set data
    x_sm, y_sm = sm.fit_resample(
        set_data.drop("DEATH", axis = 1),
        set_data.DEATH
    )

    # Concatenate balanced data
    set_data_sm = pd.concat(
        [x_sm, y_sm],
        axis = 1
    )

    # Return balanced data
    return set_data_sm

def impute_median(dataset: pd.DataFrame) -> pd.DataFrame:
  impute_values = {
    "INTUBED" : int(dataset.INTUBED.median()),
    "PNEUMONIA" : int(dataset.PNEUMONIA.median()),
    "PREGNANT" : int(dataset.PREGNANT.median()),
    "DIABETES" : int(dataset.DIABETES.median()),
    "COPD" : int(dataset.COPD.median()),
    "ASTHMA" : int(dataset.ASTHMA.median()),
    "INMSUPR" : int(dataset.INMSUPR.median()),
    "OTHER_DISEASE" : int(dataset.OTHER_DISEASE.median()),
    "CARDIOVASCULAR" : int(dataset.CARDIOVASCULAR.median()),
    "HIPERTENSION" : int(dataset.HIPERTENSION.median()),
    "OBESITY" : int(dataset.OBESITY.median()),
    "RENAL_CHRONIC" : int(dataset.RENAL_CHRONIC.median()),
    "TOBACCO" : int(dataset.TOBACCO.median()),
    "ICU" : int(dataset.ICU.median()),
  }
  dataset.fillna(value = impute_values, inplace = True)
  return dataset

if __name__ == "__main__":
    # 1. Load configuration file
    config_data = util.load_config()

    # 2. Load dataset
    train_set, valid_set, test_set = load_dataset(config_data)

    # 3. Change date died into death column
    train_set['DEATH'] = np.where(train_set.DATE_DIED == '9999-99-99', 0, 1)
    train_set['DEATH'] = train_set['DEATH'].astype(int)
    train_set.drop(columns=['DATE_DIED'], inplace=True)

    valid_set['DEATH'] = np.where(valid_set.DATE_DIED == '9999-99-99', 0, 1)
    valid_set['DEATH'] = valid_set['DEATH'].astype(int)
    valid_set.drop(columns=['DATE_DIED'], inplace=True)

    test_set['DEATH'] = np.where(test_set.DATE_DIED == '9999-99-99', 0, 1)
    test_set['DEATH'] = test_set['DEATH'].astype(int)
    test_set.drop(columns=['DATE_DIED'], inplace=True)

    # 4. Converting 97..98.99 to NaN
    train_set = nan_detector(train_set)
    valid_set = nan_detector(valid_set)
    test_set = nan_detector(test_set)

    # 5. Handling missing value using median
    impute_median(train_set)
    impute_median(valid_set)
    impute_median(test_set)

    # 6. Remove sex
    train_set.drop(columns=["SEX"], inplace=True)
    valid_set.drop(columns=["SEX"], inplace=True)
    test_set.drop(columns=["SEX"], inplace=True)

    # 7. Replace classification
    train_set.CLASIFFICATION_FINAL.replace([1, 2, 3], 1, inplace = True)
    train_set.CLASIFFICATION_FINAL.replace([4,5,6,7], 2, inplace = True)
    valid_set.CLASIFFICATION_FINAL.replace([1, 2, 3], 1, inplace = True)
    valid_set.CLASIFFICATION_FINAL.replace([4,5,6,7], 2, inplace = True)    
    test_set.CLASIFFICATION_FINAL.replace([1, 2, 3], 1, inplace = True)
    test_set.CLASIFFICATION_FINAL.replace([4,5,6,7], 2, inplace = True)

    # 8. Binning age
    train_set['AGE_BIN'] = pd.qcut(train_set['AGE'],
                           q=[0, .25, .35, .45, .55, .65, .75, .85, 1],
                           labels=False)
    valid_set['AGE_BIN'] = pd.qcut(valid_set['AGE'],
                            q=[0, .25, .35, .45, .55, .65, .75, .85, 1],
                            labels=False)
    test_set['AGE_BIN'] = pd.qcut(valid_set['AGE'],
                           q=[0, .25, .35, .45, .55, .65, .75, .85, 1],
                           labels=False)

    # 9. Undersampling dataset
    train_set_rus = rus_fit_resample(train_set)

    # 10. Oversampling dataset
    train_set_ros = ros_fit_resample(train_set)

    # 11. SMOTE dataset
    train_set_sm = sm_fit_resample(train_set)

    # 12. Dumping dataset
    x_train = {
        "Undersampling" : train_set_rus.drop(columns = "DEATH"),
        "Oversampling" : train_set_ros.drop(columns = "DEATH"),
        "SMOTE" : train_set_sm.drop(columns = "DEATH")
    }

    y_train = {
        "Undersampling" : train_set_rus.DEATH,
        "Oversampling" : train_set_ros.DEATH,
        "SMOTE" : train_set_sm.DEATH
    }

    util.pickle_dump(
        x_train,
        config_data['train_feng_set_path'][0]
    )
    util.pickle_dump(
        y_train,
        config_data['train_feng_set_path'][1]
    )

    util.pickle_dump(
        valid_set.drop(columns = "DEATH"),
        config_data['valid_feng_set_path'][0]
    )
    util.pickle_dump(
        valid_set.DEATH,
        config_data['valid_feng_set_path'][1]
    )

    util.pickle_dump(
        test_set.drop(columns = "DEATH"),
        config_data['test_feng_set_path'][0]
    )
    util.pickle_dump(
        test_set.DEATH,
        config_data['test_feng_set_path'][1]
    )
