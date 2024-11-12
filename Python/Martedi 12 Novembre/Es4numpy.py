import numpy as np

#creating a 50 number linspace array
ls_arr = np.linspace(0,1,50)
print(f'Linspace array:')
print(f'{ls_arr}')
print('')

#creating a 50 number random array
rd_arr = np.random.rand(50)
print(f'Random array:')
print(f'{rd_arr}')
print('')

#sum of both arrays element by element
ls_rd_arr = ls_arr + rd_arr
print(f'Sum of both arrays:')
print(f'{ls_rd_arr}')
print('')

#sum of the elements of the summed array
sum_lsrd = np.sum(ls_rd_arr)
print(f'Sum of elements of summed array:')
print(f'{sum_lsrd}')
print('')

#sum of the elements of summed array only where element > 1
sum_lsrd_1 = np.sum(ls_rd_arr[ls_rd_arr > 1])
print(f'Sum of elements of summed array bigger than 5:')
print(f'{sum_lsrd_1}')
print('')