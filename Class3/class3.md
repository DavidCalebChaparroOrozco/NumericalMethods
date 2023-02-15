# Modulo
Un modulo es un archivo que contiene funciones y cuyo nombre es el nombre del archivo.
Existen cuatro formas de cargar un modulo en un codigo para acceder a sus funciones.

`
from nombre_modulo import *:
`

* Cargar todas las funciones del modulo. No es aconsejable porque puede generar conflictos
con definiciones cargadas desde otros modulos.

`
from nombre_modulo import func1, func2, ...
`

`
import nombre_modulo
`
* La función func se invoca con el comando nombre_modulo.func()

`
import nombre_modulo as alias
`
* Se accede al modulo a través de un alias y se accede a func con alias.func()