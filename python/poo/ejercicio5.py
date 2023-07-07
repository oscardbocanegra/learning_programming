#Crea una clase "Vehículo" con atributos de marca, modelo y año. 
#Agrega métodos para obtener la información del vehículo y determinar si es antiguo (más de 20 años) o no.

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def informacion(self):
        return f"La marca del carro es: {self.marca} \nEl modelo es: {self.modelo}\nEl año es {self.año}"
    
    def antiguo(self):
        if(self.año <= 2003):
            print("El carro es modelo antiguo")
        else:
            print("El carro es modelo moderno")
    
vehiculo1 = Vehiculo("Mazda", "Mazda 3", 2003)
info = vehiculo1.informacion()
print(info)

model = vehiculo1.antiguo()
print(model)