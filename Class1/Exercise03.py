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


vare = int(input('Enter a number: '))
print(vare)

vare += 1
print("vare + 1: ",vare)

vare -= 1
print("vare - 1: " ,vare)

vare += 5
print("vare + 5: ",vare)

print('-'.center(50,'-'))

varb1 = True
print("varb1: ", varb1)

varb2 = False
print("varb2: ", varb2)

print('-'.center(50,'-'))

x = 5.4

y = 3.1 + 2.3

print("x: ", x)
print("y: ", y)

print('-'.center(50,'-'))

print('Type of vare: ', type(vare))
print('Type of varb1: ', type(varb1))
print('Type of varb2: ', type(varb2))
print('Type of x: ', type(x))
print('Type of y: ', type(y))

print("x == y: ", x == y)

print(" End exercise 3 ".center(50,"*"))