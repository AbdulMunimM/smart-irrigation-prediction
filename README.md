# 🌱 Smart Irrigation Need Prediction

A machine learning web application that predicts irrigation requirements using environmental conditions, soil properties, crop information, and irrigation history.

Built with **Python**, **Scikit-Learn**, and **Streamlit**.

---

## Project Overview

Efficient irrigation management is essential for improving crop yield while conserving water resources.

This project uses a supervised machine learning model to predict irrigation requirements based on multiple agricultural factors.

The application allows users to enter field conditions through a simple web interface and receive an irrigation recommendation instantly.

---

## Features

- Predicts irrigation requirement (Low, Medium, High)
- Interactive Streamlit web application
- Decision Tree Classification model
- Complete machine learning pipeline
- Model performance metrics
- Confidence score for predictions
- Clean and responsive user interface

---

## Dataset

The dataset contains agricultural information including:

### Environmental Features

- Temperature
- Humidity
- Rainfall
- Sunlight Hours
- Wind Speed

### Soil Features

- Soil Type
- Soil pH
- Soil Moisture
- Organic Carbon
- Electrical Conductivity

### Crop Features

- Crop Type
- Crop Growth Stage
- Season

### Irrigation Features

- Irrigation Type
- Water Source
- Field Area
- Previous Irrigation
- Mulching
- Region

### Target Variable

- Irrigation Need

---

## Machine Learning Workflow

1. Data Loading
2. Data Exploration
3. Data Preprocessing
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Selection
8. Model Deployment using Streamlit

---

## Models Evaluated

The following machine learning algorithms were compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The **Decision Tree Classifier** achieved the best overall performance and was selected for deployment.

---

## Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 99.60% |
| Precision | 99.60% |
| Recall | 99.60% |
| F1 Score | 99.60% |

---

## Project Structure

```text
smart-irrigation-prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/
│       └── irrigation_prediction.csv
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   └── irrigation_prediction.ipynb
│
├── reports/
│   └── metrics.json
│
└── src/
    ├── model.py
    └── evaluation.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AbdulMunimM/smart-irrigation-prediction.git
```

Move into the project directory:

```bash
cd smart-irrigation-prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit
- Matplotlib

---

## Future Improvements

- Support regression-based irrigation amount prediction
- Weather API integration
- Real-time sensor integration
- Explainable AI using SHAP
- Hyperparameter tuning
- Docker deployment
- Cloud deployment

---

## Author

**Abdul Munim**

Machine Learning & AI Developer

GitHub:
https://github.com/AbdulMunimM

---

## License

This project is intended for educational and portfolio purposes.