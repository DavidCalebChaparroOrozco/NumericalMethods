import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 1, 10)
y = np.sin(x)

# Adjust figure size
plt.figure(figsize=(8, 6))

# Graph the function sin(x) 
plt.plot(x, y, label='sin(x)')

# Add legend
plt.legend()

# Show graph
plt.show()


# # Internet
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)

# fig, ax = plt.subplots(figsize=(8, 6))
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# ax.tick_params(axis='both', which='major', width=2, length=5)
# ax.tick_params(axis='both', which='minor', width=1, length=3)

# ax.plot(x, y, linewidth=2, color='blue', label='sin(x)')


# for n in [1, 3, 5]:
#     p = np.polyfit(x, y, n)
#     f = np.poly1d(p)
#     ax.plot(x, f(x), linestyle='--', linewidth=2, label=f'P{n}(x)')

# ax.set_xlabel('x', fontsize=14)
# ax.set_ylabel('y', fontsize=14)
# ax.set_title('Taylor polynomials of sin(x)', fontsize=16)
# ax.legend()

# plt.show()