import pandas as pd
import numpy as np

data =  {
    'Name': ['Charles', 'Lewis', 'Carlos', 'Max', 'Lando'],
    'Age': [27, 39, 27, np.nan, 26],
    'City': ['Monaco', 'London', 'Barcelona', 'Spa', 'London'],
    'Salary': [450000, 600000, 250000, 650000, 400000]
}

base_dataframe = pd.DataFrame(data)
base_dataframe = base_dataframe.drop_duplicates()

print(f'Original Dataframe: ')
print(base_dataframe)
print('')

cleaned_dataframe = base_dataframe.dropna()

print('Cleaned Dataframe:')
print(cleaned_dataframe)
print('')

base_dataframe['Age'].fillna(base_dataframe['Age'].mean(), inplace=True)

def agetypes(age):
    if age <= 18:
        return 'Junior'
    elif 19 <= age <= 65:
        return 'Adult'
    else:
        return 'Senior'
    
base_dataframe['Age Category'] = base_dataframe['Age'].apply(agetypes)

print('First 2 rows of the Dataframe:')
print(base_dataframe.head(2))
print('')
print('Last 2 rows of the Dataframe:')
print(base_dataframe.tail(2))
print('')

print('Data types of the Dataframe:')
print(base_dataframe.dtypes)
print('')

base_dataframe.to_csv('FirstDataFrame.csv', index=False)
print("DataFrame saved to 'FirstDataFrame.csv'")