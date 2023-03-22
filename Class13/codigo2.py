#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:30:48 2023

@author: usuario
"""

#caso RBF basico

#librerias 
import numpy as np
import matplotlib.pylab as plt

#crear un dominio
xm=1.0 #flotante definicion implicita
n=50 #nodos

#vector de referencia
x=np.linspace(-xm,xm,n)

#c=1 #parametro de forma
nc=5
c=np.linspace(0,1,nc)
m=1

#multicuadrica
def mq(r,c):
    f=np.sqrt(r**2+c**2)
    return f

r=np.abs(x) #vector r

#grafico
plt.figure(1)
for i in range(nc):
    fmq=mq(r,c[i])
    texto=str(c[i])
    plt.plot(x,fmq,label=texto)

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="best")
plt.show()



