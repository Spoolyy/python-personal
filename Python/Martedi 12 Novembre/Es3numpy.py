import numpy as np

es_arr = np.linspace(0,1,12)
print('array di partenza: ')
print(f'{es_arr}')
print('')
resh_arr = es_arr.reshape(3,4)
print('array reshape:')
print(f'{resh_arr}')
print('')
matr_arr = np.random.rand(3,4)
print('array matrix:')
print(f'{matr_arr}')
print('')
sum_resh_arr = np.sum(resh_arr)
sum_matr_arr = np.sum(matr_arr)

print(f'Somma array reshape: {sum_resh_arr}')
print(f'Somma array matrix: {sum_matr_arr}')