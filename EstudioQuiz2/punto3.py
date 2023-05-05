import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(t,y) = dy/dt
def f(t, y):
    return y * np.sin(t)**3

# Definir el intervalo de t y el tamaño de paso h
t0, tf = 0, 3
h = 0.1

# Definir la condición inicial y0
y0 = 1

# Método de Heun
def heun(f, t0, y0, tf, h):
    n = int((tf - t0)/h)
    t = np.linspace(t0, tf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i+1], y[i] + h*k1)
        y[i+1] = y[i] + (h/2) * (k1 + k2)
    
    return t, y

# Método de Punto medio
def punto_medio(f, t0, y0, tf, h):
    n = int((tf - t0)/h)
    t = np.linspace(t0, tf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/2, y[i] + (h/2) * k1)
        y[i+1] = y[i] + h * k2
    
    return t, y

# Solución analítica
t = np.linspace(t0, tf, 100)
y_analitica = np.exp((1-np.cos(t)**4)/4)

# Obtener las soluciones numéricas
t_heun, y_heun = heun(f, t0, y0, tf, h)
t_pmedio, y_pmedio = punto_medio(f, t0, y0, tf, h)

# Graficar los resultados
plt.plot(t, y_analitica, label='Solución analítica')
plt.plot(t_heun, y_heun, 'o-', label='Heun')
plt.plot(t_pmedio, y_pmedio, 'x-', label='Punto medio')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()
