# Customer Churn Prediction - End to End ML Project

An End-to-End Machine Learning project to predict Telco Customer Churn.
### Streamlit link (customer_churn_predictor): https://customerchurnprediction-9ufpblcsuwaddmyx8fuvkq.streamlit.app

###  Problem Statement
To predict whether a customer will churn (leave the company) using Telco dataset.

### Tech Stack
- Python, SQL, Machine Learning, Streamlit
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

### Models Used & Compared
I trained and compared 4 classification models on the Telco dataset:

1.  **Logistic Regression**
2.  **Decision Tree Classifier**
3.  **Random Forest Classifier**
4.  **Gradient Boosting Classifier**-Best Performing Model

Final model deployed in Streamlit is **Gradient Boosting Classifier** as it gave the highest accuracy.

| Model | Accuracy |
| Gradient Boosting | ~82% |

### Project Workflow
1.  **SQL:** Data extraction and querying from Telco Database
2.  **Data Cleaning:** Handled null values in TotalCharges, converted Yes/No to 1/0, One-Hot Encoding for categorical features
3.  **EDA:** Analyzed churn rate by Contract, Tenure, MonthlyCharges
4.  **Model Training:** Trained 4 models and compared performance
5.  **Deployment:** Deployed best model using Streamlit (`app.py`)

