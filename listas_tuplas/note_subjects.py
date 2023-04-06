#Agregamos una lista con las asignaturas.
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#indicamos una variable en forma de tupla donde vamos a guardar las notas 
scores = []

#recorremos la lista preguntando por la nota que se saco en cada
#asignatura y la almacenamos en la variable score.
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    #Agregamos la nota a scores
    scores.append(score)
    
#Imprimimos el nombre de la materia junto con la nota
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])