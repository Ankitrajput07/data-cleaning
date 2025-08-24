# data-cleaning
This repository contains a collection of Python scripts demonstrating various data cleaning and preparation techniques on real-world datasets. Each script takes a raw, messy CSV file and transforms it into a clean, analysis-ready dataset.


🚀 Projects Included
This portfolio showcases cleaning operations on four distinct datasets, each with its own unique challenges.

1. Loan Approval Prediction (loan.csv)
Challenge: This dataset contained standard missing values (NaN), outliers in income columns, and inconsistent categorical data ('3+').

Cleaning Operations:

Imputed missing values using median (for numerical) and mode (for categorical).

Corrected inconsistent data in the Dependents column.

Applied a log transformation to the Income feature to handle outliers and normalize the distribution.

Encoded categorical features for machine learning readiness.

2. Netflix Content Analysis (netflix1.csv)
Challenge: This dataset used text placeholders ("Not Given") for missing data, had incorrect data types for dates, and contained composite information in the duration column (e.g., "90 min", "1 Season").

Cleaning Operations:

Replaced text placeholders with standard NaN values.

Imputed missing director and country information.

Converted the date_added column to a proper datetime format.

Parsed the duration column into two separate numerical columns: duration_min and duration_seasons.

3. Space Mission Launches (mission_launches.csv)
Challenge: This dataset included redundant index columns, a Price column with a large number of missing values and non-numeric characters (commas), and a complex Location string containing multiple pieces of information.

Cleaning Operations:

Removed unnecessary columns.

Cleaned the Price column by removing commas, converting it to a numeric type, and imputing over 3,000 missing values with the median.

Converted the Date column to a timezone-aware datetime format.

Engineered a new Country feature by parsing it from the Location string.

4. Cafe Sales (dirty_cafe_sales.csv)
Challenge: A classic messy dataset with data integrity errors ("ERROR" in Total Spent), incorrect data types, and a mix of standard (NaN) and text-based ("UNKNOWN") missing values.

Cleaning Operations:

Ensured data integrity by recalculating the Total Spent column (Quantity * Price Per Unit) for all rows.

Handled both standard and non-standard missing values by imputing with the mode.

Corrected all relevant column data types, including Transaction Date.

🛠️ Technologies Used
Python

Pandas: For data manipulation and cleaning.

NumPy: For numerical operations and handling missing values.
