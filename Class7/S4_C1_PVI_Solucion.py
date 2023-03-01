'''
Código construido para solucionar un PVIs conformado por una EDO de primer orden de la forma y'=fld(t,y) y condiciones iniciales y(t_0)=y_0.
TAREA: Agregar líneas comentadas que faciliten la comprensión del código.
'''

import numpy as np
import pvi_methods as pvim
import matplotlib.pyplot as plt

# Definición de la función f (lado derecho de la EDO)
def fld(t, y):
    return y

# Solución analítica del PVI
def fanalit(t):
    y = np.exp(t)
    return y

# Información de entrada
# Condiciones iniciales
t_0 = 0.
y_0 = 1.
# Punto final del intervalo de solución
T = 2.
# Tamaño de paso
hp = 0.2

# Calculo del número de pasos (ó número de iteraciones)
nit = int((T - t_0)/hp)

# Solución con el método de Euler
teu, yeu = pvim.euler_meth(fld,t_0,y_0,nit,hp)
the, yhe = pvim.heun_meth(fld,t_0,y_0,nit,hp)
tptom, yptom = pvim.ptomed_meth(fld,t_0,y_0,nit,hp)

# Valores de t para construir la gráfica de la solución analítica
t_v = np.linspace(t_0,T,100)

print(yhe)

# Gráfica con las soluciones obtenidas
plt.plot(t_v, fanalit(t_v),label='Solución analítica')
plt.plot(teu, yeu,'o',label='Método de Euler')
plt.plot(the, yhe,'*',label='Método de Heun')
plt.plot(tptom, yptom,'--',label='Método de Punto Medio')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Soluciones numéricas del PVI planteado')
plt.show()