import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Definir la función de Runge
def runge(x):
    return 1 / (1 + 25 * x ** 2)

# 1.- Graficar la función de Runge en el intervalo [-1,1]
x = np.linspace(-1, 1, 1000)
y = runge(x)
plt.plot(x, y)
plt.title("Función de Runge")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 2.- Generar y graficar el polinomio de interpolación de Lagrange
xi = np.array([-1, -0.5, 0, 0.5, 1])
yi = runge(xi)
poly = lagrange(xi, yi)
x = np.linspace(-1, 1, 1000)
y = poly(x)
plt.plot(x, y, label="Polinomio de Lagrange")
plt.plot(xi, yi, "o", label="Datos equiespaciados")
plt.plot(x, runge(x), label="Función de Runge")
plt.title("Polinomio de Lagrange para la Función de Runge")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# 3.- Estimar f(0.8) con polinomios de interpolación de grado 2 y 3
poly2 = lagrange(xi[1:4], yi[1:4])
poly3 = lagrange(xi, yi)
print("El valor estimado de f(0.8) con polinomio de grado 2 es:", poly2(0.8))
print("El valor estimado de f(0.8) con polinomio de grado 3 es:", poly3(0.8))
