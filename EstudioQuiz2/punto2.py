import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x,y) = dy/dx
def f(x, y):
    return (1 + 4*x) * np.sqrt(y)

# Definir el intervalo de x y el tamaño de paso h
x0, xf = 0, 1
h = 0.25

# Definir la condición inicial y0
y0 = 1

# Solución analítica
x = np.linspace(x0, xf, 100)
y_analitica = ((2/9) * (1 + 4*x)**2)**2

# Método de Euler con h = 0.5 y 0.25
def euler(f, x0, y0, xf, h):
    n = int((xf - x0)/h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
    
    return x, y

x_euler1, y_euler1 = euler(f, x0, y0, xf, h=0.5)
x_euler2, y_euler2 = euler(f, x0, y0, xf, h=0.25)

# Método de punto medio con h = 0.5
def punto_medio(f, x0, y0, xf, h):
    n = int((xf - x0)/h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + (h/2) * k1)
        y[i+1] = y[i] + h * k2
    
    return x, y

x_pmedio, y_pmedio = punto_medio(f, x0, y0, xf, h=0.5)

# Método de la serie de Taylor de orden 3
def taylor3(f, f1, f2, x0, y0, xf, h):
    n = int((xf - x0)/h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i]) + (h**2/2) * f1(x[i], y[i]) + (h**3/6) * f2(x[i], y[i])
    
    return x, y

# Definir las funciones f', f'' necesarias para el método de Taylor de orden 3
def f1(x, y):
    return (2 + 8*x) * np.sqrt(y)

def f2(x, y):
    return (-2/np.sqrt(y)) * (1 + 4*x) * (1 + 8*x)

x_taylor3, y_taylor3 = taylor3(f, f1, f2, x0, y0, xf, h=0.25)

# Graficar los resultados
plt.plot(x,y_analitica, label='Solución analítica')
plt.plot(x_euler1, y_euler1, 'o-', label='Euler h=0.5')
plt.plot(x_euler2, y_euler2, 'o-', label='Euler h=0.25')
plt.plot(x_pmedio, y_pmedio, 'o-', label='Punto medio h=0.5')
plt.plot(x_taylor3, y_taylor3, 'o-', label='Taylor orden 3 h=0.25')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
