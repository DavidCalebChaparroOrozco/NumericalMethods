import numpy as np
import matplotlib.pyplot as plt

def cos_taylor(x, n):
    """Calculate the Taylor polynomial of degree n for the function cos(x) centered at x=0."""
    result = 0
    for i in range(n+1):
        result += ((-1)**i / np.math.factorial(2*i)) * x**(2*i)
    return result

# Define the range of values of x
x = np.linspace(-np.pi, 1 , 10)

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

# def cos_taylor(x, n):
#     """Calculate the Taylor polynomial of degree n for the function cos(x) centered at x=0."""
#     result = 0
#     for i in range(n+1):
#         result += ((-1)**i * (x-1)**(i+1)) / (i+1)
#     return result
# # Generate data
# x = np.linspace(0, 1, 10)
# y = np.cos(x)

# # Adjust figure size
# plt.figure(figsize=(8, 6))

# # Graph the function cos(x) 
# plt.plot(x, y, label='cos(x)')
# for i in range(6):
#     plt.plot(x, cos_taylor(x, i), label=f'Polinomio de Taylor de grado {i}')
# # Add legend
# plt.legend()

# # Show graph
# plt.show()