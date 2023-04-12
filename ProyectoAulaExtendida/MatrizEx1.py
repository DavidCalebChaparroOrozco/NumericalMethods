import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

MatrizA = np.array([[1,np.exp(-1)], [np.exp(1),1]])
print(f'El vector original: {MatrizA}')

v_res = np.array([0,1])
print(f'El vector resultante: {v_res}')

MatrizA_solv = np.linalg.solve(MatrizA, v_res)
print(f'Matriz resuelta: {MatrizA_solv}')
