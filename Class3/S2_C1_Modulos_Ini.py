'''
Taller sobre módulos

1.  Python viene con una gran cantidad de módulos que contienen funciones y métodos para varias tareas. Dos de esos módulos son math y cmath.
    math (Mathematical functions): Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar C.
    Excepto cuando se indique explícitamente lo contrario, todos los valores devueltos por las funciones de este módulo son flotantes.
    cmath (Mathematical functions for complex numbers): Este módulo proporciona acceso a funciones matemáticas para números complejos.
    Las funciones de este módulo aceptan números enteros, números de coma flotante o números complejos como argumentos.
    También aceptarán cualquier objeto de Python que tenga un método
    __complex__() o __float__(): estos métodos se utilizan para convertir el objeto en un número complejo o de punto flotante,
    respectivamente, y la función se aplica al resultado de la conversión.

2.  Ingrese en la terminal (parte inferior de la pantalla) las siguientes líneas de comando (si la terminal no está disponible puede activarla  con la combinación ctrl+ñ):

    python (enter)
    import math
    dir(math)
    import cmath
    dir(math)

    ¿Cómo puede describir la información que se muestra en pantalla?
    ¿Identifica similitudes entre las listas correspondientes a dir(math) y dir(cmath)?
    Ingrese el comando exit() en la línea de comando para cerrar python.
    Ingrese el comando clear para limpiar la terminal.

3.  Para ampliar la información sobre estos módulos consulte los enlaces
    math: https://docs.python.org/3/library/math.html
    cmath: https://docs.python.org/3/library/cmath.html

4.  Utilice las funciones log y sin, que hacen parte del módulo math, para calcular el logaritmo natural del seno de 0.5 radianes.
    Imprima el resultado obtenido. Emplee cada una de las cuatro formas de cargar un módulo si se desea utilizar una función específica.
    (El resultado debe ser -0.735166686385)

5.  La siguiente función calcula la primera y segunda derivadas de f en el punto x utilizando el parámetro h cuyo valor por defecto es 0.0001:

    def derivatives(f,x,h=0.0001):
        df = (f(x+h) - f(x-h))/(2.0*h)
        dff= (f(x+h) - 2.0*f(x) + f(x-h))/(h**2)
        return df,dff

    Utilice la función anterior para calcular la primera y segunda derivadas de la función tangente inversa en x=0.5 (deben obtenerse los resultados 0.799999999573 y -0.639999991892, respectivamente)
'''

# import math
# # import cmath

# def sin(x):
#     return math.sin(x)

# def cos(x):
#     return math.cos(x)

# def log(x):
#     return math.log(x)

# def atan(x):
#     return math.atan(x)

# def derivatives(f,x,h=0.0001):
#     df = (f(x+h) - f(x-h))/(2.0*h)
#     dff= (f(x+h) - 2.0*f(x) + f(x-h))/(h**2)
#     return df,dff


# numberX = float(input("Enter the number: "))

# result = sin(numberX)
# print(f"The result of sin: {result}")

# result = cos(numberX)
# print(f"The result of cos: {result}")

# result = log(numberX)
# print(f"The result of log: {result}")

# print(derivatives(f=atan,x=numberX))

from math import atan
# import cmath

def derivatives(f,x,h=0.0001):
    df = (f(x+h) - f(x-h))/(2.0*h)
    dff= (f(x+h) - 2.0*f(x) + f(x-h))/(h**2)
    return df,dff


numberX = float(input("Enter the number: "))

print(f'The derivates are: {derivatives(f=atan,x=numberX)}')