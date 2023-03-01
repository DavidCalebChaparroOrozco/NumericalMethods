'''
TAREAS: 
1. Escribir un encabezado para el módulo en el que se indiquen las funciones que contiene y el tipo de problemas que resuelven. Asegúrese de incluir el aspecto o los aspectos que tienen en común las funciones para ser incluidas en un mismo módulo.
2. Agregar líneas comentadas que faciliten la comprensión del código.
3. Agregar una función por cada método estudiado en clase y que no haya sido incluido en este módulo.
'''

import numpy as np

def euler_meth(fld,t0,y0,n,h):
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        y[i+1] = y[i] + h*fld(t[i], y[i])
        t[i+1] = t[i] + h
    return t,y

def heun_meth(fld,t0,y0,n,h):
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        yaux = y[i] + h*fld(t[i], y[i])
        t[i+1] = t[i] + h
        pend = (fld(t[i], y[i]) + fld(t[i+1], yaux))/2.0
        y[i+1] = y[i] + h*pend
    return t,y

def ptomed_meth(fld,t0,y0,n,h):
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        yaux = y[i] + h*fld(t[i], y[i])/2.0
        taux = t[i] + 0.5*h
        y[i+1] = y[i] + h*fld(taux, yaux)
        t[i+1] = t[i] + h
    return t,y