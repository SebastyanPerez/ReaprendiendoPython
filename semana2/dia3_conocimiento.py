contadorP=0
contadorN=0

entrada=1

while entrada !=0:
    entrada=int(input('Ingresa un numero (para salir ingresa cero): '))

    if entrada>0:
        contadorP+=1
    elif entrada<0:
        contadorN+=1

print('Has salido del programa')
print('La cantidada de numeros positivos ingresado es:',contadorP)
print('La cantidada de numeros negativos ingresado es:',contadorN)