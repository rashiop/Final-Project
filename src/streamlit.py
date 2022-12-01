import streamlit as st
import requests
from PIL import Image

# Load and set images in the first place
header_images = Image.open('assets/header_images.jpeg')
st.image(header_images)

# Add some information about the service
st.title("COVID Death Prediction")
st.subheader("Just enter variabel below then click Predict button")

# Create form of input
with st.form("covid_data_form"):

    # Create box for number input
    USMER = st.number_input(
        label = "1.\tEnter USMER Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)",
    )

    MEDICAL_UNIT = st.number_input(
        label = "2.\tEnter MEDICAL_UNIT Value:",
        min_value = 1,
        max_value = 13,
        help = "Value range from 1 to 13"
    )

    ICU = st.number_input(
        label = "3.\tEnter ICU Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    PATIENT_TYPE = st.number_input(
        label = "4.\tEnter PATIENT_TYPE Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (hospitalized) to 2 (no)"
    )

    INTUBED = st.number_input(
        label = "5.\tEnter INTUBED Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    PNEUMONIA = st.number_input(
        label = "6.\tEnter PNEUMONIA Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    AGE_BIN = st.number_input(
        label = "7.\tEnter AGE_BIN Value:",
        min_value = 0,
        max_value = 7,
        help = "Value range from 0 to 7"
    )

    PREGNANT = st.number_input(
        label = "8.\tEnter PREGNANT Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    DIABETES = st.number_input(
        label = "9.\tEnter DIABETES Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    COPD = st.number_input(
        label = "10.\tEnter COPD Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    ASTHMA = st.number_input(
        label = "11.\tEnter ASTHMA Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    INMSUPR = st.number_input(
        label = "12.\tEnter INMSUPR Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    HIPERTENSION = st.number_input(
        label = "13.\tEnter HIPERTENSION Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    OTHER_DISEASE = st.number_input(
        label = "14.\tEnter OTHER_DISEASE Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    CARDIOVASCULAR = st.number_input(
        label = "15.\tEnter CARDIOVASCULAR Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )
    OBESITY = st.number_input(
        label = "16.\tEnter OBESITY Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )
    RENAL_CHRONIC = st.number_input(
        label = "17.\tEnter RENAL_CHRONIC Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )
    TOBACCO = st.number_input(
        label = "18.\tEnter TOBACCO Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (yes) to 2 (no)"
    )

    CLASIFFICATION_FINAL = st.number_input(
        label = "19.\tEnter CLASIFFICATION_FINAL Value:",
        min_value = 1,
        max_value = 2,
        help = "Value range from 1 (covid) to 2 (not covid)"
    )

    AGE = st.number_input(
        label="20.\tEnter AGE Value:",
        min_value=1,
        max_value=2,
        help="Value range from 0 to 121"
    )
    
    # Create button to submit the form
    submitted = st.form_submit_button("Predict")

    # Condition when form submitted
    if submitted:
        # Create dict of all data in the form
        raw_data = {
            "USMER": USMER,
            "MEDICAL_UNIT": MEDICAL_UNIT,
            "PATIENT_TYPE": PATIENT_TYPE,
            "INTUBED":INTUBED,
            "PNEUMONIA":PNEUMONIA,
            "AGE": AGE,
            "AGE_BIN":AGE_BIN,
            "PREGNANT":PREGNANT,
            "DIABETES":DIABETES,
            "COPD":COPD,
            "ASTHMA":ASTHMA,
            "INMSUPR":INMSUPR,
            "HIPERTENSION":HIPERTENSION,
            "OTHER_DISEASE":OTHER_DISEASE,
            "CARDIOVASCULAR":CARDIOVASCULAR,
            "OBESITY":OBESITY,
            "RENAL_CHRONIC":RENAL_CHRONIC,
            "TOBACCO":TOBACCO,
            "CLASIFFICATION_FINAL":CLASIFFICATION_FINAL,
            "ICU":ICU
        }

        # Create loading animation while predicting
        with st.spinner("Sending data to prediction server ..."):
            # res = requests.post(
            #     "http://0.0.0.0:8080/predict/", json=raw_data).json()
            res = requests.post("http://api:8080/predict",
                                json=raw_data).json()

        # Parse the prediction result
        if res["error_msg"] != "":
            st.error("Error Occurs While Predicting: {}".format(res["error_msg"]))
        else:
            if res["res"] == 0:
                st.warning("Predicted Covid Death: Selamat - 0")
            else:
                st.success("Predicted Covid Death: Meninggal - 1")
