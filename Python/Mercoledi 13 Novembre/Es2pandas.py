import numpy as np
import pandas as pd

data = {
    'Product': ['T-Shirt', 'Jeans', 'Hoodie', 'Sweatshirt', 'Gloves'],
    'Amount': [50, 45, 75, 25, 100],
    'Price': [15, 25, 45, 40, 5],
    'City': ['London', 'Los Angeles', 'Tokyo', 'Rome', 'Chicago']
}

sales = pd.DataFrame(data)

sales = sales.drop_duplicates()
sales_cleaned = sales.dropna()
sales['Amount'].fillna(sales['Amount'].mean(), inplace=True)
sales['Price'].fillna(sales['Price'].mean(), inplace=True)

sales['Total Sales'] = sales['Amount'] * sales['Price']

most_sold = sales.groupby('Product')['Amount'].sum().idxmax()
highest_quantity = sales.groupby('Product')['Amount'].sum().max()
bigsales = sales[sales['Total Sales'] > 1000]
sales_sorted = sales.sort_values(by='Total Sales', ascending=False)
sales_by_city = sales['City'].value_counts()

print(sales)
print('')
print(most_sold, highest_quantity)
print('')
print(bigsales)
print('')
print(sales_sorted)
print('')
print(sales_by_city)
