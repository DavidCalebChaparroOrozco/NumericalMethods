import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y * np.sin(3*x)  # EDO a resolver: y' = y*sin(3x)

x0, xf = 0, 1  # Intervalo de x
y0 = 1  # Condición inicial
h = 0.1  # Tamaño de paso

def rk4(f, x0, y0, xf, h):
    n = int((xf - x0)/h)  # Número de pasos
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    
    return x, y

x_rk4, y_rk4 = rk4(f, x0, y0, xf, h)

plt.plot(x_rk4, y_rk4, label='RK4')
plt.legend()
plt.show()
