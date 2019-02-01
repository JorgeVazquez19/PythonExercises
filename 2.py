def first_option():
    word = input("escribe una palabra -> ")
    secondWord = input("escribe otra palabra -> ")
    if word in secondWord:
        print("la palabra " + word + " esta dentro de la palabra " + secondWord)
    else:
        print("la palabra " + word + " no esta dentro de la palabra " + secondWord)


def second_option():
    word = input("escribe una palabra -> ")
    secondWord = input("escribe otra palabra -> ")
    if word < secondWord:
        print(word)

    else:
       print(secondWord)

options = {1: first_option,
           2: second_option,


           }
print("escribe 1 para comprobar si una palabra esta dentro de otra")
print("escribe 2 para imprimer la palabra anterior en orden alfabético")


num = int(input())
options[num]()
