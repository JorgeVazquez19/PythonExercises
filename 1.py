def first_option():
    word = input("escribe una palabra -> ")
    character = input("escribe un caracter -> ")
    print(character.join(word))

def second_option():
    text = input("Escribe una frase con espacios -> ")
    character = input("Escribe el caracter que va a sustituir los espacios -> ")
    print(text.replace(" ", character))


def third_option():
    word = input("Escribe clave -> ")
    character = "x"
    for i in range(0,len(word)):
     word = word.replace(str(i), character)
    print(word)


def fourth_option():
    word = input("escribe una palabra -> ")
    character = input("escribe un caracter -> ")
    aux = ""
    for i in range(0,len(word)):
        if i % 3 == 0 and i > 0:
            aux = aux + character
        aux = aux + word[i]


    print(aux)


options = {1: first_option,
           2: second_option,
           3: third_option,
           4: fourth_option

           }
print("escribe 1 para separar caracteres")
print("escribe 2 para sustituir espacios")
print("escribe 3 para sustituir la clave por xxxxx...")
print("escribe 4 para separar caracteres cada 3 posiciones")

num = int(input())
options[num]()
