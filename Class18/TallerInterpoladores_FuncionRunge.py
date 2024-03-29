# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Función de evaluación de FBR multicuádrica
def rbffunction(xev, xdat, c):
    rbfv = np.sqrt((xev - xdat)**2 + c**2)
    return rbfv

# Construcción de la matriz de interpolación
def interpmat(xdat, c):
    nd = len(xdat)
    mat1 = np.zeros((nd,nd),float)
    for i in range (nd):
        for j in range (nd):
            mat1[i,j] = rbffunction(xdat[i], xdat[j], c)
    return mat1

# Superposición de funciones de base radial
def rbfsuperposit(x, coef, xdat, c):
    y = np.zeros((len(x)))
    for i in range (len(x)):
        for j in range (len(xdat)):
            y[i] = y[i] + coef[j]*rbffunction(x[i], xdat[j], c)
    return y

time = [1,3,5,6]
