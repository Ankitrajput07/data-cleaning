import pandas as pd
import numpy as np

# 1. Load the dataset
print("Loading the Netflix dataset...")
df = pd.read_csv('csv_datas/netflix1.csv')
print("Dataset loaded successfully.")

# 2. Handle "Hidden" Missing Values
print("\nStep 1: Handling 'hidden' missing values...")
# Replace the placeholder "Not Given" with a standard NaN value
df.replace("Not Given", np.nan, inplace=True)
print("'Not Given' values have been replaced.")

# 3. Impute Missing Data
print("\nStep 2: Imputing missing data...")
# Fill missing 'director' values with "Unknown"
df['director'].fillna("Unknown", inplace=True)

# Fill missing 'country' values with the mode (most frequent country)
country_mode = df['country'].mode()[0]
df['country'].fillna(country_mode, inplace=True)
print("Missing 'director' and 'country' values have been imputed.")

# 4. Correct Data Types
print("\nStep 3: Correcting data types...")
# Convert 'date_added' from text to a proper datetime format
df['date_added'] = pd.to_datetime(df['date_added'])
print("'date_added' column converted to datetime.")

# 5. Parse the 'duration' Column
print("\nStep 4: Parsing the 'duration' column...")
# Split the 'duration' column into a number and a unit
temp_duration = df['duration'].str.split(' ', expand=True)
duration_val = pd.to_numeric(temp_duration[0])
duration_unit = temp_duration[1]

# Create new columns for minutes (for movies) and seasons (for TV shows)
df['duration_min'] = np.where(duration_unit.str.contains('min', na=False), duration_val, 0)
df['duration_seasons'] = np.where(duration_unit.str.contains('Season', na=False), duration_val, 0)

# Drop the original and temporary columns
df.drop(columns=['duration'], inplace=True)
print("Created 'duration_min' and 'duration_seasons' columns.")

# 6. Display and Save the Final Cleaned Data
print("\nData cleaning is complete! ✨")
print("\nFirst 5 rows of the final cleaned dataset:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv('netflix_cleaned.csv', index=False)
print("\nFinal cleaned data has been saved to 'netflix_cleaned.csv'.")