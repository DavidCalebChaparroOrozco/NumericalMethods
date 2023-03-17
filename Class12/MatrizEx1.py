import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
# import MetInterpolacion

MatrizA = np.loadtxt('Class12\matrizEx1.txt')
print(MatrizA)
# Es una matriz bien condicionada, ya que no tiene valores propios muy diferentes en magnitud. 
# Además, la matriz no es singular, ya que su determinante es diferente de cero. 

# MatrizA = np.array([[1., 2., 3.], [2., 3., 4.], [3., 4.,5.]])
print(f'El vector original: {MatrizA}')
# result =np.linalg.inv(MatrizA)

v_res = np.array([[0],[1.3862],[1.6094],[1.7917]])
print(f'El vector resultante: {v_res}')

MatrizA_solv = np.linalg.solve(MatrizA, v_res)
print(f'Matriz resuelta: {MatrizA_solv}')

v_x = np.arange(1,4,0.1)
# v_x = np.array([[1],[4],[5],[6],[7],[8],[9]])

plt.plot(v_x, MatrizA_solv,'--', label='Metodo de la frontera',marker="o")
plt.show()