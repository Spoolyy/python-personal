import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temp_data = np.random.randint(low=10, high=35, size=30)

df = pd.DataFrame(temp_data, columns=['Temperature'])

max_temp = df['Temperature'].max()
min_temp = df['Temperature'].min()
avg_temp = df['Temperature'].mean()
med_temp = df['Temperature'].median()

labels = ['Highest', 'Lowest', 'Average', 'Median']
values = [max_temp, min_temp, avg_temp, med_temp]
days = range(0,30,1)

# you cannot use a histogram graph for this type of distribution beacuse the histogram 
# graphtype groups the values instead of displaying all of them, you must use a Block type Graph 

# remember to try and use all graph type, as a each different type of graph gives you
# a different perspective on the dataset

plt.figure()
plt.plot(days, temp_data)
plt.title('Grafico a Linee')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# plt.bar(labels, values, color=['red', 'blue', 'green', 'orange'])
# plt.title('Temperatures in the city')
# plt.xlabel('Last 30 days')
# plt.ylabel('Temperatures')