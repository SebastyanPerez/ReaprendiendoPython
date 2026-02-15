class Jugador:
    total_jugadores = 0

    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.ataques_recibidos = 0
        Jugador.total_jugadores += 1

    def recibir_ataque(self, ataque):
        if self.esta_vivo() and ataque > 0:
            self.vida -= ataque
            self.ataques_recibidos += 1
            if self.vida < 0:
                self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

    def curar(self, cantidad):
        if self.esta_vivo() and cantidad > 0:
            self.vida += cantidad
            if self.vida > self.vida_max:
                self.vida = self.vida_max

    def pelear_con(self, otro_jugador, ataque):
        if self.esta_vivo() and otro_jugador.esta_vivo() and ataque > 0:
            otro_jugador.recibir_ataque(ataque)

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")

class Guerrero(Jugador):

    def atacar(self,otro_jugador,ataque):
        if self.esta_vivo() and otro_jugador.esta_vivo():
            danio_total = ataque + 10  # bonus físico
        print(f"{self.nombre} ataca con fuerza bruta 💥")
        super().pelear_con(otro_jugador, danio_total)

class Mago(Jugador):
    def lanza_hechizo(self,otro_jugador):
        if self.esta_vivo() and otro_jugador.esta_vivo():
            danio_total = 15  # daño mágico fijo
        print(f"{self.nombre} lanza un hechizo 🔮")
        super().pelear_con(otro_jugador, danio_total)

# Ejemplo de uso
g1 = Guerrero("Thor", 150)
m1 = Mago("Merlin", 100)

g1.atacar(m1, 20)
m1.mostrar_informacion()

m1.lanza_hechizo(g1)
g1.mostrar_informacion()
