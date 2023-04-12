import numpy as np

a = 0
x = np.linspace(-np.pi, np.pi, 100)

def f(x):
    return np.cos(x)

def g(x):
    return np.log(x)

def taylor(f, a, x, n):
    taylor_sum = 0
    for k in range(n+1):
        taylor_sum += (f(a) * (x-a)**k) / np.math.factorial(k)
        f_d = np.polyder(np.poly1d(f), k+1)
        f_d_a = f_d(a)
        taylor_sum += (f_d_a * (x-a)**(k+1)) / np.math.factorial(k+1)
    return taylor_sum

# Error relativo porcentual de cada aproximación de cos(x)
for n in range(1, 6):
    P_n = taylor(f, a, x, n)
    error = np.abs((f(x) - P_n) / f(x)) * 100
    print(f"Error relativo porcentual de P_{n}(x) para cos(x):")
    print(error)
    print("")

a = 1
x = np.linspace(0.1, 0.01, 10)

# Error relativo porcentual de cada aproximación de ln(x)
for n in range(1, 6):
    P_n = taylor(g, a, x, n)
    error = np.abs((g(x) - P_n) / g(x)) * 100
    print(f"Error relativo porcentual de P_{n}(x) para ln(x):")
    print(error)
