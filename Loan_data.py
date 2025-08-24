import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 1. Load the dataset
print("Loading the dataset...")
df = pd.read_csv('csv_datas/Loan.csv')
print("Dataset loaded successfully.")

# 2. Handle Missing Values
print("\nStep 1: Handling Missing Values...")
# Numerical columns
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)

# Categorical columns
for col in ['Gender', 'Married', 'Dependents', 'Self_Employed', 'Credit_History']:
    df[col].fillna(df[col].mode()[0], inplace=True)
print("Missing values handled.")

# 3. Correct Data Types and Values
print("\nStep 2: Correcting Data Types...")
# Clean the 'Dependents' column and convert to numeric
df['Dependents'] = df['Dependents'].replace('3+', '3')
df['Dependents'] = pd.to_numeric(df['Dependents'])

# Convert 'Credit_History' to integer
df['Credit_History'] = df['Credit_History'].astype(int)
print("Data types corrected.")

# 4. Feature Engineering and Outlier Treatment
print("\nStep 3: Feature Engineering and Outlier Handling...")
# Create 'TotalIncome' feature
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# Apply log transformation to handle outliers/skewness
df['TotalIncome_Log'] = np.log(df['TotalIncome'] + 1)
print("Engineered 'TotalIncome_Log' feature.")


# 5. Final DataFrame Preparation
print("\nStep 4: Preparing Final DataFrame...")
# Drop original columns that are no longer needed
df.drop(columns=['Loan_ID', 'ApplicantIncome', 'CoapplicantIncome', 'TotalIncome'], inplace=True)
print("Dropped unnecessary columns.")

# 6. Categorical Variable Encoding
print("\nStep 5: Encoding Categorical Variables...")
# Encode the target variable 'Loan_Status'
le = LabelEncoder()
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])

# Perform One-Hot Encoding on the remaining categorical features
categorical_features = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
print("Categorical variables encoded.")

# 7. Display and Save the Final Cleaned Data
print("\nData cleaning complete!")
print("\nFirst 5 rows of the final cleaned dataset:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv('Loan_cleaned.csv', index=False)
print("\nFinal cleaned data saved to 'Loan_cleaned.csv'.")