"""
DÍA 6 POO - MINI SISTEMA DE COMBATE POR TURNOS
Aplicando: Herencia, Override, super(), Polimorfismo y Métodos de Clase
"""

from abc import ABC, abstractmethod
from random import randint
from datetime import datetime


class Personaje(ABC):
    """Clase base abstracta para todos los personajes"""
    
    contador_personajes = 0  # Método de clase para rastrear personajes
    
    def __init__(self, nombre: str, salud: int, fuerza: int):
        self.nombre = nombre
        self.salud = salud
        self.salud_maxima = salud
        self.fuerza = fuerza
        self.indice_combate = 0
        Personaje.contador_personajes += 1
    
    @classmethod
    def obtener_total_personajes(cls):
        """Método de clase - Obtiene el total de personajes creados"""
        return cls.contador_personajes
    
    @abstractmethod
    def atacar(self, objetivo: 'Personaje') -> int:
        """Cada personaje ataca de forma diferente (Polimorfismo)"""
        pass
    
    def recibir_daño(self, daño: int):
        """Reduce la salud del personaje"""
        self.salud -= daño
        if self.salud < 0:
            self.salud = 0
    
    def sanar(self, cantidad: int):
        """Recupera salud hasta el máximo"""
        self.salud = min(self.salud + cantidad, self.salud_maxima)
    
    def esta_vivo(self) -> bool:
        """Verifica si el personaje sigue vivo"""
        return self.salud > 0
    
    def __str__(self):
        return f"{self.nombre} | ❤️ {self.salud}/{self.salud_maxima} | 💪 {self.fuerza}"


class Guerrero(Personaje):
    """Guerrero - Ataque directo con bonificación de fuerza"""
    
    def __init__(self, nombre: str, salud: int, fuerza: int):
        super().__init__(nombre, salud, fuerza)
        self.defensa = 10
    
    def atacar(self, objetivo: 'Personaje') -> int:
        """Override: Attack directo con crítico aleatorio"""
        daño_base = self.fuerza + randint(5, 15)
        critico = randint(1, 100) > 80  # 20% de probabilidad
        
        if critico:
            daño = daño_base * 2
            print(f"⚔️  {self.nombre} ¡CRÍTICO! inflige {daño} de daño")
        else:
            daño = daño_base
            print(f"⚔️  {self.nombre} ataca con {daño} de daño")
        
        objetivo.recibir_daño(daño)
        return daño
    
    def activar_defensa(self):
        """Habilidad especial del Guerrero"""
        self.indice_combate += 20
        print(f"🛡️  {self.nombre} sube su defensa! +20 armadura")


class Mago(Personaje):
    """Mago - Ataque mágico con menor salud pero más daño"""
    
    def __init__(self, nombre: str, salud: int, fuerza: int, mana: int = 100):
        super().__init__(nombre, salud, fuerza)
        self.mana = mana
        self.mana_maxima = mana
    
    def atacar(self, objetivo: 'Personaje') -> int:
        """Override: Ataque mágico que consume mana"""
        if self.mana < 20:
            print(f"😰 {self.nombre} no tiene suficiente mana!")
            daño = randint(3, 8)
        else:
            daño = self.fuerza + randint(15, 25)
            self.mana -= 20
            print(f"✨ {self.nombre} lanza hechizo infligiendo {daño} de daño")
        
        objetivo.recibir_daño(daño)
        return daño
    
    def recuperar_mana(self, cantidad: int = 30):
        """Habilidad especial del Mago"""
        self.mana = min(self.mana + cantidad, self.mana_maxima)
        print(f"🔮 {self.nombre} recupera {cantidad} de mana")


class Arquero(Personaje):
    """Arquero - Ataque rápido y evasión"""
    
    def __init__(self, nombre: str, salud: int, fuerza: int):
        super().__init__(nombre, salud, fuerza)
        self.municiones = 50
    
    def atacar(self, objetivo: 'Personaje') -> int:
        """Override: Ataque rápido de múltiples flechas"""
        if self.municiones < 5:
            print(f"🏹 {self.nombre} se quedó sin flechas!")
            return 0
        
        daño = self.fuerza + randint(8, 12)
        self.municiones -= 5
        print(f"🏹 {self.nombre} dispara {daño} de daño (Munición: {self.municiones})")
        
        objetivo.recibir_daño(daño)
        return daño
    
    def evasion(self):
        """El arquero puede evadir un ataque"""
        print(f"💨 {self.nombre} se esquiva ágilmente!")
        return True


class CombateManager:
    """Gestor del combate por turnos"""
    
    def __init__(self, personaje1: Personaje, personaje2: Personaje):
        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.turno = 0
        self.historial = []
    
    def mostrar_estado(self):
        """Muestra el estado actual de ambos personajes"""
        print(f"\n{'='*60}")
        print(f"Turno {self.turno}")
        print(f"{'='*60}")
        print(f"[1] {self.personaje1}")
        print(f"[2] {self.personaje2}")
        print(f"{'='*60}\n")
    
    def ejecutar_turno(self, atacante: Personaje, defensor: Personaje):
        """Ejecuta un turno de combate"""
        self.turno += 1
        self.mostrar_estado()
        
        print(f"🔴 Turno de {atacante.nombre}")
        atacante.atacar(defensor)
        
        if not defensor.esta_vivo():
            return False
        
        return True
    
    def simular_combate(self):
        """Simula un combate completo"""
        print(f"\n{'🔥'*30}")
        print(f"INICIO DEL COMBATE")
        print(f"⚡ {self.personaje1.nombre} VS {self.personaje2.nombre}")
        print(f"{'🔥'*30}\n")
        
        while self.personaje1.esta_vivo() and self.personaje2.esta_vivo():
            if not self.ejecutar_turno(self.personaje1, self.personaje2):
                self.combate_terminado(self.personaje1)
                break
            
            input("Presiona Enter para continuar...")
            
            if not self.ejecutar_turno(self.personaje2, self.personaje1):
                self.combate_terminado(self.personaje2)
                break
            
            input("Presiona Enter para continuar...")
    
    def combate_terminado(self, ganador: Personaje):
        """Finaliza el combate"""
        print(f"\n{'🏆'*30}")
        print(f"¡¡¡ {ganador.nombre.upper()} HA GANADO !!!")
        print(f"{'🏆'*30}\n")


# 🎮 DEMOSTRACIÓN DEL SISTEMA
if __name__ == "__main__":
    # Crear personajes
    guerrero = Guerrero("Conan", salud=150, fuerza=25)
    mago = Mago("Gandalf", salud=80, fuerza=30, mana=100)
    arquero = Arquero("Legolas", salud=100, fuerza=20)
    
    # Mostrar total de personajes creados (método de clase)
    print(f"Total de personajes en juego: {Personaje.obtener_total_personajes()}\n")
    
    # Demostración individual
    print("=" * 60)
    print("DEMOSTRACIÓN DE POLIMORFISMO - Cada clase ataca diferente")
    print("=" * 60)
    
    dummy = Guerrero("Dummy", 200, 0)
    
    print("\n1. GUERRERO ATACANDO:")
    guerrero.atacar(dummy)
    
    print("\n2. MAGO ATACANDO:")
    mago.atacar(dummy)
    
    print("\n3. ARQUERO ATACANDO:")
    arquero.atacar(dummy)
    
    # Iniciar combate
    print("\n\n")
    input("Presiona Enter para iniciar combate...")
    
    combate = CombateManager(guerrero, mago)
    combate.simular_combate()

