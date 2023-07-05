#Crear una clase "Rectangulo" con atributos de ancho y alto. 
#Incluye métodos para calcular el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def area(self):
        return self.ancho * self.alto
        
    def perimetro(self):
        return 2*(self.ancho+self.alto)
    
rectangulo = Rectangulo(10, 5)
area=rectangulo.area()
perimetro=rectangulo.perimetro()
        
print(f"El area es de ", area)
print(f"El perimetro es de ", perimetro)