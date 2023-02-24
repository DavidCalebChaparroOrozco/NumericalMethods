import numpy as np
import matplotlib.pyplot as plt

a = 2

# Definition function(x)
def f(x):
    return 3*x**5 - 2*x**4 + 15*x**3 + 13*x**2 - 12*x - 5

# Function of taylor
def taylor(x, n):
    taylor_sum = 0
    for k in range(n+1):
        taylor_sum += (f(a) * (x-a)**k) / np.math.factorial(k)
        f_d = np.polyder(np.poly1d(f), k+1)
        f_d_a = f_d(a)
        taylor_sum += (f_d_a * (x-a)**(k+1)) / np.math.factorial(k+1)
    return taylor_sum

# Generate data
x = np.linspace(-10, 10, 100)
y = f(x)

# Adjust the size and style of the figure
fig, ax = plt.subplots(figsize=(8, 6))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.tick_params(axis='both', which='major', width=2, length=5)
ax.tick_params(axis='both', which='minor', width=1, length=3)

# Graph function
ax.plot(x, y, linewidth=2, color='blue', label='f(x)')

# Graph Taylor polynomials from degree 0 to 5
for n in range(6):
    t = [taylor(i, n) for i in x]
    ax.plot(x, t, linestyle='--', linewidth=2, label=f'P{n}(x)')

# Add labels and legend
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Taylor polynomials of function f(x)', fontsize=16)
ax.legend()

# Show the graph
plt.show()
