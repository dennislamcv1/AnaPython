# Concatenacion
mensaje1 = 'Saludos'+ ' '+ 'desde' + ' ' + 'Mexico'
print(mensaje1)

#Multiplicar
mensaje2 = ' a todos,' * 3
print(mensaje1 + mensaje2)

#Añadir
mensaje3 = ' vamos '
mensaje3 += 'a'
mensaje3 += ' programar'
print(mensaje1 + mensaje2 + mensaje3)

#Extensión
print(len(mensaje1 + mensaje2 + mensaje3))

# Encontrar
mensaje3 = mensaje3.find('programar')
print(mensaje3)

mensaje2 = mensaje2.find('gato')
print(mensaje2)
