import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)  # La computadora elige un número entre 1 y 100
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100. ¡Adivina cuál es!")

    while True:
        intentos += 1
        intento = int(input("Introduce tu adivinanza: "))

        if intento < numero_secreto:
            print("Mi número es mayor. ¡Inténtalo de nuevo!")
        elif intento > numero_secreto:
            print("Mi número es menor. ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

if __name__ == "__main__":
    juego_adivinanza()