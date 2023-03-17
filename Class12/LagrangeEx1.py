import numpy as np
import MetInterpolacion as mi
import matplotlib.pyplot as plt

x_data = np.array([[1],[4],[5],[6]])
y_data = np.array([[0],[1.3862],[1.6094],[1.7917]])
# x = np.array([[0],[1],[2],[3]])
x = np.arange(1,40,0.1)
# x = [2]

# mi(x=x,xdat= x_data, ydat=y_data)

y = mi.interp_lagrange(x=x,xdat= x_data, ydat=y_data)

print(y)

plt.plot(y,"--",marker="o",label="Interpolacion")
plt.show()