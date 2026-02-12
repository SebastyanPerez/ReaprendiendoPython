nombre=input('Ingreso tu nombre:')


if len(nombre)<3:
    print('El nombre es muy corto')
else:
    print('El nombre es válido')


name_lista=['sebastian','allizon','yaretzi','norma','mike']

        
for name in name_lista:
    print('Hola',name,'¡Bienvenido!-tienes',len(name),'letras')


dato=input('Ingresa un dato:')

if len(dato)<1:
    print('no ingresaste ningun dato')
else:
    print('Ingresaste el dato:',dato ,'que tiene',len(dato),'letras')

lista_vacia=[]

input_usuario=input('Ingresa un dato para agregar a la lista:')

lista_vacia.append(input_usuario)
print('La lista ahora contiene:',lista_vacia)
print('El dato ingresado tiene',len(input_usuario),'letras')