from trazadores_lineales import *
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


xi = [0.1, 0.2, 0.3, 0.40, 0.5]
yi = [1.5, 1.8, 1.9, 1.95, 2.0]

muestra = 10

n = len(xi)
px_table = trazador_lineal(xi,yi)

print('Polinomio por tramos: ')
for tramo in range(1,n,1):
    print('x = [' + str(xi[tramo-1]) + ',' + str(xi[tramo])+']')
    print(str(px_table[tramo-1]))

## Graficar
xtraza = np.array([])
ytraza = np.array([])
tramo = 1

while not(tramo>=n):
    a = xi[tramo-1]
    b = xi[tramo]
    xtramo = np.linspace(a,b,muestra)

    # Evaluar polinomio del tramo.
    pxtramo = px_table[tramo-1]
    pxt = sym.lambdify('x',pxtramo)
    ytramo = pxt(xtramo)

    # Vectores de trazador en x,y
    xtraza = np.concatenate((xtraza,xtramo))
    ytraza = np.concatenate((ytraza,ytramo))
    tramo = tramo + 1

# Gráfica
plt.plot(xi,yi,'o', label='puntos')
plt.plot(xtraza,ytraza, label='trazador')
plt.title('Trazadores lineales (splines)')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()