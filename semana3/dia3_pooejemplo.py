class Jugador :

    def __init__(self,nombre,vida): 
        self.nombre=nombre
        self.vida=vida
        self.vida_max=vida
        self.ataque_resivido=0
    
    def recibir_ataque(self,ataque):
       
        if self.esta_vivo() and ataque>0:
            self.vida-=ataque
            self.ataque_resivido+=1

            if self.vida < 0:
             self.vida = 0
        else:
           print(f"El ataque a {self.nombre} no tuvo efecto (ya está muerto o daño inválido).")
        
    def esta_vivo(self):
        return self.vida>0
    
    def curar(self,curacion):
        if self.esta_vivo() and curacion>0:
            self.vida+=curacion
            if self.vida > self.vida_max:
                self.vida = self.vida_max
        else:
            print(f"La curación a {self.nombre} no tuvo efecto (ya está muerto o curación inválida).")

    def pelear_con(self, otro_jugador,ataque):
        if self.esta_vivo() and otro_jugador.esta_vivo() and ataque>0:
            otro_jugador.recibir_ataque(ataque)
        else:
            print(f"El pelea entre {self.nombre} y {otro_jugador.nombre} no tuvo efecto (alguno está muerto o ataque inválido).")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Ataques resividos: {self.ataque_resivido}")

j1=Jugador("sebas",5)
j2=Jugador("maria",50)

j1.recibir_ataque(2)
j1.curar(30)
j1.mostrar_informacion()
j2.recibir_ataque(1)
j2.mostrar_informacion()