# **Wind Turbine Fault Detection**

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-orange)](https://your-app-url.streamlit.app)  
This project leverages real-time weather data and analytics to monitor and predict faults in wind turbines. It includes a dashboard for visualizing wind speed, temperature, and turbine health parameters.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Example Visualizations](#example-visualizations)
7. [Future Enhancements](#future-enhancements)
8. [Authors](#authors)

---

# Wind Turbine Fault Detection and Real-Time Monitoring Dashboard

## Overview
This repository contains a project focused on fault detection in wind turbines and a real-time weather monitoring dashboard. The project leverages advanced data analytics and visualization tools to monitor wind turbine performance, identify potential faults, and provide real-time weather and power output metrics.

## Features

### 1. Wind Turbine Fault Detection
- **Objective**: Analyze wind turbine data to detect potential faults using machine learning models.
-  **Key Features**:
  - Data preprocessing and feature engineering for handling imbalanced datasets.
  - Implementation of advanced machine learning models for fault classification and anomaly detection.
  - Comprehensive evaluation of model performance using metrics like accuracy, precision, recall, and F1-score.
- **Machine Learning Models Used**:
  - **Balanced Random Forest**: For robust classification while addressing class imbalance.
  - **Easy Ensemble Classifier**: An ensemble approach designed to handle imbalanced data effectively.
  - **LSTM (Long Short-Term Memory)**: For sequence modeling and capturing temporal patterns in turbine data.
- **File**: `Wind_Turbine_Fault_Detection_Project.ipynb`

### 2. Real-Time Weather Monitoring Dashboard
- **Objective**: Real-time visualization of weather data and estimated power output for wind turbines.
- **Features**:
  - Summary statistics of weather data.
  - Interactive visualizations including:
    - Wind speed trends.
    - Temperature trends.
    - Weather description distribution.
    - Estimated power output over time.
  - Location-based data filtering.
- **Technologies Used**: Streamlit, Plotly, Matplotlib, Pandas.
- **File**: `dashboard.py`

## Prerequisites
To run this project, you need the following:
- Python 3.8 or above
- Required Python packages:
  ```bash
  pip install pandas matplotlib plotly streamlit
  ```

## Usage

### Wind Turbine Fault Detection Workflow

1. **Load and Preprocess the Dataset**:
   - Handle class imbalance in the dataset using resampling techniques.

2. **Train Machine Learning Models**:
   - **Balanced Random Forest**: A robust ensemble method to address class imbalance.
   - **Easy Ensemble Classifier**: An effective method for imbalanced datasets using boosted ensembles.
   - **LSTM (Long Short-Term Memory)**: A neural network model for capturing temporal patterns in time-series data.

3. **Evaluate Model Performance**:
   - Use metrics such as accuracy, precision, recall, F1-score, and AUC-ROC to analyze the performance of the models.

4. **Analyze Fault Detection Results**:
   - Visualize insights from the models, including confusion matrices, feature importance, and temporal predictions for wind turbine faults.


### Real-Time Monitoring Dashboard
1. Ensure the `wind_data.csv` file is in the same directory as `dashboard.py`.
2. Run the Streamlit application:
   ```bash
   streamlit run dashboard.py
   ```
3. Interact with the dashboard to explore weather trends, wind power output, and more.

## File Structure
```
|-- Wind_Turbine_Fault_Detection_Project.ipynb  # Jupyter Notebook for fault detection analysis
|-- dashboard.py                                # Streamlit application for real-time monitoring
|-- wind_data.csv                               # Dataset for the dashboard (place in the same directory)
```

## Example Visualizations
### Real-Time Weather Monitoring Dashboard
- **Wind Speed Over Time**
- **Temperature Trends**
- **Power Output Estimation**

## Future Enhancements
- Extend fault detection capabilities using advanced deep learning models.
- Integrate real-time data collection from sensors or APIs.
- Deploy the dashboard on a cloud platform for broader access.


## Authors
- Sharvari Ghatake, Diksha Jadhav
