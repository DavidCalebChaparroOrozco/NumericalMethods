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

vare = int(input('Enter a number: '))
print(type(vare))
print(vare)
vare = str(vare)
print(type(vare))
print(vare)

print('-'.center(50,'-'))

varn = input('Enter an integer: ')
print(type(varn))
print(varn)
varn = int(varn)
print(type(varn))
print(varn)

print("-".center(50,'-'))

num1 = 1
num2 = 2
num3 = 3
num4 = 4

s1 = 'Hello'
s2 = 'World'
s3 = '!'

print('num1 + num2: ', num1 + num2)
print('num3 * num4: ', num3 * num4)
print('s1 + s2: ', s1 + s2)
print('s2 * 3: ', s2 * 3)

print('-'.center(50,'-'))

print("num1 - num2:", num1 - num2)
print("num2 / num1:", num2 / num1)
print("num2 % num1:", num2 % num1)
print("num2 // num1:", num2 // num1)
print("num1 ** 2:", num1 ** 2)

print(" End exercise 4 ".center(50,"*"))