# Las funciones son sentencias que nos permiten aumentar la complejidad de los programas que podemos construir en
# Python y facilitar su construcción y lectura. Las funciones nos ayudan a agrupar un conjunto de sentencias para que
# puedan ser ejecutadas por un programa más de una vez. ¿Cómo nos sirven las funciones y cuáles son sus ventajas?
# Veamos el siguiente ejemplo para comprender la importancia de estas sentencias.

# Lista 1

G1 = [1, 2, 3, 4, 5]

# Promedio de los valores en la lista 1

sumatoria = 0
for i in G1:
    sumatoria = sumatoria + i

promedio = sumatoria / len(G1)
print(promedio)

# Lista 2

G2 = [2, 4, 6, 8, 10, 12]

# Promedio de los valores en la lista 2

sumatoria = 0
for i in G2:
    sumatoria = sumatoria + i

promedio = sumatoria / len(G2)
print(promedio)

# Lista 3

G3 = [80, 50, 100, 93, 75]

# Promedio de los valores en la lista 3

sumatoria = 0
for i in G3:
    sumatoria = sumatoria + i

promedio = sumatoria / len(G3)
print(promedio)