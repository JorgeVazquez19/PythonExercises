def first_option():
    names = ("Jesus", "Carlos", "Benito", "Pepe")
    for elto in names:
        print(elto + " vote por mí")


def second_option():
    names = ("Jesus", "Carlos", "Benito", "Pepe", "Jacinto", "Julio", "Verne", "Federico")
    posicion = int(input("Escribe la posicion ->"))
    cantidad = int(input("Escribe la cantidad ->"))
    posicion = posicion - 1
    cantidad = posicion + cantidad
    for i in range(posicion, cantidad):
        print(names[i] + " vote por mí")


def third_option():
    names = [["Jesus", "hombre"], ["Benito", "hombre"], ["Carmen", "hombre"], ["Maria", "hombre"]]
    for i in range(0, len(names)):
        aux = str()
        print(str(names[i]) + " vote por mí")

def fourth_option():
    names = [["Jesus", "hombre"], ["Benito", "hombre"], ["Carmen", "hombre"], ["Maria", "hombre"]]
    posicion = int(input("Escribe la posicion ->"))
    cantidad = int(input("Escribe la cantidad ->"))
    posicion = posicion - 1
    cantidad = posicion + cantidad
    for i in range(posicion, cantidad):
        print(str(names[i]) + " vote por mí")

options = {1: first_option,
           2: second_option,
           3: third_option,
           4: fourth_option}

print("escribe 1 para imprimir x vote por mí")
print("escribe 2 para imprimir x vote por mí desde una posicion concreta y con una cantidad concreta")
print("escribe 3 para hacer lo de la opcion 1 pero distinguiendo entre géneros")

num = int(input())
options[num]()
