import numpy as np
import matplotlib.pyplot as plt

def log_taylor(x, n):
    """Calculate the Taylor polynomial of degree n for the function log(x) centered at x=0."""
    result = 0
    for i in range(n+1):
        result += ((-1)**i * (x-1)**(i+1)) / (i+1)
    return result
# Generate data
x = np.linspace(0, 1, 10)
y = np.log(x)

# Adjust figure size
plt.figure(figsize=(8, 6))

# Graph the function log(x) 
plt.plot(x, y, label='log(x)')
for i in range(6):
    plt.plot(x, log_taylor(x, i), label=f'P{i}(x)')
# Add legend
plt.legend()
# Show graph
plt.show()
