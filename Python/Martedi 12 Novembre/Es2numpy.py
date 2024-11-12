import numpy as np

x = np.random.randint(10, 50, size=40)
print("array monodimensionale con numeri casuali: ",x)
print("")
print("array casuale, che richiama i valori degli indici da 1 a 10: ",x[:10])
print("")
print("array sempre casuale, che richiama i valori degli indici dal 35 al 40",x[-5:])
print("")
print("sempre il solito array casuale, da cui estrapoliamo i valori degli indici che vanno dal 5 al 15",x[5:15])
print("")
print("prendiamo sempre il nostro array casuale, questa volta stampiamo i valori a balzi di 3: ", x[0:40:3])
print("")
x[5:10] = 99
print("dopo aver assegnato un nuovo valore agli indici da 5 a 10, stampo tutto l'array casuale: ", x)