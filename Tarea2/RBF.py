import numpy as np


def rbffunction(xev, xdat, c):
    rbfv = np.sqrt((xev - xdat)**2 + c**2)
    return rbfv

# Construcción de la matriz de interpolación
def interpmat(xdat, c):
    numero_datos = len(xdat)
    mat1 = np.zeros((numero_datos,numero_datos),float)
    for i in range (numero_datos):
        for j in range (numero_datos):
            mat1[i,j] = rbffunction(xdat[i], xdat[j], c)
    return mat1

# Superposición de funciones de base radial
def rbfsuperposit(x, coef, xdat, c):
    y = np.zeros((len(x)))
    for i in range (len(x)):
        for j in range (len(xdat)):
            y[i] = y[i] + coef[j]*rbffunction(x[i], xdat[j], c)
    return y