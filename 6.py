contacts = {
        "david": "6757585",
        "chechu": "94859345",
        "maria": "35384435",
    }
name = ""
while name != "*":
    name = str(input("Escribe el nombre del contacto a buscar o * si deseas finalizar el programa --> "))
    if contacts.get(name):
        print(contacts.get(name))
        modify = int(input("Escribe 1 si deseas modificar el contacto --> "))
        if modify == 1:
           num = str(input("Introduce el nuevo número para " + name + "--> "))
           contacts.update({name: num})


    else:
        print("Ese contacto no existe, introduce el numero de ese contacto para introducirlo")
        num = str(input())
        contacts.update({name: num})
