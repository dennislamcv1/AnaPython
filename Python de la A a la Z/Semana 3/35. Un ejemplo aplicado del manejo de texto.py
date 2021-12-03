def lectura():
    numeros = []
    with open("numeros", "r") as f:
        for line in f:
            numeros.append(int(line))
        print(numeros)

def escritura():
    paises = ["Mexico", "Colombia", "Brasil", "Uruguay", "Argentina"]
    with open("paises.txt", "a", encoding="utf-8") as f:
        for nombre in paises:
            f.write(nombre)
            f.write("\n")

def ejecucion():
    lectura()
    escritura()

if __name__ == '__main__':
    ejecucion()

