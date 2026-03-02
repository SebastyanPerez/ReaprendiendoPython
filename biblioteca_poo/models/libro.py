class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def __str__(self):
        return f"{self.titulo} de {self.autor} (ISBN: {self.isbn})"
