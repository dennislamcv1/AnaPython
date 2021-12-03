# Es importante distinguir entre dos acciones que podemos realizar con funciones.
# 1. Definir una función
# 2. Llamar a una función
# Para poder llamar a una función, primero es necesario definirla. En este video aprenderás
# cuáles son los elementos que necesitarás para hacerlo.

# Lo primero que necesitamos utilizar para definir una función es escribir la palabra reservada "def";
# después, Python te permite asignarle el nombre que tu quieras a la funcion. En seguida del nombre,
# se abren paréntesis, dentro de los cuales escribiremos los parámetros de la función.
# Los parámetros pueden ser de dos tipos:
# 1. Por nombre
# 2. Por defecto

# Una vez que asignamos los parámetros, cerramos paréntesis y en seguida colocamos dos puntos.
# Al dar enter, se nos colocará automáticamente una sangría o indentación. Es aquí donde
# nosotros podemos escribir todas las sentencias que deseamos en nuestra función.
# Por último, Python nos permite regresar un valor a nuestro programa principal a través de la palabra
# reservada "return" seguido de la variable que deseamos recuperar.
# De esta manera, podemos utilizar los resultados que logramos en nuestra función.

# Vayamos a nuestra computadora y veamos el primer ejemplo.

def saludo(nombre):
    print("Hola", nombre)

saludo("Carlos")
saludo("Luisa")
saludo("Frodo")

def promedio5(a, b, c, d, e):
    media = (a + b + c + d + e) / 5
    return media

x = promedio5(1, 2, 3, 4, 5)
print(x)

def promedio3(a, d, b=2, c=6):
    media = (a + b + c + d) / 4
    return media

x = promedio3(2, 3)
print(x)