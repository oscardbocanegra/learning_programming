#Escribir un programa que pregunte al usuario los números ganadores de la lotería 
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

#definimos una variable que contenga un array 
numbers = []

#recorremos la lista las veces que le indicamos en el range para obtener los numeros ganadores
for i in range(6):
    numbers.append(int(input("Cuales son los numero ganadores de la loteria? ")))
    
#con el .sort() estamos indicando que la lista se va ordenar
numbers.sort()
print("Los numeros ganadores son: " + str(numbers))
    

