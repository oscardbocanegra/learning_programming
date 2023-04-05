name = input('Cual es tu nombre? ')
edad = input('Cual es tu edad? ')
direccion = input('Cual es tu direccion? ')
telefono = input('Cual es tu telefono? ')

# En la siguiente linea de codigo lo que vamos a 
# hacer es definir ya el diccionario guardando la
# informacion que el usuario nos dio.

informacion = {
    'nombre': name,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

# Lo que vamos a hacer ahora es imprimir la
# informacion del usuario en un texto completo.

print(informacion['nombre'], 'tiene', informacion['edad'], 'años, vie en', informacion['direccion'], 'y su número de teléfono es', informacion['telefono'])