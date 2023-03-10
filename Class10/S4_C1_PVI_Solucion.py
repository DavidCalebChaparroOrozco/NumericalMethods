'''
Código construido para solucionar un PVIs conformado por una EDO de primer orden de la forma y'=fld(t,y) y condiciones iniciales y(t_0)=y_0.
TAREA: Agregar líneas comentadas que faciliten la comprensión del código.
'''

import numpy as np
import pvi_methods as pvim
import matplotlib.pyplot as plt

# Definición de la función f (lado derecho de la EDO)
def fld(t, y_1,y_2):
    return y_2

def fld2(t, y_1, y_2):
    return -0.6*y_2 -8*y_1

# Solución analítica del PVI
def fanalit(t):
    y = np.exp(t)
    return y

# Información de entrada
# Condiciones iniciales
t_0 = 0.
y_0 = 4.
y_1 = 0
y_2 = 0
# Punto final del intervalo de solución
T = 5.
# Tamaño de paso
hp = 0.5

# Calculo del número de pasos (ó número de iteraciones)
nit = int((T - t_0)/hp)

# Solución con el método de Euler
# fld,fld2,t0,y0,y1,y2,n,h
t, y1,y2 = pvim.euler_meth_2(fld,fld2,t_0,y_1,y_2,nit,hp)
# the, yhe = pvim.heun_meth2(fld,fld2,t_0,y_0,y_1,y_2,nit,hp)
# tptom, yptom = pvim.ptomed_meth2(fld,fld2,t_0,y_0,y_1,y_2,nit,hp)

plt.plot(t, y1,'o', label='Method Euler')
plt.plot(t,y2,'-')

# teu, yeu = pvim.euler_meth(fld2,t_0,y_1,nit,hp)
# the, yhe = pvim.heun_meth(fld2,t_0,y_1,nit,hp)
# tptom, yptom = pvim.ptomed_meth(fld2,t_0,y_1,nit,hp)

# Valores de t para construir la gráfica de la solución analítica
t_v = np.linspace(t_0,T,100)
print(t,y2,'-')

# Gráfica con las soluciones obtenidas
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Soluciones numéricas del PVI planteado')
plt.show()