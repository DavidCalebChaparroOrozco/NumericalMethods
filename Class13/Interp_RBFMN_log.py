import numpy as np
import matplotlib.pyplot as plt
import MetInterpolacion as mint

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

# Información de entrada
# datos = np.loadtxt('Class13\dat_log.txt')
datos = np.loadtxt('Class13\dat_log2.txt')
xdat = datos[:,0]
ydat = datos[:,1]
c = 0.5  # Parámetro de forma

# Matriz de interpolación
matint = interpmat(xdat, c)
# Coeficientes de la interpolación
coef = np.linalg.solve(matint, ydat)

# Evaluación de la superposición sobre un intervalo
x = np.arange(-2., 2.05, 0.05)
yinterp = rbfsuperposit(x, coef, xdat, c)
fbr1 = rbffunction(x, xdat[0], c)
fbr2 = rbffunction(x, xdat[1], c)
fbr3 = rbffunction(x, xdat[2], c)
fbr4 = rbffunction(x, xdat[3], c)
ylagrange = mint.interp_lagrange(x, xdat, ydat)

# Cálculo del error RMS entre la interpolación y la función dada
Err = np.sqrt((np.sum((yinterp - (np.log(x))))**2)/len(yinterp))
print('Parámetro de forma: ', c)
print('Error RMS de la aproximación: ', Err)

# Sumas parciales de la interpolación
yinterp6 = rbfsuperposit(x, coef[0:6], xdat[0:6], c)
yinterp7 = rbfsuperposit(x, coef[0:7], xdat[0:7], c)
yinterp8 = rbfsuperposit(x, coef[0:8], xdat[0:8], c)

# Gráficas

plt.figure()
plt.plot(x, (np.cos(x))**10, label = 'Función dada')
plt.plot(x, yinterp6, label = 'Interpolación RBF6')
plt.plot(x, yinterp7, label = 'Interpolación RBF7')
plt.plot(x, yinterp8, label = 'Interpolación RBF8')
plt.plot(x, yinterp, label = 'Interpolación RBF')
plt.plot(xdat, ydat, 'or', label = 'Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Sucesión de sumas parciales con RBF')

plt.figure()
plt.plot(x, (np.cos(x))**10, label = 'Función dada')
plt.plot(x, fbr1, label = 'RBF1 evaluada en el intervalo de interés')
plt.plot(x, fbr2, label = 'RBF2 evaluada en el intervalo de interés')
plt.plot(x, fbr3, label = 'RBF3 evaluada en el intervalo de interés')
plt.plot(x, fbr4, label = 'RBF4 evaluada en el intervalo de interés')
plt.plot(xdat, ydat, 'or', label = 'Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('RBFs utilizadas en la interpolación')

plt.figure()
plt.plot(x, (np.cos(x))**10, label = 'Función dada')
plt.plot(x, yinterp, label = 'Interpolación RBF')
plt.plot(x, ylagrange, label = 'Polinomio de Lagrange')
plt.plot(xdat, ydat, 'or', label = 'Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Interpolación con Funciones de Base Radial')

plt.show()