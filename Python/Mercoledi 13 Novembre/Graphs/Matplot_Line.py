import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,7,4,7,3,9]

plt.figure()
plt.plot(x,y)
plt.title('Grafico a Linee')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# plt.rcParams['figure.figsize'] = [10, 6]  
# # Imposta la dimensione predefinita delle figure

# plt.rcParams['figure.dpi'] = 100          
# # Imposta la risoluzione delle figure in DPI