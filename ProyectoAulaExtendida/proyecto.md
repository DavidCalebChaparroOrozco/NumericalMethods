$y(x) ≈ ∑_{i=1}^{10} c_i e^{-(\frac{r_i}{c})}$

donde $c_i$ son los coeficientes desconocidos que debemos determinar y $r_i$ es la distancia euclidiana entre x y el punto de colocación $x_i$, es decir,

$r_i = |x - x_i|$

Derivación de las funciones de base radial:
Para encontrar los coeficientes $c_i$, necesitamos resolver un sistema de ecuaciones lineales que surge al imponer las condiciones de frontera y la ecuación diferencial en los puntos de colocación. Para hacerlo, primero necesitamos derivar la función de base radial gaussiana con respecto a x.

Podemos calcular la derivada de la función de base radial gaussiana $e^{-(\frac{r}{c})}$ con respecto a x como sigue:

$\frac{\partial}{\partial x} e^{-(\frac{r}{c})} = -\frac{1}{c} e^{-(\frac{r}{c})}$

Utilizando la definición de r, tenemos:

$\frac{\partial r}{\partial x} = \frac{x - x_i}{r_i}$

Entonces, podemos escribir la derivada de la función de base radial como:

$\frac{\partial}{\partial x} e^{-(\frac{r}{c})} = -\frac{1}{c} \frac{x - x_i}{r_i} e^{-(\frac{r}{c})}$

${e^{-(\frac{r}{c})}}'' = \frac{e^{-\frac{r}{c}}}{c^2}$

Imposición de condiciones de frontera y la ecuación diferencial:
Ahora podemos imponer la ecuación diferencial y las condiciones de frontera en los puntos de colocación y escribir las ecuaciones resultantes en forma matricial. Esto nos da un sistema de ecuaciones lineales para los coeficientes $c_i$.

En particular, para cada punto de colocación $x_i$, podemos imponer la ecuación diferencial y obtener:

$y_i'' + 2y_i' + y_i = 0$

Reemplazando la aproximación de la solución $y(x) ≈ ∑_{i=1}^{10} c_i e^{-(\frac{r_i}{c})}$ y sus derivadas en la ecuación anterior en el punto $x_i$, se tiene:

$\sum_{j=1}^{10} c_j \left( -\frac{1}{c} \frac{x_i - x_j}{r_{ij}} \right) e^{-(\frac{r_{ij}}{c})} + 2\sum_{j=1}^{10} c_j \left( -\frac{1}{c} \frac{x_i - x_j}{r_{ij}} \right) e^{-(\frac{r_{ij}}{c})} + \sum_{j=1}^{10} c_j e^{-(\frac{r_{ij}}{c})} = 0$

Simplificando y reorganizando los términos, se tiene:

$\sum_{j=1}^{10} e^{-(\frac{r_{ij}}{c})} \left[ -\frac{1}{c} \frac{x_i - x_j}{r_{ij}} c_j + 2\left( -\frac{1}{c} \frac{x_i - x_j}{r_{ij}} \right) c_j + c_j \right] = 0$

$\sum_{j=1}^{10} e^{-(\frac{r_{ij}}{c})} \left[ \frac{2}{c} - \frac{x_i - x_j}{r_{ij}} \right] c_j = 0$

Esto da un sistema lineal de 10 ecuaciones para los 10 coeficientes $c_i$ que podemos escribir en forma matricial como:

$A\vec{c} = \vec{b}$

Donde $A$ es la matriz de coeficientes que depende de las posiciones de colocación $x_i$, $\vec{c}$ es el vector de coeficientes desconocidos y $\vec{b}$ es el vector de términos independientes que depende de las condiciones de frontera.

Resolviendo el sistema lineal:
Podemos resolver el sistema lineal utilizando cualquier método de solución de sistemas lineales, como la eliminación gaussiana o la descomposición LU. Una vez que hemos determinado los coeficientes $c_i$, podemos utilizar la aproximación de la solución $y(x) ≈ ∑_{i=1}^{10} c_i e^{-(\frac{r_i}{c})}$ para evaluar la solución aproximada en cualquier punto $x$ en el intervalo de interés.


Para resolver el sistema lineal $A\vec{c} = \vec{b}$, primero necesitamos construir la matriz $A$ y el vector $\vec{b}$.

Para construir la matriz $A$, necesitamos calcular las distancias euclidianas entre cada par de puntos de colocación $x_i$ y $x_j$, lo cual nos dará los valores de $r_{ij}$. Luego, podemos calcular los elementos de la matriz $A$ utilizando la fórmula anterior:

$A_{ij} = e^{-(\frac{r_{ij}}{c})} \left[ \frac{2}{c} - \frac{x_i - x_j}{r_{ij}} \right]$

Para construir el vector $\vec{b}$, podemos utilizar las condiciones de frontera $y(0) = 0$ y $y(1) = 1$:

$\begin{cases} y(0) = c_1 e^{-(\frac{r_1}{c})} + c_2 e^{-(\frac{r_2}{c})} + \dots + c_{10} e^{-(\frac{r_{10}}{c})} = 0 \ y(1) = c_1 e^{-(\frac{r_1}{c})} + c_2 e^{-(\frac{r_2}{c})} + \dots + c_{10} e^{-(\frac{r_{10}}{c})} = 1 \end{cases}$

Esto nos da un sistema de dos ecuaciones lineales en los coeficientes $c_i$, que podemos escribir en forma matricial como:

$\begin{bmatrix} e^{-(\frac{r_1}{c})} & e^{-(\frac{r_2}{c})} & \dots & e^{-(\frac{r_{10}}{c})} \ e^{-(\frac{r_1}{c})} & e^{-(\frac{r_2}{c})} & \dots & e^{-(\frac{r_{10}}{c})} \end{bmatrix} \begin{bmatrix} c_1 \ c_2 \ \vdots \ c_{10} \end{bmatrix} = \begin{bmatrix} 0 \ 1 \end{bmatrix}$

Podemos resolver este sistema de ecuaciones lineales utilizando cualquier método de solución de sistemas lineales, como la eliminación gaussiana o la descomposición LU.

Una vez que hemos determinado los coeficientes $c_i$, podemos utilizar la aproximación de la solución $y(x) ≈ ∑_{i=1}^{10} c_i e^{-(\frac{r_i}{c})}$ para evaluar la solución aproximada en cualquier punto $x$ en el intervalo de interés.
---

Para resolver la matriz, podemos usar la descomposición LU. Primero, necesitamos encontrar las matrices L y U.

Comenzamos dividiendo la primera fila por el primer elemento:

$\begin{align*}
\begin{bmatrix}
1 & e^{-1} \
e^{1} & 1
\end{bmatrix}
&\to
\begin{bmatrix}
1 & e^{-1} \
0 & 1 - \frac{1}{e}
\end{bmatrix}
\end{align*}$

Entonces, nuestra matriz U es:

$\begin{align*}
U =
\begin{bmatrix}
1 & e^{-1} \
0 & 1 - \frac{1}{e}
\end{bmatrix}
\end{align*}$

Ahora, encontramos la matriz L. Para hacerlo, necesitamos encontrar los factores por los cuales multiplicamos las filas de la matriz U para obtener la matriz original. Comenzamos dividiendo la segunda fila por el elemento (1 - 1/e):
$
\begin{align*}
\begin{bmatrix}
1 & e^{-1} \
0 & 1 - \frac{1}{e}
\end{bmatrix}
&\to
\begin{bmatrix}
1 & e^{-1} \
0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 \
e^{1} & 1
\end{bmatrix}
\end{align*}$

Entonces, nuestra matriz L es:
$
\begin{align*}
L =
\begin{bmatrix}
1 & 0 \
e^{1} & 1
\end{bmatrix}
\end{align*}$

Verificamos que L*U es igual a la matriz original:
$\begin{align*}
L*U =
\begin{bmatrix}
1 & 0 \
e^{1} & 1
\end{bmatrix}
\begin{bmatrix}
1 & e^{-1} \
0 & 1 - \frac{1}{e}
\end{bmatrix}

\begin{bmatrix}
1 & e^{-1} \
e^{1} & 1
\end{bmatrix}
\end{align*}$

Por lo tanto, la descomposición LU de la matriz es:
$
\begin{align*}
\begin{bmatrix}
1 & e^{-1} \
e^{1} & 1
\end{bmatrix} =
\begin{bmatrix}
1 & 0 \
e^{1} & 1
\end{bmatrix}
\begin{bmatrix}
1 & e^{-1} \
0 & 1 - \frac{1}{e}
\end{bmatrix}
\end{align*}$