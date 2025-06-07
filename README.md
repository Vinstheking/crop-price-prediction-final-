# End-to-End Crop Price Prediction Model

This project is an end-to-end pipeline designed to predict crop prices accurately. It leverages multiple machine learning models, evaluates their performance, and selects the best-performing model for final predictions. The pipeline is modular and scalable, making it adaptable for real-world agricultural applications.

## Features

* Supports multiple machine learning algorithms.
* Automatically selects the best model based on evaluation metrics.
* Provides exploratory data analysis (EDA) and visualization of data.
* Modular pipeline for data preprocessing, model training, and evaluation.

## Table of Contents

1. [Installation](#installation)
2. [Dataset](#dataset)
3. [Workflow](#workflow)
4. [Model Selection](#model-selection)
5. [Usage](#usage)
6. [Results](#results)
7. [Future Improvements](#future-improvements)

## Installation

### Prerequisites

Ensure the following are installed:

* Python 3.7+
* pip
* Libraries listed in `requirements.txt`

### Steps

1. Clone the repository:

2. Install dependencies:



## Dataset

The dataset should include features like:

* **Crop type**: Type of crop being analyzed.
* **District**: Geographical area of interest.
* **Date and Month**: Temporal data for seasonal trends.
* **Weather data**: Temperature, rainfall, humidity, etc.
* **Market data**: Historical prices, demand, and supply.

### Example Dataset

| Crop  | District  | Date       | Month | Rainfall (mm) | Price (₹/kg) |
| ----- | --------- | ---------- | ----- | ------------- | ------------ |
| Wheat | Bangalore | 2025-06-01 | June  | 20.5          | 25           |
| Rice  | Mysore    | 2025-06-01 | June  | 30.2          | 35           |

## Workflow

1. **Data Collection**: Import historical crop price and auxiliary data.
2. **Data Preprocessing**:

   * Handle missing values.
   * Encode categorical variables.
   * Normalize numerical data.
3. **Exploratory Data Analysis (EDA)**: Generate insights and visualize trends.
4. **Feature Engineering**: Create relevant features for better model performance.
5. **Model Training**: Train multiple machine learning models including:

   * Linear Regression
   * Random Forest
   * Gradient Boosting Machines (e.g., XGBoost, LightGBM)
   * Neural Networks
6. **Model Evaluation**:

   * Evaluate models using metrics like RMSE, R2, and MAE.
   * Automatically select the best model.
7. **Prediction**: Use the selected model to predict crop prices for unseen data.

## Model Selection

The pipeline evaluates all models based on key metrics and selects the best model. For example:

| Model             | RMSE | R2 Score |
| ----------------- | ---- | -------- |
| Linear Regression | 10.5 | 0.75     |
| Random Forest     | 8.2  | 0.85     |
| XGBoost           | 7.5  | 0.88     |
| Neural Network    | 9.0  | 0.82     |

Based on this example, XGBoost would be chosen as the final model.

## Usage

1. **Prepare Dataset**: Ensure the dataset is in `.csv` format and placed in the `data/` directory.
2. **Run the Pipeline**:

   ```bash
   python main.py
   ```
3. **View Results**: Results will be saved in the `outputs/` folder.

## Results

The pipeline outputs:

* **Plots**: EDA visualizations.
* **Metrics**: RMSE, R2, and MAE scores for all models.
* **Best Model**: Name of the selected model.
* **Predictions**: CSV file with predicted prices for new data.

## Future Improvements

* Incorporate time-series forecasting models like ARIMA or LSTMs.
* Add a web interface for user interaction.
* Integrate real-time data fetching from APIs.
* Enhance feature engineering with domain-specific insights.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.


