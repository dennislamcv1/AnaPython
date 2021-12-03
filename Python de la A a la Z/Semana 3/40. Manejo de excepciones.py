pregunta = True

while pregunta:
    x = int(input("Ingrese un numero: "))
    print("Dividir 100 entre ", x, "te dará :", 100 / x)

'''
pregunta = True

while pregunta:
    try:
        x = int(input("Ingrese un numero: "))
        print("Dividir 100 entre ", x, "te dará :", 100 / x)
    except ValueError:
        print("La entrada no era un número entero. Vuelve a intentarlo ")

'''