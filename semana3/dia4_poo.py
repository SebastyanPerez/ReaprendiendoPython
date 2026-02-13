class Jugador:
    total_jugadores=0
    def __init__(self,nombre,vida):
        self.nombre=nombre
        self.vida=vida
        self.vida_max=vida
        self.ataques_recibidos = 0

        Jugador.total_jugadores+=1


j1 = Jugador("Sebas", 100)
j2 = Jugador("Maria", 50)

print(Jugador.total_jugadores)  
print(j1.total_jugadores)       
print(j2.total_jugadores)       
