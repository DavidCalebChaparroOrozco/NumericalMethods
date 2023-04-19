# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# INGRESO , Datos de prueba
xi = np.array([1/4, 1/2, 1, 5/4])
fi = np.array([22.98, 47.23, 80.49, 121.26])

# PROCEDIMIENTO
# Polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)
for i in range(0,n,1):
    
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = sym.lambdify(x,polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)



#-----------------------------------------------------------

# Crea los datos de ejemplo
x2 = [0, 1/4, 1/2, 1, 5/4]
y2 = [0, 22.98, 47.23, 97.49, 122.66]

# Crea la función de interpolación basada en funciones de base radial
rbf = Rbf(x2, y2, function='multiquadric', epsilon=2)

# Evalúa la función de interpolación en el punto 3/4,67.48
xsubi = np.linspace(0, 2, 101)
yi = rbf(xsubi)


# SALIDA
print('    valores de fi: ',fi)
print('divisores en L(i): ',divisorL)
print()
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(polisimple)

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.plot(x2, y2, 'x', label='Datos originales')
plt.plot(xsubi, yi, '-', label='Interpolación basada en funciones de base radial')
plt.legend()
plt.xlabel('Distancia(millas)')
plt.ylabel('Tiempo(seg)')
plt.title('Interpolación Lagrange')
plt.show()