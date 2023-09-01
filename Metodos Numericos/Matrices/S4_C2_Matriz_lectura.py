'''
Solución de ejercicios propuestos en taller sobre matrices.
'''

import numpy as np
import scipy as sci

# Ejercicio 3
matL = np.loadtxt('Matrices\Matriz3L.txt')
matU = np.loadtxt('Matrices\Matriz3U.txt')
vecb = np.loadtxt('Matrices\Vectorb3.txt')

print("=".center(50,"="))
print(matL)
print("=".center(50,"="))
print(matU)
print("=".center(50,"="))
print(vecb)
print("=".center(50,"="))

print(' Taller punto 1 '.center(50, "-"))

"""
Evalúe el determinante de cada una de las siguientes matrices y clasifíquelas como singulares o 
no singulares. 

A)
1   2   3
2   3   4
3   4   5

B)
2.11    -0.80   1.72
-1.84   3.03    1.29
-1.57   5.25    4.30

C)
2   -1  0
-1  2   -1
0   -1  2

D)
4   3   -1
7   -2  3
5   -18 13
"""

matTaller1A = np.loadtxt('Matrices\MatrizTaller1_A.txt')
determinante = np.linalg.det(matTaller1A)
print(" Punto A ".center(50, "="))
print(determinante)

matTaller1B = np.loadtxt('Matrices\MatrizTaller1_B.txt')
determinante = np.linalg.det(matTaller1B)
print(" Punto B ".center(50, "="))
print(determinante)

matTaller1C = np.loadtxt('Matrices\MatrizTaller1_C.txt')
determinante = np.linalg.det(matTaller1C)
print(" Punto C ".center(50, "="))
print(determinante)

matTaller1D = np.loadtxt('Matrices\MatrizTaller1_D.txt')
determinante = np.linalg.det(matTaller1D)
print(" Punto D ".center(50, "="))
print(determinante)



print(' Taller punto 2 '.center(50, "-"))
"""
Dada la descomposición 𝐿𝑈 de 𝐴, determine 𝐴 y |𝐴|.

A)
L:
1   0   0
1   1   0
1   1.66666666666 1

U:
1   2   4
0   3   21
0   0   0

B)
L:
2   0   0
-1  1   0
1   -3  1

U:
2   -1  1
0   1   -3
0   0   1
"""
# Determinante de L
matTaller2AL = np.loadtxt('Matrices\MatrizTaller2A_L.txt')
determinante = np.linalg.det(matTaller2AL)
print("Determinante de (L): ",determinante)

# Determinante de U
matTaller2AU = np.loadtxt('Matrices\MatrizTaller2A_U.txt')
determinante = np.linalg.det(matTaller2AU)
print(" Punto A (U) ".center(50, "="))
print("Determinante de (U): ",determinante)

# Determinante de L*U
detp = matTaller2AL * matTaller2AU
print(" Punto A (L*U) ".center(50, "="))
print("Determinante de (L*U): \n", detp)

# Determinante de A
A = np.matmul(matTaller2AL, matTaller2AU)
detA = np.linalg.det(A)
print(" Punto A (Determinante A) ".center(50, "="))
print("Determinante de (Determinante A): \n", detA)

