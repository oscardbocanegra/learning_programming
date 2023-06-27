class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad} unidades. Saldo actual: {self.saldo}")
            else:
                print("Saldo insuficiente.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")
    
    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


# Ejemplo de uso
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.consultar_saldo()  # Saldo actual: 1000

cuenta.depositar(500)  
cuenta.retirar(200)  

cuenta.consultar_saldo()  
    
print("-----------------------------------")

persona = CuentaBancaria("Oscar Bocanegra", 10000000)
persona.consultar_saldo()
persona.depositar(1)
persona.retirar(50000)
persona.consultar_saldo()