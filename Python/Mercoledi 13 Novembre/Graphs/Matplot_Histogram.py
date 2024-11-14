import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(1000)

plt.figure()
plt.hist(data, bins=100)# bins are the amount elements based on wich we divide the relations of the histogram
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()