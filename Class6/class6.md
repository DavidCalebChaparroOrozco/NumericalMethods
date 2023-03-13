# Problemas con Valores Iniciales

## Conceptos basicos
Una ecuación diferencial (ED) es una ecuación que contiene las derivadas de una función desconocida
, $u$. El _orden_ de la ecuación diferencial es el orden de la mayor derivada en la ecuación.

$$m \frac{d^{2}u}{dt^{2}} + c \frac{du}{dt} + ku = 0$$

$$\frac{d^{2}u}{dt^{2}} + k sin(u) = sin(wt)$$

$$\frac{d^{2}u}{dx^{2}} + \frac{d^{2}u}{dy^{2}} + ku = 0$$

$$\frac{du}{dt} + u\frac{du}{dx} = 0 $$

Las variables _t_, _x_ y _y_ representan variables independientes.

Si _u_ es la función desconocida entonces, estructuralmente, cualquier ecuación diferencial tiene 
la forma $L(u) = F$,

Donde el lado izquierdo representa todas las expresiones de la ecuación que están en terminos de 
_u_ o que dependen de _u_ y sus derivadas. _F_ tipicamente es una función que solamente depende
de las variables independientes.

La función que aplica _L_ a _u_  se denomina operador.

$L: \text {Operador Diferencial}$

Una _solución_ de una ED es una función _u_ que cuando se sustituye en la ecuación genera una
identidad.

La ecuación diferencial $L(u) = F$ se denomina _lineal_ si el operador satisface 

$$L (\alpha u_1 + \beta u_2) = \alpha L (u_1) + \beta L (u_2)$$

donde _a_ y _B_ son escalares (coeficientes) y $u_1$ y $u_2$ son funciones. Una ED para cual _F_ es
igual a cero se denomina _homogenea_.

$m \frac{d^{2}u}{dt^{2}} + c \frac{du}{dt} + ku = 0$
---
$m \frac{d^{2}}{dt^{2}} + c \frac{d}{dt} + k = 0$

Lineal, homogenea.

$m \frac{d^{2}u}{dx^{2}} + k sin(u) = sin(wt)$
---
$m \frac{d^{2}}{dx^{2}} + k sin() = sin(wt)$

No lineal, no homogenea.

$m \frac{d^{2}u}{dx^{2}} + \frac{d^{2}u}{dy^{2}} + ku = 0$
---
$m \frac{d^{2}}{dx^{2}} + \frac{d^{2}}{dy^{2}} + k = 0$
Lineal, homogenea.

$m \frac{du}{dt} + u \frac{du}{dx} = 0$
---
$m \frac{d}{dt} +  \frac{d}{dx} = 0$
No lineal, homogenea.

Una _ED_ se denomina _Ecuación Diferencial Ordinaria (EDO)_ si la función desconocida depende de 
una sola variable independiente.

$$m \frac{d^{2}u}{dt^{2}} + c \frac{du}{dt} + ku = F(t)$$

La _ED_ modela un sistema de masa-resorte amortiguado. Aqui $u = u(t)$ representa desplazamiento de
la masa desde la posición de equilibrio como una función del tiempo,
_t_. $m>0$, $c\geq 0$ y $k>0$ son constantes que representan la masa, la constante del resorte.
$F(t)$ es una fuerza externa aplicada al sistema. Es de gran interés y utilidad resolver esta _ED_ 
considerando la pareja de condiciones iniciales.

$$u(0) = u_0 \text {y} \frac{du}{dt}(0) = {u}'_0,$$

que hacen referencia a la posición y velocidad iniciales de la masa. La _ED_ y las dos condiciones 
forman un _Problema con Valores Iniciales (PVI)_

La ecuación
$$\frac{d^{2}u}{dx^{2}} = - \frac{g}{c},$$

sujeta a las condiciones
$$u(0) = u(l) = 0 ,$$

modela la posición de equilibrio de una cuerda elástica de longitud _l_ que esta sujeta en sus 
extremos bajo la influencia de la gravedad. Aquí _x_ es la variable espacial que representa la 
posición de un punto sobre la cuerda y $u = u(x)$ representa el desplazamiento del punto en la 
posición _x_. La _EDO_ y las dos condiciones forman un _Problema con Valores en la Frontera (PVF)_.
En este caso,

$$L(\cdot ) = \frac{d^{2}}{dx^{2}}(\cdot ), F(x) = -\frac{g}{c}. $$

Una _Ecuación Diferencial Parcial (EDP)_ es una ecuación diferencial en la que la función desconocida
depende de más de una variable independiente.

Ecuación del calor:
$$u_{t} - \alpha ^{2} u_{xx} = F( x, t)$$

Ecuación de la onda:
$$u_{tt} - c ^{2} u_{xx} = F( x, t)$$

Ecuación de Laplace:
$$u_{xx} + u_{yy} = 0$$

Ecuación de Poisson:
$$u_{xx} + u_{yy} = F( x, t)$$

Ecuación de transporte:
$$u_{t} + cu_x = 0$$

Ecuación de Burger:
$$u_t + uu_x + yu_{xx} = 0 $$

Ecuación de Korteweg - deVries:
$$u_t + uu_x + u_{xxx} = 0$$

Ecuación de Sine - Gordon:
$$u_{tt} - u_{xx} + sin(u) = 0$$

Ecuación de superficie minimal:
$$\left ( 1 + u_{y}^{2} \right ) u_{xx} - 2u_xu_yu_{xy} + \left ( 1 + u_{x}^{2} \right ) u_{yy} = 0 $$

$t: \text {tiempo}$
 
$x, y: \text {variables especiales}$

# PVI
La solución numérica de una EDO es un conjunto de valores $y_{0}$,$y_{1}$,$y_{2}$...$y_{n}$ de la variable 
dependiente que corresponden a un conjunto de valores $x_{0}$,$x_{1}$,$x_{2}$...$x_n$ de la variable 
independiente y tales que cada pareja $(X_{1}, Y_{1})$, para $i=0, 1 ,2, ..., n$, hacen que la 
diferencia sea muy cercana a cero.

La solución numérica de una EDP es un conjunto de valores {$y_i$}, $i=0, 1, 2, ..., n$ tales que 
el valor $y_i$ junto a la _k_–ésima tupla $(x_{0}^{i},x_{1}^{i},x_{2}^{i}, ... x_{n}^{i})$ de
variables independientes hacen que la diferencia $L(u) - F$ sea muy cercana a cero para 
$i = 0, 1, 2, ..., n$.

# PVI - Método de Euler
La _EDO_ 
$$\frac{dy}{dx} = f(x,y) $$

expresa que la pendiente en cada punto $(x,y)$ de una gráfica está dada por la función $f(x,y )$. 
Si se conoce la pendiente en $(x_1, y_1)$ entonces es posible aproximar el valor de $y_{i+1}$ a 
través de la recta tangente a la curva en $(x_i, y_i)$.

$$y_{i+1} = y_i + f(x_i, y_i)h$$
donde $h = x_{i+1} - x_i$. Es decir: $$ y_{i+1} = y_i + \Theta h.$$

![PVI – Método de Euler](PVI%20%E2%80%93%20M%C3%A9todo%20de%20Euler_1.PNG)
------
![PVI – Método de Euler](PVI%20%E2%80%93%20M%C3%A9todo%20de%20Euler_2.PNG)

## Para tener en cuenta.
- En la _EDO_ 
${y}' = f(x,y )$ 
sólo se tiene una variable independiente y una variable dependiente 
por lo que este tipo de ecuaciones, generalmente, modelan fenómenos transitorios (aquellos que cambian 
en el tiempo).
- De acuerdo con la anterior observación, la EDO se acostumbra a escribir como:
$$\frac{dy} {dt} = f(t,y) \text{ donde } y= y(t)$$

- La _EDO_,  en situaciones prácticas, se acompaña de una condición inicial dando lugar a un _PVI_ que 
se plantea en la forma:
$$\left\{\begin{matrix}
\frac{dy}{dx} = f(x,y) & \\ 
y(x_{0} = y_{0}) & 
\end{matrix}\right.$$