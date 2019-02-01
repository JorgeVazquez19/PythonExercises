def sortList(cadena, lista):
    auxList = []
    matching = [s for s in lista if cadena in s]
    auxList.append(matching)
    return auxList


list_person = [("David", "43545435"), ("Jesus", "83473483"),("David", "853485675635")]

print(sortList("David", list_person))