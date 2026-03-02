from .libro import Libro
from .usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
