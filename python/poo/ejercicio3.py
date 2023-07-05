#Crea una clase "Persona" con atributos de nombre, edad y ciudad. 
#Agrega métodos para obtener la información de la persona y determinar
#si es mayor de edad (edad mayor o igual a 18)

class Persona():
    def __init__ (self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def info(self):
        print(f"El nombre es {self.nombre}, tiene una edad de {self.edad}, y es de la ciudad de {self.ciudad}")
        
    def mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
        
persona1 = Persona("Oscar", 19, "Bogota")
persona1.info()
persona1.mayor()

print()

persona2 = Persona("Juan", 17, "Bogota")
persona2.info()
persona2.mayor()