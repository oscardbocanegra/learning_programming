#Implementa una clase "Pila" que simule una pila (LIFO). 
#Incluye métodos para agregar elementos a la pila, retirar 
# elementos de la pila y verificar si está vacía.

class Pila:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def agregar_elemento(self, elemento):
        self.pila.append(elemento)

    def retirar_elemento(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return None

pila = Pila()
print(pila.esta_vacia())  # Output: True

pila.agregar_elemento(1)
pila.agregar_elemento(2)
pila.agregar_elemento(3)

print(pila.retirar_elemento())  # Output: 3
print(pila.retirar_elemento())  # Output: 2
print(pila.retirar_elemento())  # Output: 1
print(pila.retirar_elemento())  # Output: None

print(pila.esta_vacia())