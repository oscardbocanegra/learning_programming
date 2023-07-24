#Crear una clase Empleado con atributos nombre, salario y años_antiguedad,
#y un método para calcular el aumento de salario según la antigüedad.

class Empleado:
    def __init__(self, nombre, salario, años_antiguedad):
        self.nombre = nombre
        self.salario = salario
        self.años_antiguedad = años_antiguedad
            
    def nombre(self):
        return "El empleado es: " + self.nombre
    
    def salario(self):
        return "El salario del empleado es: " + self.salario
    
    def antiguedad(self):
        return "La antiguedad del empleado es de: " +  self.años_antiguedad
    
    def calcular_aumento_salario(self):
        aumento_por_antiguedad = 0.03 * self.años_antiguedad  # Supongamos un aumento del 3% por año de antigüedad
        nuevo_salario = self.salario + (self.salario * aumento_por_antiguedad)
        return nuevo_salario
    

empleado1 = Empleado("Juan Perez", 2500, 3)

# Calcular el aumento de salario según la antigüedad
nuevo_salario_empleado1 = empleado1.calcular_aumento_salario()

# Imprimir el nuevo salario
print(f"El nuevo salario de {empleado1.nombre} es: ${nuevo_salario_empleado1:.2f}")