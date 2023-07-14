def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))

print("Números primos en el rango de", inicio, "a", fin, ":")

for num in range(inicio, fin + 1):
    if es_primo(num):
        print(num)