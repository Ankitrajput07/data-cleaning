import pandas as pd
import numpy as np

# Load the dirty dataset
df = pd.read_csv('dirty_cafe_sales/dirty_cafe_sales.csv')
print("--- Data Before Cleaning ---")
print(df.head(10))
print("\n--- Info Before Cleaning ---")
df.info()

# --- Step 1: Convert Columns to Numeric Before Calculation ---
# This is the FIX: Convert columns to numbers, turning any non-numeric text into NaN
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')

# --- Step 2: Fix and Recalculate the 'Total Spent' Column ---
# This corrects the 'ERROR' values and ensures all totals are accurate.
df['Total Spent'] = df['Quantity'] * df['Price Per Unit']

# --- Step 3: Handle Missing and Placeholder Values ---
# We will replace both 'UNKNOWN' and standard NaN values.
# For each categorical column, we find the most common value (mode) and use it to fill the gaps.
categorical_cols = ['Item', 'Payment Method', 'Location']

for col in categorical_cols:
    # First, replace the text placeholder 'UNKNOWN' with a standard NaN
    df[col].replace('UNKNOWN', np.nan, inplace=True)
    
    # Then, find the mode (most frequent value) of the column
    mode_value = df[col].mode()[0]
    
    # Finally, fill all NaN values with the mode
    df[col].fillna(mode_value, inplace=True)

# --- Step 4: Convert 'Transaction Date' to Datetime ---
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])


# --- Verification: Display the Cleaned Data ---
print("\n\n--- Data After Cleaning ---")
print(df.head(10))
print("\n--- Info After Cleaning ---")
df.info()

# Save the cleaned data to a new file
df.to_csv('cleaned_cafe_sales.csv', index=False)
print("\nCleaned data saved to 'cleaned_cafe_sales.csv'")
