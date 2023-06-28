# Implementa una clase "Libro" con atributos de título, 
# autor y año de publicación. Incluye métodos para obtener
# la información del libro y verificar si es un clásico (publicado hace más de 50 años).

class Libro():
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        
    def info (self):
        print("Titulo: " + self.titulo, "|  Autor: " + self.autor, "|  Año: " + str(self.año))
        
    def clasico(self):
        año_actual = 2023
        if año_actual - self.año > 50:
            print("Este libro es un clasico")
        else:
            print("Este libro no es un clasico")
        
libro = Libro("El monje que vendio su ferrari", "Robin S. Sharma", 1996)
libro.info()
libro.clasico()