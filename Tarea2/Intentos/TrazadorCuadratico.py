import numpy as np
import matplotlib.pyplot as plt

x_dat = [-1,-0.5,0,0.5,1]
y_dat =[0.03846154,0.13793103,1.,0.13793103,0.03846154]

#Definición de variables
n=len(x_dat)-1
m= 3*n-1
jump=3
move=1

matriz = np.zeros((m,m))
vector = np.zeros(m)

"Llenamos las matriz con las ecuaciones con subindices semejantes"
for i in range(n):
    matriz[i,3*i]= x_dat[i+1]
    matriz[i,3*i+1]= 1.
    if i!=0:
        matriz[i,3*i-1]=(x_dat[i+1])**2
    vector[i]=y_dat[i+1]

"Ahora llenamos la matriz con las ecuaciones con subindices diferentes"
for i in range(n,(2*n-1)):
    matriz[i,jump]=x_dat[move]
    matriz[i,jump-1]=(x_dat[move])**2
    matriz[i,jump+1]=1
    jump=jump+3
    move=move+1
    vector[i]= y_dat[i-(n-1)]

"llenamos la matriz con ecuaciones de suavidad"
j=0
k=1
for i in range(2*n-1,n-1):
    matriz[i,3*j]=1
    matriz[i,3*j+2]=2*x_dat[k]
    matriz[i,3*j+3]=-1
    if j!=0:
        matriz[i,3*j-1]=2*x_dat[k]
    j=j+1
    k=k+1

"llenamos la ultima fila de la matriz y la ultima posicion del vector"
matriz[m-1,1]=1
matriz[m-1,0]= x_dat[0]
vector[m-1]=y_dat[0]

# solucion = np.linalg.solve(matriz,vector)

print(matriz)
print(vector)
# print(solucion)