import numpy as np
import matplotlib.pyplot as plt

# Define la función y su serie de Taylor alrededor de a=2
def f(x):
    return 3*x**5 - 2*x**4 + 15*x**3 + 13*x**2 - 12*x - 5

def taylor(x, a, grado):
    resultado = 0
    for n in range(grado+1):
        resultado += f(a)*(x-a)**n / np.math.factorial(n)
        a_derivada = sum([f(a)*(np.math.factorial(k)/np.math.factorial(k-n))*(a-x)**(k-n) for k in range(n, grado+1)])
        resultado += a_derivada*(x-a)**n / np.math.factorial(n+1)
    return resultado

# Grafica la función y los polinomios de Taylor de grado 0 a 5
a = 2
x = np.linspace(0, 4, 100)
y = f(x)
taylor_0 = taylor(x, a, 0)
taylor_1 = taylor(x, a, 1)
taylor_2 = taylor(x, a, 2)
taylor_3 = taylor(x, a, 3)
taylor_4 = taylor(x, a, 4)
taylor_5 = taylor(x, a, 5)

plt.plot(x, y, label='3x^5 - 2x^4 + 15x^3 + 13x^2 - 12x - 5')
plt.plot(x, taylor_0, label='Grado 0')
plt.plot(x, taylor_1, label='Grado 1')
plt.plot(x, taylor_2, label='Grado 2')
plt.plot(x, taylor_3, label='Grado 3')
plt.plot(x, taylor_4, label='Grado 4')
plt.plot(x, taylor_5, label='Grado 5')

plt.legend()
plt.show()
