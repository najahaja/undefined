import pandas as pd

# Sample data (as before)
data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Strip any potential spaces in column names
df.columns = df.columns.str.strip()

# Debugging: Print out the columns and the first few rows
print("Columns in the dataset:", df.columns)
print("First few rows of the dataset:")
print(df.head())

# Check if 'salary' exists
if 'salary' not in df.columns:
    print("Error: 'salary' column not found!")
else:
    print("The 'salary' column is present!")

def race_count(df):
    return df['race'].value_counts()

def average_age_of_men(df):
    men = df[df['sex'] == 'Male']
    return round(men['age'].mean(), 1)

def percentage_bachelors(df):
    bachelors = df[df['education'] == 'Bachelors']
    return round((len(bachelors) / len(df)) * 100, 1)

def percentage_advanced_education_with_salary(df):
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_50k = advanced_education[advanced_education['salary'] == '>50K']
    return round((len(advanced_education_50k) / len(advanced_education)) * 100, 1)

def percentage_no_advanced_education_with_salary(df):
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    no_advanced_education_50k = no_advanced_education[no_advanced_education['salary'] == '>50K']
    return round((len(no_advanced_education_50k) / len(no_advanced_education)) * 100, 1)

def min_work_hours(df):
    return df['hours-per-week'].min()

def percentage_min_workers_with_salary(df):
    min_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_hours]
    min_workers_50k = min_workers[min_workers['salary'] == '>50K']
    return round((len(min_workers_50k) / len(min_workers)) * 100, 1)

def country_with_highest_salary_percentage(df):
    # First, create a boolean mask for those earning >50K
    df['is_high_salary'] = df['salary'] == '>50K'
    
    # Group by native-country and calculate the percentage of people earning >50K
    country_salary = df.groupby('native-country').agg(
        high_salary_percentage=('is_high_salary', 'mean')  # This gives us the percentage of True values
    )
    
    # Find the country with the highest percentage of people earning >50K
    max_country = country_salary['high_salary_percentage'].idxmax()
    max_percentage = country_salary['high_salary_percentage'].max() * 100  # Convert to percentage
    
    return max_country, round(max_percentage, 1)

def top_occupation_in_india(df):
    india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if india_50k.empty:
        return "No data for people earning >50K in India"
    else:
        return india_50k['occupation'].value_counts().idxmax()

# Run the functions after checking if 'salary' column exists
if 'salary' in df.columns:
    print("Race count:\n", race_count(df))
    print("Average age of men:", average_age_of_men(df))
    print("Percentage with Bachelor's degree:", percentage_bachelors(df))
    print("Percentage with advanced education making >50K:", percentage_advanced_education_with_salary(df))
    print("Percentage without advanced education making >50K:", percentage_no_advanced_education_with_salary(df))
    print("Minimum work hours:", min_work_hours(df))
    print("Percentage of workers with min hours earning >50K:", percentage_min_workers_with_salary(df))
    print("Country with highest % earning >50K:", country_with_highest_salary_percentage(df))
    print("Most popular occupation in India for people earning >50K:", top_occupation_in_india(df))
