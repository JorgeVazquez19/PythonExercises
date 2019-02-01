def sortList(lista):
    auxList = []
    for i in range(len(lista)):
        aux = ""
        aux = aux + str(lista[i][1]) + " " + "." + str(lista[i][2]) + " " + str(lista[i][0])
        auxList.append(aux)
    return auxList


list_person = [("Angulo", "David", "D"), ("Perez", "Jesus", "J")]
print(sortList(list_person))
