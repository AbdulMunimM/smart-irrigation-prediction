# ==========================================================
# Smart Irrigation Need Prediction
# Developed by Abdul Munim
# ==========================================================

import streamlit as st
import pandas as pd

from src.model import load_model, predict
from src.evaluation import load_metrics

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Smart Irrigation Need Prediction",
    page_icon="🌱",
    layout="wide",
)

# ----------------------------------------------------------
# Load Resources
# ----------------------------------------------------------

@st.cache_resource
def get_model():
    return load_model()


@st.cache_data
def get_metrics():
    return load_metrics()


model = get_model()
metrics = get_metrics()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

with st.sidebar:

    st.title("🌱 Smart Irrigation")

    st.markdown("---")

    st.subheader("Model Performance")

    st.metric(
        "Best Model",
        metrics["Best Model"],
    )

    st.metric(
        "Accuracy",
        f"{metrics['Accuracy']:.2%}",
    )

    st.metric(
        "Precision",
        f"{metrics['Precision']:.2%}",
    )

    st.metric(
        "Recall",
        f"{metrics['Recall']:.2%}",
    )

    st.metric(
        "F1 Score",
        f"{metrics['F1 Score']:.2%}",
    )

    st.markdown("---")

    st.subheader("Project")

    st.write("**Developer:** Abdul Munim")
    st.write(f"**Model:** {metrics['Best Model']}")
    st.write("**Version:** 1.0")

    st.markdown("---")

    st.info(
        "This application predicts irrigation requirements "
        "using soil, weather and crop information."
    )

# ----------------------------------------------------------
# Main Page
# ----------------------------------------------------------

st.title("🌱 Smart Irrigation Need Prediction")

st.markdown(
    """
Predict irrigation requirements using a trained machine learning model
based on environmental conditions, soil properties and crop information.
"""
)

st.divider()

# ----------------------------------------------------------
# Dropdown Options
# ----------------------------------------------------------

SOIL_TYPES = [
    "Clay",
    "Loamy",
    "Sandy",
    "Silty",
]

CROP_TYPES = [
    "Cotton",
    "Maize",
    "Rice",
    "Soybean",
    "Wheat",
]

GROWTH_STAGES = [
    "Initial",
    "Development",
    "Mid",
    "Late",
]

SEASONS = [
    "Spring",
    "Summer",
    "Autumn",
    "Winter",
]

IRRIGATION_TYPES = [
    "Drip",
    "Flood",
    "Sprinkler",
]

WATER_SOURCES = [
    "Canal",
    "Groundwater",
    "River",
    "Reservoir",
]

MULCHING_OPTIONS = [
    "No",
    "Yes",
]

REGIONS = [
    "Central",
    "East",
    "North",
    "South",
    "West",
]

# ----------------------------------------------------------
# Input Layout
# ----------------------------------------------------------

left_col, right_col = st.columns(2)

# ==========================================================
# LEFT COLUMN
# ==========================================================

with left_col:

    st.subheader("🌤 Environmental Conditions")

    temperature = st.slider(
        "Temperature (°C)",
        0.0,
        50.0,
        25.0,
    )

    humidity = st.slider(
        "Humidity (%)",
        0.0,
        100.0,
        50.0,
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=10.0,
    )

    sunlight = st.slider(
        "Sunlight Hours",
        0.0,
        15.0,
        8.0,
    )

    wind = st.slider(
        "Wind Speed (km/h)",
        0.0,
        50.0,
        10.0,
    )

    st.divider()

    st.subheader("🌱 Soil Information")

    soil_type = st.selectbox(
        "Soil Type",
        SOIL_TYPES,
    )

    soil_ph = st.slider(
        "Soil pH",
        3.0,
        10.0,
        7.0,
    )

    soil_moisture = st.slider(
        "Soil Moisture (%)",
        0.0,
        100.0,
        40.0,
    )

    organic_carbon = st.number_input(
        "Organic Carbon",
        value=1.0,
    )

    electrical = st.number_input(
        "Electrical Conductivity",
        value=1.0,
    )

# ==========================================================
# RIGHT COLUMN
# ==========================================================

with right_col:

    st.subheader("🌾 Crop Information")

    crop_type = st.selectbox(
        "Crop Type",
        CROP_TYPES,
    )

    growth_stage = st.selectbox(
        "Growth Stage",
        GROWTH_STAGES,
    )

    season = st.selectbox(
        "Season",
        SEASONS,
    )

    st.divider()

    st.subheader("💧 Irrigation Information")

    irrigation_type = st.selectbox(
        "Irrigation Type",
        IRRIGATION_TYPES,
    )

    water_source = st.selectbox(
        "Water Source",
        WATER_SOURCES,
    )

    field_area = st.number_input(
        "Field Area (hectare)",
        min_value=0.1,
        value=1.0,
    )

    previous_irrigation = st.number_input(
        "Previous Irrigation (mm)",
        min_value=0.0,
        value=10.0,
    )

    mulching = st.radio(
        "Mulching Used",
        MULCHING_OPTIONS,
        horizontal=True,
    )

    region = st.selectbox(
        "Region",
        REGIONS,
    )
   # ----------------------------------------------------------
# Create Input Data
# ----------------------------------------------------------

input_data = pd.DataFrame({
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
})

# ----------------------------------------------------------
# Prediction Button
# ----------------------------------------------------------

st.divider()

predict_button = st.button(
    "🌱 Predict Irrigation Need",
    use_container_width=True,
)

# ----------------------------------------------------------
# Prediction
# ----------------------------------------------------------

if predict_button:

    prediction, confidence = predict(
        model,
        input_data,
    )

    recommendations = {
        "Low": "✅ No irrigation is required at this time.",
        "Medium": "⚠ Soil moisture should be monitored. Irrigation may be needed soon.",
        "High": "🚨 Immediate irrigation is recommended to prevent crop water stress.",
    }

    st.divider()

    st.subheader("🌿 Prediction Result")

    if prediction == "High":
        st.error("🔴 HIGH IRRIGATION NEED")

    elif prediction == "Medium":
        st.warning("🟡 MEDIUM IRRIGATION NEED")

    else:
        st.success("🟢 LOW IRRIGATION NEED")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Prediction",
            prediction,
        )

    with col2:
        st.metric(
            "Confidence",
            f"{confidence:.2%}",
        )

    st.write("### Confidence")

    st.progress(float(confidence))

    st.write("### Recommendation")

    st.info(
        recommendations[prediction]
    )

    with st.expander("📋 Input Summary"):

        st.dataframe(
            input_data,
            use_container_width=True,
            hide_index=True,
        )
        # ==========================================================
# About Project
# ==========================================================

st.divider()

with st.expander("ℹ About This Project"):

    st.markdown(
        """
### Smart Irrigation Need Prediction

This application predicts irrigation requirements using a machine learning
model trained on soil, weather and crop information.

### Machine Learning Workflow

- Data Collection
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Streamlit Deployment

### Machine Learning Model

- Decision Tree Classifier
- Scikit-learn Pipeline
- StandardScaler
- OneHotEncoder
- ColumnTransformer

### Input Features

#### Environmental
- Temperature
- Humidity
- Rainfall
- Sunlight Hours
- Wind Speed

#### Soil
- Soil Type
- Soil pH
- Soil Moisture
- Organic Carbon
- Electrical Conductivity

#### Crop & Irrigation
- Crop Type
- Growth Stage
- Season
- Irrigation Type
- Water Source
- Field Area
- Previous Irrigation
- Mulching
- Region

### Prediction Output

The model predicts one of three irrigation levels:

- 🟢 Low
- 🟡 Medium
- 🔴 High

This project demonstrates an end-to-end machine learning workflow using
Python, Pandas, Scikit-learn and Streamlit.
"""
    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

footer_left, footer_right = st.columns([4, 1])

with footer_left:

    st.caption(
        "Developed by Abdul Munim | Machine Learning Portfolio Project"
    )

with footer_right:

    st.caption("Version 1.0")