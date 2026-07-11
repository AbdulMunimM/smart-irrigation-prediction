# ==========================================================
# Smart Irrigation Need Prediction
# Developed by Abdul Munim
# ==========================================================

import streamlit as st
import pandas as pd

from src.model import load_model, predict
from src.evaluation import load_metrics
from src.config import (
    APP_TITLE,
    APP_DESCRIPTION,
    AUTHOR,
    MODEL_NAME,
    VERSION,
    df,
)

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Smart Irrigation Prediction",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# Load Resources
# ----------------------------------------------------------

@st.cache_resource
def get_model():
    return load_model()


@st.cache_data
def get_dataset():
    return df.copy()


model = get_model()
metrics = load_metrics()
dataset = get_dataset()

# ----------------------------------------------------------
# Dropdown Values
# ----------------------------------------------------------

soil_types = sorted(dataset["Soil_Type"].unique())
crop_types = sorted(dataset["Crop_Type"].unique())
growth_stages = sorted(dataset["Crop_Growth_Stage"].unique())
seasons = sorted(dataset["Season"].unique())
irrigation_types = sorted(dataset["Irrigation_Type"].unique())
water_sources = sorted(dataset["Water_Source"].unique())
mulching_options = sorted(dataset["Mulching_Used"].unique())
regions = sorted(dataset["Region"].unique())

# ----------------------------------------------------------
# Recommendation Dictionary
# ----------------------------------------------------------

recommendations = {
    "Low": """
✅ **Low Irrigation Need**

Current environmental and soil conditions indicate that irrigation is **not required**.

Continue monitoring weather and soil moisture.
""",

    "Medium": """
⚠ **Medium Irrigation Need**

The crop may require irrigation soon.

Monitor soil moisture closely and irrigate if dry conditions continue.
""",

    "High": """
🚨 **High Irrigation Need**

Immediate irrigation is recommended to prevent crop water stress.
"""
}

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

with st.sidebar:

    st.title("🌱 Smart Irrigation")

    st.markdown("---")

    st.subheader("Model Information")

    st.write(f"**Model**")
    st.info(metrics["Best Model"])

    st.write(f"**Accuracy**")
    st.success(f"{metrics['Accuracy']:.2%}")

    st.write(f"**Precision**")
    st.success(f"{metrics['Precision']:.2%}")

    st.write(f"**Recall**")
    st.success(f"{metrics['Recall']:.2%}")

    st.write(f"**F1 Score**")
    st.success(f"{metrics['F1 Score']:.2%}")

    st.markdown("---")

    st.subheader("Project")

    st.write(APP_TITLE)

    st.write(f"**Developer:** {AUTHOR}")

    st.write(f"**Version:** {VERSION}")

    st.markdown("---")

    st.caption(
        "Built using Python, Scikit-Learn and Streamlit."
    )

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------

st.title(APP_TITLE)

st.markdown(APP_DESCRIPTION)

st.divider()

# ----------------------------------------------------------
# Main Layout
# ----------------------------------------------------------

left_col, right_col = st.columns(2)
# ==========================================================
# LEFT COLUMN
# Environmental + Soil Information
# ==========================================================

with left_col:

    st.subheader("🌤 Environmental Conditions")

    temperature = st.slider(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=25.0,
        step=0.1,
    )

    humidity = st.slider(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=0.1,
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=10.0,
        step=1.0,
    )

    sunlight = st.slider(
        "Sunlight Hours",
        min_value=0.0,
        max_value=15.0,
        value=8.0,
        step=0.5,
    )

    wind = st.slider(
        "Wind Speed (km/h)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=0.5,
    )

    st.divider()

    st.subheader("🌱 Soil Information")

    soil_type = st.selectbox(
        "Soil Type",
        soil_types,
    )

    soil_ph = st.slider(
        "Soil pH",
        min_value=3.0,
        max_value=10.0,
        value=7.0,
        step=0.1,
    )

    soil_moisture = st.slider(
        "Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=0.5,
    )

    organic_carbon = st.number_input(
        "Organic Carbon",
        min_value=0.0,
        value=1.0,
        step=0.1,
    )

    electrical = st.number_input(
        "Electrical Conductivity",
        min_value=0.0,
        value=1.0,
        step=0.1,
    )

# ==========================================================
# RIGHT COLUMN
# Crop + Irrigation Information
# ==========================================================

with right_col:

    st.subheader("🌾 Crop Information")

    crop_type = st.selectbox(
        "Crop Type",
        crop_types,
    )

    growth_stage = st.selectbox(
        "Growth Stage",
        growth_stages,
    )

    season = st.selectbox(
        "Season",
        seasons,
    )

    st.divider()

    st.subheader("💧 Irrigation Information")

    irrigation_type = st.selectbox(
        "Irrigation Type",
        irrigation_types,
    )

    water_source = st.selectbox(
        "Water Source",
        water_sources,
    )

    field_area = st.number_input(
        "Field Area (hectare)",
        min_value=0.1,
        value=1.0,
        step=0.1,
    )

    previous_irrigation = st.number_input(
        "Previous Irrigation (mm)",
        min_value=0.0,
        value=10.0,
        step=1.0,
    )

    mulching = st.radio(
        "Mulching Used",
        mulching_options,
        horizontal=True,
    )

    region = st.selectbox(
        "Region",
        regions,
    )

# ==========================================================
# CREATE INPUT DATAFRAME
# ==========================================================

input_data = pd.DataFrame(
    {
        "Soil_Type": [soil_type],
        "Soil_pH": [soil_ph],
        "Soil_Moisture": [soil_moisture],
        "Organic_Carbon": [organic_carbon],
        "Electrical_Conductivity": [electrical],
        "Temperature_C": [temperature],
        "Humidity": [humidity],
        "Rainfall_mm": [rainfall],
        "Sunlight_Hours": [sunlight],
        "Wind_Speed_kmh": [wind],
        "Crop_Type": [crop_type],
        "Crop_Growth_Stage": [growth_stage],
        "Season": [season],
        "Irrigation_Type": [irrigation_type],
        "Water_Source": [water_source],
        "Field_Area_hectare": [field_area],
        "Mulching_Used": [mulching],
        "Previous_Irrigation_mm": [previous_irrigation],
        "Region": [region],
    }
)

st.divider()

predict_button = st.button(
    "🌱 Predict Irrigation Need",
    use_container_width=True,
)
# ==========================================================
# PREDICTION
# ==========================================================

if predict_button:

    prediction, confidence = predict(model, input_data)

    st.divider()

    st.subheader("🌿 Prediction Result")

    # -----------------------------------------
    # Color-coded Prediction
    # -----------------------------------------

    if prediction == "High":
        st.error("🔴 HIGH IRRIGATION NEED")

    elif prediction == "Medium":
        st.warning("🟡 MEDIUM IRRIGATION NEED")

    else:
        st.success("🟢 LOW IRRIGATION NEED")

    # -----------------------------------------
    # Metrics
    # -----------------------------------------

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.metric(
            label="Prediction",
            value=prediction,
        )

    with metric_col2:
        st.metric(
            label="Model Confidence",
            value=f"{confidence:.2%}",
        )

    # -----------------------------------------
    # Confidence Progress Bar
    # -----------------------------------------

    st.write("### Confidence Score")

    st.progress(float(confidence))

    st.caption(
        f"The model is **{confidence:.2%}** confident in this prediction."
    )

    # -----------------------------------------
    # Recommendation
    # -----------------------------------------

    st.write("### Recommendation")

    st.info(recommendations[prediction])

    # -----------------------------------------
    # Input Summary
    # -----------------------------------------

    with st.expander("📋 View Input Summary"):

        st.dataframe(
            input_data,
            use_container_width=True,
            hide_index=True,
        )

# ==========================================================
# ABOUT PROJECT
# ==========================================================

st.divider()

with st.expander("ℹ About This Project"):

    st.markdown(
        """
### Smart Irrigation Need Prediction

This application predicts irrigation requirements using a
machine learning model trained on environmental, soil and crop
conditions.

### Machine Learning Pipeline

- Decision Tree Classifier
- Scikit-Learn Pipeline
- StandardScaler
- OneHotEncoder
- ColumnTransformer

### Features Used

- Soil Characteristics
- Weather Conditions
- Crop Information
- Irrigation History

### Output

The model predicts one of the following irrigation levels:

- 🟢 Low
- 🟡 Medium
- 🔴 High

This project demonstrates an end-to-end machine learning
workflow including:

- Data Understanding
- Exploratory Data Analysis
- Data Preprocessing
- Model Training
- Model Evaluation
- Streamlit Deployment
"""
    )

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

footer_col1, footer_col2 = st.columns([4, 1])

with footer_col1:

    st.caption(
        "Developed by Abdul Munim | Machine Learning Portfolio Project"
    )

with footer_col2:

    st.caption("Version 1.0")
