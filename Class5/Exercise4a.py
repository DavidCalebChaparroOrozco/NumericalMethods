import numpy as np
import matplotlib.pyplot as plt

def cos_taylor(x, n):
    """Calculate the Taylor polynomial of degree n for the function cos(x) centered at x=0."""
    result = 0
    for i in range(n+1):
        result += ((-1)**i / np.math.factorial(2*i)) * x**(2*i)
    return result

# Define the range of values of x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Adjust figure size
plt.figure(figsize=(8, 6))

# Graph the function cos(x) 
plt.plot(x, np.cos(x), label='cos(x)')

# Graphing Taylor polynomials of degree 0 to 5
for n in range(6):
    plt.plot(x, cos_taylor(x, n), label=f'P{n}(x)')

# Add legend
plt.legend()

# Show graph
plt.show()



# # Internet
# import numpy as np
# import matplotlib.pyplot as plt

# a = 0
# def f(x):
#     return np.cos(x)
# def taylor(x, n):
#     return np.sum([f(a) * (x - a)**k / np.math.factorial(k) for k in range(n+1)])

# x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
# y = f(x)

# fig, ax = plt.subplots(figsize=(8, 6))
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.tick_params(axis='both', which='major', width=2, length=5)
# ax.tick_params(axis='both', which='minor', width=1, length=3)

# ax.plot(x, y, linewidth=2, color='blue', label='cos(x)')

# for n in range(6):
#     p = [f(a) / np.math.factorial(k) * (x - a)**k for k in range(n+1)]
#     polynomial = np.sum(p, axis=0)
#     ax.plot(x, polynomial, linestyle='--', linewidth=2, label=f'P{n}(x)')

# ax.set_xlabel('x', fontsize=14)
# ax.set_ylabel('y', fontsize=14)
# ax.set_title('Taylor polynomials of cos(x)', fontsize=16)
# ax.legend()

# plt.show()
