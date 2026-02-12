# estructuras repetitivas 
inicio=1
fin =5

for i in range(inicio,fin+1):
    print('EL primer valor es:',i)


numero=int(input('Ingresa un numero para ver su lista: '))

if numero>0:
    for j in range(1,numero+1):
        print('El numero es:',j)
else:
    print('El numero no es valido o es negativo')            