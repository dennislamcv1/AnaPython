nombres = { 'Andrea': '28', 'Daniel': '32', 'Monica':'24', 'Fabian':'33'}
#Buscar un elemnto a partir de su palabra clave
print(nombres.get('Andre', 'No encontrado'))

#Generar una lista en clave de los registros del diccionario
print(nombres.keys())

#Genera una lista en valor de los registros del dccionario:
print(nombres.values())

#Genera una lista en clave-valor de los registros del diccionario:
print(nombres.items())

#Extrae un registro de un diccionario a partir de su clave y lo borra
print(nombres.pop('Andrea', 'No encontrado'))

#Borra todos los registros del diccionario
print(nombres.clear())