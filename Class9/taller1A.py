import numpy as np
import scipy as sci

MatrizA = np.loadtxt('Class9\matriz.txt')
print(MatrizA)
# Es una matriz bien condicionada, ya que no tiene valores propios muy diferentes en magnitud. 
# Además, la matriz no es singular, ya que su determinante es diferente de cero. 

# MatrizA = np.array([[1., 2., 3.], [2., 3., 4.], [3., 4.,5.]])
print(MatrizA)
# result =np.linalg.inv(MatrizA)
result = np.linalg.det(MatrizA)
print(f'Determinante de la Matriz A: {result}')


## Error de:
# MatrizA_inv = np.linalg.inv(MatrizA)
# print(f'Inversa de MatrizA: {MatrizA_inv}')

# La matriz es singular: El determinante es cero, entonces la matriz no tiene una inversa y 
# linalg.inv() arrojará el error. Esto significa que la matriz es  linealmente dependiente y no se 
# pueden encontrar suficientes ecuaciones lineales independientes para encontrar una solución única.

# La matriz es malcondicionada: La matriz es malcondicionada, es decir, sus valores propios tienen 
# una gran diferencia en magnitud, entonces la inversión de la matriz puede ser numéricamente 
# inestable y linalg.inv() puede arrojar un error o una solución inexacta.

