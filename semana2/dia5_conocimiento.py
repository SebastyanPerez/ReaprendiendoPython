contador=0
menu=0

while menu !=3 :
    print('Bienvenido al menu')
    print('1. Ingrese un numero')
    print('2. Mostrar el contador')
    print('3. Salir')

    menu=int(input('Selecciona una opcion: '))

    match menu:
        case 1:
            numero=int(input('Ingrese el numero:'))
            contador+=1
            print('Número registrado.')
        case 2:
            print('El contador actual es:',contador)
            
        case 3:
            print('Has seleccionado salir')
            
        case _:
            print('Opcion no valida, por favor selecciona una opcion del menu') 
            
    