import numpy as np
import matplotlib.pyplot as plt

#creamos los puntos por los que debe de pasar la grafica
x=np.linspace(0,1,11)
y= 1/((x-0.3)**2+0.01) + 1/((x-0.9)**2+0.04) - 6

#definimos variables, vector de terminos independientes y matriz
s=len(x)-1
n=3*s-1
p=len(x)
#print(s)
#print(p)
mat=np.zeros((n,n))
vector=np.zeros(n)
k=3
m=1

#llenamos la matriz con las ecuaciones de subindices iguales
for i in range(s):
    mat[i,3*i]=x[i+1]
    mat[i,3*i+1]=1
    if i!=0:
      mat[i, 3*i-1]=(x[i+1])**2
    vector[i]=y[i+1]

#llenamos la matriz con subindices diferentes 
for j in range (s,(2*s-1)):      
  mat [j,k]=x[m]
  mat [j,k-1]=(x[m])**2
  mat [j,k+1]=1
  k=k+3
  m=m+1
  vector[j]=y[j-(s-1)]

#llenamos la matriz con las ecuaciones de suavidad (las derivadas)
r=0
u=1
for e in range ((2*s-1),n-1):
    mat [e, 3*r]=1
    mat [e, 3*r+2]=-2*x[u]
    mat [e, 3*r+3]=-1
    if r!=0:
       mat [e, 3*r-1]=2*x[u]
    r=r+1
    u=u+1

#llenamos la ultima fila de la matriz, y la ultima posicion del vector
mat[n-1, 1]=1
mat[n-1, 0]=x[0]
vector[n-1]=y[0]

# print(mat)
#resolvemos el vector de incognitas
sol=np.linalg.solve(mat,vector)

#creamos 3 vectores para almacenar los datos desde (a_2) hasta (c_10)
vec_a=np.zeros(s)
vec_b=np.zeros(s)
vec_c=np.zeros(s)

#llenamos los vectores
for i in range (s):
   vec_b[i]=sol[3*i]
   vec_c[i]=sol[3*i+1]

for i in range (1,s):
   vec_a[i]=sol[3*i-1]

#print (vec_b, "vector de b")
#print (vec_c, "vector de c")
#print (vec_a, "vector de a")

#creamos dos listas una para almacenar los valores de x,y obtenidos de la interpolacion
lista_x=[]
lista_y=[]

#llenamos las listas
for w in range(s): 
   x_dat=np.arange(x[w],x[w+1]+0.01,0.01)
   lista_x.append(x_dat)
#print(lista_x)

for i in range(s):
   y_dat=vec_a[i]*(lista_x[i])**2 + vec_b[i]*lista_x[i] + vec_c[i]
   lista_y.append(y_dat)
#print(lista_y)

#graficamos la interpolacion con las listas anteriormente creadas
for i in range(len(x_dat)):
   plt.plot(lista_x[i-1],lista_y[i-1],label="interpolacion")  

#grafica de la funcion analitica
x_dato = np.linspace(0, 1, 100)
y_dato = 1/((x_dato-0.3)**2+(0.01)) + 1/((x_dato-0.9)**2+(0.04)) - 6
plt.plot(x_dato,y_dato,'--',label="solucion analitica")
plt.plot(x,y,'o',label="puntos")
plt.show()

