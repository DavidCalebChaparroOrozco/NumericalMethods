import numpy as np
import scipy as sci

MatrizA = np.loadtxt('Class9\matriz.txt')
print(MatrizA)

# MatrizA = np.array([[1., 2., 3.], [2., 3., 4.], [3., 4.,5.]])
result =np.linalg.det(MatrizA)
print(f'Resultado: {result}')
