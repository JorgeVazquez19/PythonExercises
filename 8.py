class Personaje:
    vida = 100
    posicion = 1
    velocidad = 100

    def recibir_ataque(sefl, cantidad):
        Personaje.vida = Personaje.vida - cantidad
        if Personaje.vida <= 0:
            print("te mueres")

    def mover(self, cantidad):
        Personaje.posicion = cantidad * Personaje.velocidad


class Soldado(Personaje):
    ataque = 5

    def atacar (self, personaje):
        personaje.recibir_ataque(self.ataque)


class Campesino(Personaje):
    cosecha = 2

    def cosechar(self):
        cantidad_cosechada = 10
        return cantidad_cosechada
