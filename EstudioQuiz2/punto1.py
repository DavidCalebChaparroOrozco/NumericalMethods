import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación diferencial
def f(t, y):
    return y*t**3 - 1.1*y

# Definición de la solución analítica
def y_analytic(t):
    return np.exp(-0.55*t**2) * (2*t + 1)

# Definición de los métodos numéricos
def euler(f, t0, y0, h, tf):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(t.shape)
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
    return t, y

def heun(f, t0, y0, h, tf):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(t.shape)
    y[0] = y0
    for i in range(1, len(t)):
        k1 = f(t[i-1], y[i-1])
        k2 = f(t[i-1] + h, y[i-1] + h*k1)
        y[i] = y[i-1] + h/2 * (k1 + k2)
    return t, y

def midpoint(f, t0, y0, h, tf):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(t.shape)
    y[0] = y0
    for i in range(1, len(t)):
        k1 = f(t[i-1], y[i-1])
        k2 = f(t[i-1] + h/2, y[i-1] + h/2*k1)
        y[i] = y[i-1] + h * k2
    return t, y

def taylor3(f, df, d2f, d3f, t0, y0, h, tf):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(t.shape)
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h*f(t[i-1], y[i-1]) + h**2/2*df(t[i-1], y[i-1]) + \
                h**3/6*d2f(t[i-1], y[i-1]) + h**4/24*d3f(t[i-1], y[i-1])
    return t, y

# Definición de los parámetros iniciales
t0, y0, tf = 0, 1, 2
h1, h2 = 0.5, 0.25

# Cálculo de los resultados para cada método
t_analytic = np.linspace(t0, tf, 100)
y_analytic = y_analytic(t_analytic)

t_euler1, y_euler1 = euler(f, t0, y0, h1, tf)
t_euler2, y_euler2 = euler(f, t0, y0, h2, tf)

t_heun1, y_heun1 = heun(f, t0, y0, h1,tf)
t_midpoint1, y_midpoint1 = midpoint(f, t0, y0, h1, tf)

df = lambda t, y: y*t**3 - 1.1*y
d2f = lambda t, y: 3*y*t**2 - 1.1*df(t, y)
d3f = lambda t, y: 6*y*t - 3*df(t, y) - 1.1*d2f(t, y)

t_taylor3, y_taylor3 = taylor3(f, df, d2f, d3f, t0, y0, h1, tf)

# Graficar los resultados

plt.plot(t_analytic, y_analytic, label='Solución analítica')
plt.plot(t_euler1, y_euler1, '-o', label='Método de Euler, h=0.5')
plt.plot(t_euler2, y_euler2, '-o', label='Método de Euler, h=0.25')
plt.plot(t_heun1, y_heun1, '-o', label='Método de Heun, h=0.5')
plt.plot(t_midpoint1, y_midpoint1, '-o', label='Método del punto medio, h=0.5')
plt.plot(t_taylor3, y_taylor3, '-o', label='Método de la serie de Taylor, orden 3')

plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()