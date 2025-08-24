# 🧹 Data Cleaning Cheat Sheet

A comprehensive reference guide for data cleaning operations in Python using pandas.

## 📊 Quick Data Assessment

```python
# Basic dataset info
df.info()                    # Data types and memory usage
df.shape                     # Rows and columns
df.columns                   # Column names
df.dtypes                    # Data types per column

# Missing values
df.isnull().sum()           # Count missing per column
df.isnull().sum().sum()     # Total missing values
df.isnull().sum() / len(df) * 100  # Percentage missing

# Duplicates
df.duplicated().sum()       # Count duplicate rows
df.duplicated(subset=['col1', 'col2']).sum()  # Duplicates based on specific columns

# Unique values
df.nunique()                # Unique values per column
df['column'].value_counts() # Value frequency
```

## 🔍 Data Quality Checks

### Missing Values
```python
# Check for missing values
df.isnull().sum()

# Visualize missing values
import seaborn as sns
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# Handle missing values
df.dropna()                 # Remove rows with any missing values
df.dropna(subset=['col1'])  # Remove rows missing specific column
df.fillna(0)                # Fill with constant value
df.fillna(df.mean())        # Fill with mean
df.fillna(df.median())      # Fill with median
df.fillna(df.mode()[0])     # Fill with mode
df.fillna(method='ffill')   # Forward fill
df.fillna(method='bfill')   # Backward fill
```

### Duplicates
```python
# Remove duplicates
df.drop_duplicates()                    # Remove exact duplicates
df.drop_duplicates(subset=['col1'])     # Remove based on specific column
df.drop_duplicates(keep='first')        # Keep first occurrence
df.drop_duplicates(keep='last')         # Keep last occurrence
df.drop_duplicates(keep=False)          # Remove all duplicates
```

### Data Types
```python
# Convert data types
df['column'] = df['column'].astype('int64')      # To integer
df['column'] = df['column'].astype('float64')    # To float
df['column'] = pd.to_datetime(df['column'])      # To datetime
df['column'] = df['column'].astype('category')   # To category

# Check data types
df.dtypes
df.select_dtypes(include=['object'])     # Select string columns
df.select_dtypes(include=['number'])     # Select numeric columns
```

## 🧹 Text Data Cleaning

### String Operations
```python
# Basic string cleaning
df['column'] = df['column'].str.strip()           # Remove whitespace
df['column'] = df['column'].str.lower()           # Convert to lowercase
df['column'] = df['column'].str.upper()           # Convert to uppercase
df['column'] = df['column'].str.title()           # Title case
df['column'] = df['column'].str.capitalize()      # Capitalize first letter

# Replace patterns
df['column'] = df['column'].str.replace('old', 'new')           # Simple replace
df['column'] = df['column'].str.replace(r'[^\w\s]', '', regex=True)  # Remove punctuation
df['column'] = df['column'].str.replace(r'\s+', ' ', regex=True)      # Multiple spaces to single

# Extract patterns
df['new_col'] = df['column'].str.extract(r'(\d+)')             # Extract numbers
df['new_col'] = df['column'].str.extract(r'([A-Za-z]+)')       # Extract letters
```

### Email Validation
```python
# Basic email validation
import re
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df['valid_email'] = df['email'].str.match(email_pattern)

# Remove invalid emails
df = df[df['email'].str.contains('@', na=False)]
```

### Phone Number Cleaning
```python
# Clean phone numbers
df['phone'] = df['phone'].str.replace(r'[^\d+]', '', regex=True)  # Keep only digits and +
df['phone'] = df['phone'].str.replace(r'^\+1', '', regex=True)    # Remove country code
df['phone'] = df['phone'].str.replace(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', regex=True)  # Format
```

## 🔢 Numeric Data Cleaning

### Outlier Detection
```python
# IQR method for outliers
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df_clean = df[(df['column'] >= lower_bound) & (df['column'] <= upper_bound)]

# Z-score method
from scipy import stats
z_scores = stats.zscore(df['column'])
df_clean = df[abs(z_scores) < 3]  # Remove values with |z-score| > 3
```

### Range Validation
```python
# Validate age ranges
df = df[(df['age'] >= 0) & (df['age'] <= 120)]

# Validate percentages
df = df[(df['percentage'] >= 0) & (df['percentage'] <= 100)]

# Validate amounts
df = df[df['amount'] >= 0]
```

### Scaling and Normalization
```python
# Min-Max scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['scaled_column'] = scaler.fit_transform(df[['column']])

# Standard scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['scaled_column'] = scaler.fit_transform(df[['column']])
```

## 📅 Date and Time Cleaning

### Date Parsing
```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Handle multiple formats
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
```

### Date Validation
```python
# Remove future dates
df = df[df['date'] <= pd.Timestamp.now()]

# Remove very old dates
df = df[df['date'] >= pd.Timestamp('2000-01-01')]

# Check date ranges
df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2023-12-31')]
```

## 🏷️ Categorical Data Cleaning

### Category Standardization
```python
# Create mapping dictionary
category_mapping = {
    'Electronix': 'Electronics',
    'Electroncs': 'Electronics',
    'Cloth': 'Clothing',
    'Clothes': 'Clothing'
}

# Apply mapping
df['category'] = df['category'].replace(category_mapping)

# Standardize case
df['category'] = df['category'].str.title()
```

### Encoding Categorical Variables
```python
# One-hot encoding
df_encoded = pd.get_dummies(df, columns=['category'])

# Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])
```

## 🔄 Data Transformation

### Reshaping Data
```python
# Melt (wide to long)
df_long = df.melt(id_vars=['id'], value_vars=['col1', 'col2'], 
                   var_name='variable', value_name='value')

# Pivot (long to wide)
df_wide = df.pivot(index='id', columns='variable', values='value')

# Stack/Unstack
df_stacked = df.set_index(['id', 'date']).stack()
df_unstacked = df_stacked.unstack()
```

### Aggregations
```python
# Group by operations
df_grouped = df.groupby('category').agg({
    'amount': ['mean', 'sum', 'count'],
    'age': ['mean', 'min', 'max']
})

# Pivot tables
df_pivot = df.pivot_table(values='amount', index='category', 
                          columns='region', aggfunc='mean', fill_value=0)
```

## ✅ Data Validation

### Custom Validation Functions
```python
def validate_age(age):
    """Validate age is reasonable"""
    return 0 <= age <= 120

def validate_email(email):
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Apply validation
df['valid_age'] = df['age'].apply(validate_age)
df['valid_email'] = df['email'].apply(validate_email)
```

### Data Quality Score
```python
def calculate_data_quality_score(df):
    """Calculate overall data quality score"""
    completeness = 1 - (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]))
    uniqueness = 1 - (df.duplicated().sum() / len(df))
    validity = 1 - (len(df[df['age'] < 0]) / len(df))  # Example for age
    
    return (completeness + uniqueness + validity) / 3

quality_score = calculate_data_quality_score(df)
print(f"Data Quality Score: {quality_score:.2%}")
```

## 🚀 Performance Tips

### Efficient Operations
```python
# Use vectorized operations instead of loops
df['new_col'] = df['col1'] + df['col2']  # ✅ Good
# for i in range(len(df)): df.loc[i, 'new_col'] = df.loc[i, 'col1'] + df.loc[i, 'col2']  # ❌ Bad

# Use .loc and .iloc for indexing
df.loc[df['age'] > 18, 'adult'] = True  # ✅ Good
# df[df['age'] > 18]['adult'] = True  # ❌ Bad (SettingWithCopyWarning)

# Use appropriate data types
df['category'] = df['category'].astype('category')  # Memory efficient for categorical data
```

### Memory Optimization
```python
# Check memory usage
df.memory_usage(deep=True)

# Optimize data types
df_optimized = df.astype({
    'int_col': 'int32',      # Instead of int64
    'float_col': 'float32',  # Instead of float64
    'category_col': 'category'
})
```

## 📝 Best Practices Checklist

### Before Cleaning
- [ ] Make a backup of original data
- [ ] Understand the business context
- [ ] Document data quality issues
- [ ] Set cleaning priorities

### During Cleaning
- [ ] Work with copies, not originals
- [ ] Document each cleaning step
- [ ] Validate results after each step
- [ ] Use appropriate methods for data types

### After Cleaning
- [ ] Verify data quality improvements
- [ ] Check for unintended data loss
- [ ] Document final dataset
- [ ] Save cleaned data with metadata

## 🎯 Common Data Quality Issues & Solutions

| Issue | Detection | Solution |
|-------|-----------|----------|
| Missing values | `df.isnull().sum()` | `fillna()`, `dropna()` |
| Duplicates | `df.duplicated().sum()` | `drop_duplicates()` |
| Outliers | IQR method, Z-score | Remove or cap values |
| Invalid ranges | Range checks | Filter or recode |
| Format inconsistencies | Pattern matching | String operations |
| Data type mismatches | `df.dtypes` | `astype()`, `pd.to_datetime()` |
| Encoding issues | Character inspection | `encode()`, `decode()` |

## 🔧 Advanced Techniques

### Fuzzy String Matching
```python
from fuzzywuzzy import fuzz, process

# Find similar strings
similar = process.extract('Electronics', df['category'].unique(), limit=5)

# Fuzzy string replacement
def fuzzy_replace(text, choices, threshold=80):
    match = process.extractOne(text, choices)
    return match[0] if match[1] >= threshold else text
```

### Regular Expressions
```python
# Extract patterns
df['area_code'] = df['phone'].str.extract(r'\((\d{3})\)')
df['domain'] = df['email'].str.extract(r'@([^.]+)')

# Complex replacements
df['clean_text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)
```

---

**💡 Pro Tip**: Always start with data exploration and quality assessment before cleaning. Understanding your data helps you choose the right cleaning strategies!

**📚 Remember**: Data cleaning is iterative. Clean, validate, repeat until you're satisfied with the data quality.
