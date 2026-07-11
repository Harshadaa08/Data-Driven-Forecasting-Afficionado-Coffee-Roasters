# ☕ Data-Driven Forecasting & Demand Prediction for Afficionado Coffee Roasters

## 📌 Project Overview

This project analyzes coffee shop transaction data to identify sales patterns, customer demand, and revenue trends. Using Exploratory Data Analysis (EDA) and Machine Learning, the project provides valuable business insights to improve inventory planning, staff scheduling, and operational efficiency.

---

## 🚀 Live Demo

### 🌐 Streamlit Dashboard

**https://data-driven-forecasting-afficionado-coffee-roasters-fmeg5jpvla.streamlit.app/**

---

## 🎯 Problem Statement

Afficionado Coffee Roasters experiences fluctuations in customer demand throughout the day and across different store locations. Traditional planning methods based on historical intuition often result in inventory waste, inefficient staffing, and inconsistent operational decisions.

This project applies data analytics and machine learning techniques to support data-driven business decision-making.

---

## 🎯 Objectives

- Analyze sales and revenue performance
- Identify peak business hours
- Evaluate store-wise performance
- Analyze product category and product type sales
- Build Machine Learning models for revenue prediction
- Provide business recommendations for operational improvement

---

## 📂 Dataset Features

The dataset contains the following fields:

- Transaction ID
- Transaction Quantity
- Unit Price
- Store ID
- Store Location
- Product ID
- Product Category
- Product Type
- Product Detail
- Transaction Time
- Revenue (Engineered Feature)
- Hour (Engineered Feature)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 📊 Exploratory Data Analysis (EDA)

The project includes:

- Dataset Overview
- Data Cleaning
- Feature Engineering
- Revenue Analysis
- Store-wise Analysis
- Product Category Analysis
- Product Type Analysis
- Product Detail Analysis
- Hourly Sales Analysis
- Store-wise Hourly Heatmap
- Correlation Analysis

---

## 🤖 Machine Learning Models

The following regression models were implemented:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

### Model Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📈 Key Business Insights

- Customer demand varies significantly across stores and business hours.
- Revenue is strongly influenced by transaction quantity.
- Peak business hours require optimized staffing and inventory.
- Certain product categories contribute more to total revenue.
- Machine Learning models improve revenue prediction accuracy.

---

## 💼 Business Recommendations

- Increase inventory for high-demand products.
- Schedule additional staff during peak business hours.
- Improve promotional strategies for low-performing products.
- Optimize inventory allocation based on store performance.
- Collect transaction dates in future datasets to enable advanced time-series forecasting.

---

## 📁 Project Structure

```
Data-Driven-Forecasting-Afficionado-Coffee-Roasters/
│
├── Data_Driven_Forecasting.ipynb
├── app.py
├── requirements.txt
├── README.md
├── Afficionado Coffee Roasters.xlsx
├── Executive_Summary_Afficionado_Coffee_Roasters.docx
├── Research_Paper_Afficionado_Coffee_Roasters.docx
└── images/
```

---

## ▶️ How to Run

### 1. Clone this repository

```bash
git clone https://github.com/Harshadaa08/Data-Driven-Forecasting-Afficionado-Coffee-Roasters.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📌 Dataset Limitation

The provided dataset does not contain transaction dates. Therefore, traditional time-series forecasting methods such as ARIMA, SARIMA, and Prophet were not applied. Revenue prediction was performed using supervised Machine Learning models based on the available features.

---

## 📸 Project Screenshots

You can add dashboard screenshots inside the **images/** folder and display them here.

Example:

```markdown
![Dashboard](images/dashboard.png)
```

---

## 👩‍💻 Author

**Harshada R. Kanse**

**MBA (Business Analytics & Marketing)**

**Unified Mentor Internship**

### 🔗 GitHub

https://github.com/Harshadaa08

### 🔗 LinkedIn

https://www.linkedin.com/in/harshada-r-kanse

---

## ⭐ Support

If you found this project useful, please ⭐ Star this repository and feel free to fork it.

---

## 🙏 Acknowledgements

This project was completed as part of the **Unified Mentor Internship Program**, focusing on Business Analytics, Exploratory Data Analysis (EDA), Machine Learning, and Streamlit Dashboard Development.
