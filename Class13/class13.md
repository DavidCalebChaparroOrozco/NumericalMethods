# Interpolación con BRF

Es una función Real que dependen de dos puntos o nodos uno de ellos, un nood puente que actua como 
centro y el otro de campo para evaluar la función.
Hay 3 parametros que define la función radial $\varepsilon$ el cual es el centro, otro puede ser un
vector definido por la forma euclidiana.

$$\text{Si } \overrightarrow{x}, \overrightarrow{\varepsilon} \epsilon R^{d} \text{ y } r = \left \| \overrightarrow{x} - \overrightarrow{\varepsilon} \right \|_{L2}$$

La función de base radial $\psi (r)$ se caracteriza por:

- Simetria radial:
    Tiene que estar relacionado con la distancia Euclidiana

- Monotonia:
    Tiene que ver con las funciones crecientes o decrecientes

- Diferenciabilidad:
    Caracteristica mas importante, que sea derivable en cualquier dirección

![Alt text](Funciones%20de%20base%20radial.jpeg)

## Tabla de funciones mas comunes.
_C_: Parametro de forma

_m_: Numero impar

_MQ_: La mas utilizada

_TPS_: Para esta los puntos no sean colineales.

_MQ o G_: NO SE REQUIERE NINGUNA REGULARIDAD

![Alt text](Funciones%20de%20base%20radial%20mas%20comunes.jpeg)

Ahora a partir de unos puntos conocidos se puede hallar nuevos valores en zona donde no hay información

![Alt text](Aplicaciones%20con%20RBF.jpeg)

Es una tecnica para interpolar datos dispersos multidimensionales.

$$X: \text{Es cualquier punto del dominio que se quiere obtener el valor de la función.}$$

$${\varepsilon}_j: \text{Datos conocidos} \rightarrow  \text{Trial points, donde se conoce la solución}.$$

- Considere una función multivariable $u$ , cuyos valores son conocidos en un conjunto de puntos
$\overrightarrow{x_1}, \dots , \overrightarrow{x_n}$ , llamados _test points_.

- Se define un segundo conjunto de puntos $\varepsilon_{1}, \dots , \overrightarrow{xi_n}$ conocidos como _trial points_.

- Se obtiene una función de interpolación en términos de RBF dada por:

$$u(\overrightarrow{x}) = \sum_{j=1}^{n} \alpha_j \Psi (r_j)$$

$\text{con } r_j = \left \| \overrightarrow{x} - \overrightarrow{\varepsilon}_j \right \|_{L2}$

![Alt text](Interpolacion%20con%20RBF.jpeg)
