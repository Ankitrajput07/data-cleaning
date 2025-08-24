import pandas as pd
import numpy as np

# 1. Load the dataset
print("Loading the Mission Launches dataset...")
df = pd.read_csv('csv_datas/mission_launches.csv')
print("Dataset loaded successfully.")

# 2. Initial Column Cleanup
print("\nStep 1: Dropping unnecessary columns...")
# Drop the redundant 'Unnamed' index columns safely
df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'], inplace=True, errors='ignore')
print("Columns dropped (if they existed).")

# 3. Clean and Process the 'Price' Column
print("\nStep 2: Cleaning and imputing the 'Price' column...")
# Ensure Price is string before replacing commas
df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace(',', '', regex=False), errors='coerce')

# Calculate the median price to fill in missing values
price_median = df['Price'].median()

# Fill the NaN values with the calculated median
df['Price'].fillna(price_median, inplace=True)
print("'Price' column has been cleaned and imputed.")

# 4. Convert the 'Date' Column
print("\nStep 3: Converting the 'Date' column to datetime format...")
date_format = "%a %b %d, %Y %H:%M UTC"
df['Date'] = pd.to_datetime(df['Date'], format=date_format, errors='coerce')
print("'Date' column converted (invalid formats set as NaT).")

# 5. Feature Engineering: Extract Country from Location
print("\nStep 4: Engineering 'Country' feature from 'Location'...")
df['Country'] = df['Location'].str.split(',').str[-1].str.strip()
print("'Country' column created.")

# 6. Display and Save the Final Cleaned Data
print("\nData cleaning is complete! 🚀")
print("\nFirst 5 rows of the final cleaned dataset:")
print(df.head())

# Save the final DataFrame to a new CSV file
df.to_csv('mission_launches_cleaned.csv', index=False)
print("\nFinal cleaned data has been saved to 'mission_launches_cleaned.csv'.")
