# Este es el primer archivo de python
print('Hola mundo')

# Es posible imprimir resultados de operaciones 
# como se muestra a continuación
print(12*3)
print(15 + 6)
print(15/3)


""" 
Si es necesario incluir varias líneas de
comentarios puede utilizarse comillas
dobles. 
"""

'''
También se consigue un bloque comentado
si se utilizan comillas sencillas. Ambas
opciones permiten ingresar comentarios
al programa.
'''

# Declaración de variables en el código
# ==============================================
var1='Julian'
var2=24
var3=input('¿Curso a cargo? ')

print('Mi nombre es ',var1)
print('Soy el profesor del curso ',var3)
print('El número de estudiantes en el curso es ',var2)








# Tipos de datos: Strings, integer, boolean y float
# Ejercicio 1: Cree una variable de cada tipo, imprima cada variable e imprima el tipo (type) de cada variable.
# Ejercicio 2:
#     Cree una variable tipo string que contenga su nombre (var1s)
#     Cree una segunda variable tipo string que contenga el programa en el que está matriculado (var2s)
#     Cree una variable tipo entera que contenga el semestre que cursa en su programa (var3n)
#     Concatene las variables de tres formas diferentes:
#         Forma 1: "Mi nombre es " + var1s + ". Soy estudiante de " + var2s + " y estoy en el semestre " + var3n
#         Forma 2: "Mi nombre es {}. Soy estudiante de {} y estoy en el semestre {}".format(var1s,var2s,var3n)
#         Forma 3: f"Mi nombre es {var1s}. Soy estudiante de {var2s} y estoy en el semestre {var3n}"
#     Imprima cada variable y las concatenaciones construidas
# Ejercicio 3:
#     Cree una variable tipo entero (vare)
#         Increméntela en 1
#         Disminúyala en 1
#         Increméntela en 5
#         Imprima el resultado de cada operación
#     Cree una variable booleana (varb1) con valor verdadero (True)
#     Cree una segunda variable booleana (varb2) con valor falso (False)
#     Cambie el valor de la segunda variable anteponiendo el comando not a la variable
#     Imprima las variables
#     Cree una variable tipo float (x) y asígnele el valor 5.4
#     Cree una segunda variable tipo float (y) y asígnele el resultado de la operación 3.1 + 2.3
#     Imprima cada variable
#     Imprima el tipo de cada variable
#     Digite el comando print(x == y) y ejecute el programa.
# Ejercicio 4. Revisión de comandos de transformación y de operaciones entre variables.
#     Cree una variable tipo entero (vare) y asígnele un valor.
#     Imprima el tipo de variable
#     Digite el comando vare = str(vare)
#     Imprima el tipo de variable
#     Digite el comando varn = input('Ingrese un número entero')
#     Imprima el tipo de variable
#     Digite el comando varn = int(varn)
#     Imprima el tipo de variable
#     Genere varias variables numéricas con valor entero y varias variables tipo string
#     Opere las variables numéricas entre sí y las variables tipo string entre sí utilizando 
#         las operaciones + y *. Imprima los resultados.
#     Opere las variabes numéricas entre sí utiizando las operaciones -, /, %, //, **