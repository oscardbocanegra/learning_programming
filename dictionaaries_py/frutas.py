frutas = {
    'Platano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

fruit = input("¿Qué fruta decea llevar? ").title()
kilos = float(input("Cuantos quilos de esa fruta desea llevar? "))

if fruit in frutas:
    print(kilos, ' de', fruit, ' le van a costar', frutas[fruit]*kilos, 'euros')
else:
    print('lo sentimos pero', fruit, 'no la tenemos en el momento')