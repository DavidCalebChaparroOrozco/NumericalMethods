# Problemas con Valores Iniciales

## Conceptos basicos
Una ecuación diferencial (ED) es una ecuación que contiene las derivadas de una función desconocida
, $u$. El _orden_ de la ecuación diferencial es el orden de la mayor derivada en la ecuación.

$m d{^2}u$

Si _u_ es la función desconocida entonces, estructuralmente, cualquier ecuación diferencial tiene la
forma

$L(u) = F$,

Donde el lado izquierdo representa todas las expresiones de la ecuación que están en terminos de _u_ o
que dependen de _u_ y sus derivadas. _F_ tipicamente es una función que solamente depende de las
variables independientes.

La función que aplica _L_ a _u_  se denomina operador.

$L: \text {Operador Diferencial}$

Una _solución_ de una ED es una función _u_ que cuando se sustituye en la ecuación genera una identidad.

La ecuación diferencial $L(u) = F$ se denomina _lineal_ si el operador satisface

$$L (\alpha u_1 + \beta u_2) = \alpha L (u_1) + \beta L (u_2)$$

donde _a_ y _B_ son escalares (coeficientes) y $u_1$ y $u_2$ son funciones. Una ED para cual _F_ es igual
a cero se denomina _homogenea_.

$ m \frac{d^{2}u}{dt^{2}} + c \frac{du}{dt} + ku = 0$
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

Una _ED_ se denomina _Ecuación Diferencial Ordinaria (EDO)_ si la función desconocida depende de una sola variable independiente.

$ m \frac{d^{2}u}{dt^{2}} + c \frac{du}{dt} + ku = F(t)$

La _ED_ modela un sistema de masa-resorte amortiguado. Aqui $u = u(t)$ representa desplazamiento de la masa desde la posición de equilibrio como una función del tiempo,
_t_. $m>0$