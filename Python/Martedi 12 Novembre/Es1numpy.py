import numpy as np

x = np.random.randint(10, 50, (6, 6))
print("6x6 casuale: ", x)
x[1:5, 1:5]
print("quadrato 4x4: ", x[1:5, 1:5])
y = x[::-1]
print("")
print("righe invertite", y)
print("")
print("righe a step di 3",y[::3])