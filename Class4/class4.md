# Errores
Debido a que los metodos numericos son utilizados, generalmente para aproximar la solución de problemas
complejos que, por lo regular, carecen de solución analitica o conocida, en su naturaleza esta inmerso el error.

- Errores de redondeo: se deben a que la computadora tan solo representa cantidad de un numero finito de digitos.

- Erores de truncamiento: Discrepancia que se introduce por el hecho de que los metodos numericos pueden emplear aproximaciones para representar operaciones y cantidades matematicas exactas.

- Errores no relacionados con el metodo: equivocaciones, errores de formulación o del modelo, y la incertidumbre en la obtención de los datos.

## Errores de redondeo:
Los numeros son almacenados en la memoria dle computador utilizando una cadena de digitos binarios o bits que es finita. Esto genera una dificultad evidente con el almacenamiento de numeros como: $\pi$, $e$ ,$\sqrt{2}$


- Para reflexionar:
    1. ¿Que relación existe entre el sistema de numeración decimal y el sistema de numeración binario?
    2. ¿Como se expresa el numero 173 en terminos de potencias de 10? $$(173)_{10}$$
    $$173 = 100 + 70 + 3 = 1 * 10^2 + 7 * 10^1 + 3 * 10^0$$
    3. ¿Como se expresa el numero 173.246 en termino de potencia de 10? $$(173.246)_{10}$$
    $$173 = 100 + 70 + 3 = 1 * 10^2 + 7 * 10^1 + 3 * 10^0 + 2 * 10^{-1} + 4 * 10^{-2} + 6 * 10^{-3} $$
    4. ¿Cual es la representación en el sistema de numeración binario del numero?
    $$(173)_2$$

- Utilizar los comandos int() y bin() para convertir de un sistema de numeración a otro.

# Representación Entera:
El metodo mas sencillo de almacenamiento se utiliza con numeros enteros y se denomina _Metodo de magnitud con signo_. Consiste en utilizar el primer bit de la cadena para indicar el signo y los restantes se utilizan para guardar el numero.

${0:+}$ y ${1:-}$

- Ejm1 : Si se cuenta con un computador de 16 bits, el numero $-173$ se almacena en memoria con la cadena.
`1 0 0 0 0 0 0 0 1 0 1 0 1 1 0 1`

- Ejm2: Determine el rango de enteros de base 10 que puede ser representado en un computador de 16 bits.
`0 1 1 1 1 1 1 1 1 1 1 1 1 1 1`

## Para tener en cuenta.
    1. El cero tiene una doble representación por lo que ocupa dos cadenas de digitos binarios. Una de ellas puede utilizarse para almacenar un numero entero mas.

    2. La representación en el sistema binario del mayor numero entero que puede almacenarse utilizarse utilizando el metodo de magnitud con signo se simplifica facilmente debido a que su estructura tiene la forma del producto notable:
$$(x - y)(x^{n-1} + x^{n-2}y +  \cdot\cdot\cdot + xy^{n-2} + y^{n-1})= x^{n} - y^{n} $$

## Representación real
Los numeros reales se almacenan en la maquina utilizando la _Representation de punto flotante_
$$mb^{-e}$$

$$ \text { m: Mantisa normalizada (parte entera igual a cero y primer cifra decimal diferente de cero)}$$
$$ \text {b: Base del sistema numerico}$$
$$ \text {e: Exponente.}$$

## Para tener en cuenta.
Como consecuencia de la normalización, $m < 1$ (limite superior) y $m >= 0.1$ (limite inferior). Es decir:
$$\frac{1}{b} \leq m < 1$$

* Ejercicio 2: Escribir los numeros 156.78 y 1/34 en su representación punto flotante.
    - $156.78$
        - $\text {Signo: 0 (positivo)}$
        - $\text {Exponente: 10000010 (130 en decimal) sumado a un sesgo de 127, resultando en 257 en binario (100000001)}$
        - $\text {Mantisa: 1.00111110011100110101110 (los primeros 23 bits después del punto decimal)}$
        - $\text {Representación en punto flotante: }$`0 10000001 00111110011100110101110`

    - $1/34$
        - $\text {Signo: 0 (positivo)}$
        - $\text {Exponente: -5 sumado a un sesgo de 127, resultando en 122 en binario (01111010)}$
        - $\text {Mantisa: 1.01010101010101010101011 (los primeros 23 bits después del punto decimal)}$
        - $\text {Representación en punto flotante: }$`0 01111010 01010101010101010101011`