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

$$\text{con } r_j = \left \| \overrightarrow{x} - \overrightarrow{\varepsilon}_j \right \|_{L2}$$

![Alt text](Interpolacion%20con%20RBF.jpeg)

# Ejm de Interpolación
- Ejm 1: Estime $ln(2)$ mediante interpolación con funciones de Base Radial.
    - Primero realizar el calculo por interpolación entre $ln(1) = 0$ y $ln(6) = 1.791759$
    - Incremente la cantidad de puntos (datos) y estimar nuevamente $ln(2)$
        * Tener en cuenta que $ln(2) = 0.6931472$

        | **J** | **x** | **y**    |
        |-------|:-----:|----------|
        | 1     | 1     | 0        |
        | 2     | 6     | 1.791759 |

        $$\zeta_1 = 1$$
        $$\zeta_2 = 6$$
        $$n = 2$$

        $$\alpha_1, \alpha_2: \text{Incognitas}$$
        $$\text{Seleccionamos } c = 1$$

        $$u(\overrightarrow{x}) = \sum_{j=1}^{n} \alpha_j \Psi (r_j) = \sum_{j=1}^{n} \alpha_j\sqrt{(x-\zeta_j)^{2}+C^{2}}$$

        $$
        \left.\begin{matrix} 
        \Psi (r_1) = \sqrt{(x-\zeta_1)^{2}+C^{2}} = \sqrt{(x-1)^{2}+1}
        \\ 
        \Psi (r_2) = \sqrt{(x-\zeta_2)^{2}+C^{2}} = \sqrt{(x-6)^{2}+1}
        \end{matrix}\right\} u(x)$$

    La siguiente expresión es importante:

    $$u(x) = \sum_{j=1}^{2} \alpha_1 \Psi(r_1) + \alpha_2 \Psi(r_1) = \alpha_1\sqrt{(x-1)^{2}+1} + \alpha_2\sqrt{(x-6)^{2}+1}$$

    La grafica de $u$ debe pasar por los puntos (1,0) y (6,1.791759)
    1. $u(x_1) = y_1:$ 
    $$u(1)= \alpha_1\sqrt{(1-1)^{2}+1} + \alpha_2\sqrt{(1-6)^{2}+1}=0$$
    $$\alpha_1 + 5.099 \alpha_2 = 0$$

    2. $u(x_2) = y_2:$ 
    $$u(6)= \alpha_1\sqrt{(6-1)^{2}+1} + \alpha_2\sqrt{(6-6)^{2}+1}=1.791759$$
    $$ 5.099 \alpha_1 + \alpha_2 = 1.791759$$

    De (1) y (2):

    $$\begin{bmatrix}
        1 & 5.099 \\ 
        5.099 & 1
        \end{bmatrix}
        \begin{bmatrix}
        \alpha_1  \\ 
        \alpha_2
        \end{bmatrix}
        =
        \begin{bmatrix}
        0  \\ 
        1.791759
        \end{bmatrix}
        \Rightarrow 

        \begin{matrix}
        \alpha_1 = 0.3654 \\ 
        \alpha_2 = -0.0716
    \end{matrix}$$

    Reemplazando estos valores en la expresión
    $$u(x) = 0.3654 \sqrt{(x-1)^{2}+1} - 0.0716\sqrt{(x-6)^{2}+1}$$

    $$u(2) = 0.3654 \sqrt{(2-1)^{2}+1} - 0.0716\sqrt{(2-6)^{2}+1} \Rightarrow u(2) = 0.2213$$

- Ejm 2: