#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:26:00 2023

@author: ab
"""

import numpy as np
import matplotlib.pylab as plt

x0=1.0
L=2.0

n=100

x=np.linspace(x0,L,n)
c=0.1

h=10.
B=0.02
W=0.2

P=2*B+2*W
Ac=B*W

k=20.

m=np.sqrt(h*P/k/Ac)

thb=0.
thl=0.638961

def fmq(r,c):
    f=np.sqrt(r**2+c**2)
    return f

def d2fmq(r,c):
    f=1./fmq(r,c)-r**2/fmq(r,c)**3
    return f

def d1xfmq(r,dx,c):
    f=dx/fmq(r,c)
    return f

psi=np.zeros((n,n))
A=np.zeros((n,n))
B=np.zeros(n)
for i in range(n):
    xi=x[i]
    for j in range(n):
        ej=x[j]
        #r=np.sqrt(np.dot(xi-ej,xi-ej)) # 2-3 D
        r=np.abs(xi-ej) #1-D
        psi[i,j]=fmq(r,c)
        if i==0:
            A[i,j]=fmq(r,c)    
        elif i==n-1:
            A[i,j]=fmq(r,c)
        else:
            A[i,j]=xi**2*d2fmq(r,c)+xi*d1xfmq(r,xi-ej,c)+fmq(r,c)
            
    if i==0:
        B[i]=thb
    elif i==n-1:
        B[i]=thl
    else:
        B[i]=0.0
alpha=np.linalg.solve(A,B)
th=np.matmul(psi,alpha)

#tha=thb*np.exp(-m*x)
tha=np.sin(np.log(x))
er=np.abs(tha-th)

el2=np.sqrt(np.dot(er,er))
print(el2)

plt.figure()
plt.plot(x,th,'b.',label='Númerica')
plt.plot(x,tha,label='Analítica')
plt.xlabel('x[m]')
plt.ylabel('th[°C]')
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x,er,'--.',label='Númerica')
plt.xlabel('x[m]')
plt.ylabel('error[°C]')
plt.legend()
plt.show()



