""""
#Definición de una clase
class <nombre_clase>(<super_clase):
#Metodo __init__ se conoce como el constructor
    def  __init__(self, <parametros>):
        <expresión

    def <nombre_metodo>(self, <parametros>):
        <expresión>

"""

# Definición
class Nacionalidad:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def presentacion(self, presento):
        return f'Hola mi nombre es {presento.nombre}, soy de {presento.pais}.'
#Impresión
mexico = Nacionalidad('Laura', 'México')
colombia = Nacionalidad('Luisa', 'Colombia')

print(mexico.presentacion(colombia))