class Corcho:
    bodega = 'San Martin De Valdeiglesias'


class Botella:
    corcho = Corcho()
    isOpen = False


class Sacacorchos:
    def destapar(self,corcho,botella):
        botella.isOpen = True
        corchoSacado = corcho.bodega


def limpiar():
    Botella.corcho = Corcho()
