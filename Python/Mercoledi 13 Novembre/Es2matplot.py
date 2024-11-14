import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temp_data = np.random.randint(low=10, high=35, size=30)
temp_data2 = temp_data
df = pd.DataFrame(temp_data, columns=['Temperature'])

max_temp = df['Temperature'].max()
min_temp = df['Temperature'].min()
avg_temp = df['Temperature'].mean()
med_temp = df['Temperature'].median()

labels = ['Highest', 'Lowest', 'Average', 'Median']
values = [max_temp, min_temp, avg_temp, med_temp]
days = range(0,30,1)
days2 = days

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

ax1.plot(days2, temp_data2)
ax1.set_title('Grafico a Barre')
ax1.set_xlabel('Categorie')
ax1.set_ylabel('Valori')

for i, (days2, temp_data2) in enumerate(zip(days2, temp_data2)): 
    if temp_data2 <= 15: 
        ax1.annotate( "Temperatura bassa", xy=(days2, temp_data2), xytext=(days2, temp_data2 + 1), arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center' )
        
ax2.scatter(days, temp_data)
ax2.set_title('Grafico a Barre')
ax2.set_xlabel('Categorie')
ax2.set_ylabel('Valori')

for i, (days, temp_data) in enumerate(zip(days, temp_data)): 
    if temp_data >= 30: 
        ax2.annotate( "Temperatura alta!", xy=(days, temp_data), xytext=(days, temp_data + 1), arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center' )

plt.tight_layout()
plt.show()

