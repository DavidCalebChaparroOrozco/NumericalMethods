import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def heat_equations(t, T):
    k = 0.075
    C = 10
    T_f = 20
    return -k * (T - T_f) / C

teval = np.linspace(0,1800, 1000)

sol = solve_ivp(heat_equations, (teval[0], teval[-1]), (30,), t_eval=teval)

fig, ax = plt.subplots()
ax.plot(sol.t, sol.y[0, :], "-k", ms=3, label="Scipy Runge-Kutta")

ax.set_ylabel("Temperature", fontsize=18)
ax.set_xlabel("Time", fontsize=18)
plt.legend()
plt.show()