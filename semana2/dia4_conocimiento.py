menu=0

while menu !=3 :
    print('Bienvenido al menu')
    print('1. Opcion Saludo')
    print('2. Opcion Despedida')
    print('3. Salir')

    menu=int(input('Selecciona una opcion: '))

    match menu:
        case 1:
            print('Hola,que tal?')
        case 2:
            print('Adios, que tengas un buen dia!')
        case 3:
            print('Has seleccionado salir')         
        case _:
            print('Opcion no valida, por favor selecciona una opcion del menu')
    