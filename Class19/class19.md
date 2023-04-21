# Problemas con Valores Iniciales Métodos de Runge - Kutta

Una _Ecuación Diferencial (ED)_ es una ecuación que contiene las derivadas de una función desconocida, *u*.
El _orden_ de la ecuación diferencial es el orden de la mayor derivada en la ecuación.

$$m\frac{d^2u}{dt^2} + c\frac{du}{dt} + ku = 0$$

$$\frac{d^2u}{dt^2} + ksin(u) = sin(wt)$$

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + ku = 0$$

$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0$$

Las variables _t_, _x_ y _y_ representan variables independientes.

## Conceptos Básicos

Si _u_ es la función desconocida entonces, estructuralmente, cualquier ecuación diferencial tiene la forma.

$$L (u) = F$$

donde el lado izquierdo representa todas las expresiones de la ecuación que están en terminos de _u_ o que depeden de _u_ y sus derivadas.
_F_ tipicamente es una función que solamente depende de las variables independientes.
La función que aplica _L_ a _u_ se denomina operador.

$$ L: \text{Operador Diferencial}$$

Una _solución_ de una ED es una función _u_ que cuando se sustityye en la ecuación genera una identidad.

La ecuación diferencial $L(u) = F$ se denomina _lineal_ si el operador satisface.

$$L(\alpha \mu_1 + \beta \mu_2 ) = \alpha L(\mu_1) + \beta L (\mu_2)$$

donde $\alpha$ y $\beta$ son escalares (coeficientes) y $\mu_1$ y $\mu_2$ son funciones.
Una _ED_ para la cual _F_ es igual a cero se denomina *homogénea*.

$$$$