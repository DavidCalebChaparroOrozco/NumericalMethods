#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:30:48 2023

@author: usuario
"""

#caso RBF basico para varias posiciones 

#librerias 
import numpy as np #libreria para manejo de arreglos
import matplotlib.pylab as plt #libreria para graficacion

#crear un dominio
xm=1.0 #flotante definicion implicita
n=20 #nodos

#vector de referencia
x=np.linspace(-xm,xm,n)

c=1 #parametro de forma
m=1

#multicuadrica funcion base radial
def mq(r,c):
    f=np.sqrt(r**2+c**2)
    return f

r=np.abs(x) #vector r en una 1d
fmq=mq(r,c) #vector al evaluar la multicuadrica

#grafico
#observamos grafico monotono
#que pasa con el parametro forma
#suaviza o forma de manera cónica la funcion
# se puede ver simetria radial
# como continuo esta funcion es diferenciable

plt.figure(1)
plt.plot(x,fmq)
plt.xlabel('x')
plt.ylabel('y')
plt.show()



