person = {}
continuar = True
while continuar:
    info = input('What personal info do you want to introduce?')
    result = input(info + ': ')
    person[info] = result
    print(person)
    continuar = input('Do you want to add more information?(Yes/No)') == 'Yes'