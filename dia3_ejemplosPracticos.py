# primer ejercicio

nota=input('Ingresa la nota del estudiante: ')

if float(nota)>=11.0:
    print('El estudiante esta aprobado')
else:
    print('El estudiante esta reprobado')

# ejercicio dos

temperatura=input('Ingresa la temperatura actual:')

if float(temperatura)>30.0:
    print('Hace calor')
elif float(temperatura) >=15.0 and float(temperatura)<=30.0:
    print('El clima es agradable')
else:
    print('Hace frio')
