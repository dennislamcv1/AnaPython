# Definición de función
def promedioDeLista(lista):
    sumatoria = 0
    for i in lista:
        sumatoria = sumatoria + i

    promedio = sumatoria / len(lista)
    return promedio

# Lista 1
G1 = [1, 2, 3, 4, 5]

# Promedio de los valores en la lista 1
x = promedioDeLista(G1)
print(x)

# Lista 2
G2 = [2, 4, 6, 8, 10, 12]

# Promedio de los valores en la lista 2
y = promedioDeLista(G2)
print(y)

# Lista 3
G3 = [80, 50, 100, 93, 75]

# Promedio de los valores en la lista 3
z = promedioDeLista(G3)
print(z)
