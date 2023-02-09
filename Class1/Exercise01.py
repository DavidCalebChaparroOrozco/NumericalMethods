# Tipos de datos: Strings, integer, boolean y float
# Ejercicio 1: Cree una variable de cada tipo, imprima cada variable e imprima el tipo (type) de cada variable.

name = input('Enter your name: ')
print(name)
print(type(name))

genre = input('What gender are you? (M) or (F): ')
if genre.lower() == 'm':
    es_genre = True
else:
    es_genre = False
print(es_genre)
print(type(es_genre))

age = int(input('Enter your age: '))
print(age)
print(type(age))

avg = float(input('What was your average last semester?: '))
print(avg)
print(type(avg))
print("End exercise 1 ".center(50,"*",))