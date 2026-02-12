contado=0
acumulador=0

variable=1

while variable !=0:

    variable=int(input('Ingresa un numero (para salir ingresa cero): '))
    if variable >0:
        contado+=1
        acumulador+=variable
    elif variable <0:   
        print('El numero ingresado es negativo')

print('Has salido del programa')
print('La cantidad de numeros positivos ingresados es: ', contado)
print('El acumulado de los numeros positivos es: ', acumulador)