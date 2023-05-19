import numpy as np
import matplotlib.pyplot as plt

def euler_method(dt, t_final, i_initial):
    t = np.arange(0, t_final, dt)
    i = np.zeros_like(t)
    i[0] = i_initial

    for n in range(1, len(t)):
        di = -1.5 * i[n-1] * dt
        i[n] = i[n-1] + di

    return t, i

dt = 0.1
t_final = 5
i_initial = 0.5

t, i = euler_method(dt, t_final, i_initial)

plt.plot(t, i)
plt.xlabel('Tiempo')
plt.ylabel('Corriente')
plt.title('Evolución de la corriente en un circuito RL')
plt.grid(True)
plt.show()
