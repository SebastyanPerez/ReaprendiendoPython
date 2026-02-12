acumulador=0
menu=0

while menu !=3:
    print('Bienvenido al menu')
    print('1. Ingresar numero')
    print('2. Mostrar resultados')
    print('3. Salir')
    menu=int(input('Selecciona una opcion: '))

    match menu:
        case 1:
            numero=int(input('Ingresa un numero:'))
            acumulador+=numero
        case 2:
            print(f'La suma de los numeros ingresados es: {acumulador}')
        case 3:
            print('Has seleccionado salir')
        case _:
            print('Opcion no valida, por favor selecciona una opcion del menu')