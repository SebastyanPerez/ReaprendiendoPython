contador_posi=0
contador_nega=0

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
            if numero>0:
                contador_posi+=1
            elif numero<0:
                contador_nega+=1
            else:
                print('El numero es cero, no se contara como positivo ni negativo')
        case 2:
            print(f'Cantidad de numeros positivos ingresados: {contador_posi}')
            print(f'Cantidad de numeros negativos ingresados: {contador_nega}')
        case 3:
            print('Has seleccionado salir')
        case _:            
            
            print('Opcion no valida, por favor selecciona una opcion del menu')