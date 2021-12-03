x1 = { 5, 10, 15, 20, 25, 30}
x2 = x1.copy()
print(x1, x2)

#Realizamos la unión entre dos conjuntos
x2 = {6, 12, 18, 24, 30}
print(x1.union(x2))

#Podemos encontrar la diferencia entre dos conjuntos
print(x1.difference(x2))

# De igual forma podemos encontrar el elemento en comun entre ellos
print("La intersección es: ", x1.intersection(x2))

#Tambien podemo hallar la diferencia simetrica entre los conjuntos
#Devuelve los elementos simétricamente diferentes entre dos conjuntos,
# es decir, todos los elementos que no concuerdan entre los dos conjuntos:
print(x1.symmetric_difference(x2))
