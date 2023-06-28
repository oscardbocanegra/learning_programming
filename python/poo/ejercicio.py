# Crea una clase "Estudiante" con atributos de nombre,
# edad y calificaciones. Agrega métodos para calcular
# el promedio de calificaciones y determinar si el 
# estudiante está aprobado (promedio mayor o igual a 60).

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
    
    def calcular_promedio(self):
        total_calificaciones= sum(self.calificaciones)
        promedio = total_calificaciones / len(self.calificaciones)
        return promedio
    
    def aprobado(self):
        promedio = self.calcular_promedio()
        if promedio >= 60:
            print("Tu estas aprobado con un promedio de " + str(promedio))
        else:
            print("Tu no has aprobado, tu promedio es de " + str(promedio))
        
        
#Estudiante aprobado 
estudiante1 = Estudiante("Oscar", 19, [80, 75, 90, 60, 85])
#Estudiante no aprobado 
# estudiante1 = Estudiante("Oscar", 19, [10, 75, 10, 60, 85])

estudiante1.calcular_promedio()
estudiante1.aprobado()
        