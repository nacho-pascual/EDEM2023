'''Reto 4
Escribe un programa que almacene lenguajes de programación en una lista.
El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá responder "sí" o "no" y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la misma pregunta:
¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes de la lista.
Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce o no. Algo así:
JavaScript: no
TypeScript: sí
Python: sí
Dart: no'''

lista_lenguajes=[["JavaScript"],["TypeScript"],["Python"],["Dart"]]


for i in range(len(lista_lenguajes)):
    if i==0:
        lista_lenguajes[i].append(input("Conoces el lenguaje  JavaScript, introduce si o no: "))
    elif i==1:
        lista_lenguajes[i].append(input("Conoces el lenguaje TypeScript, introduce si o no: "))    
    elif i==2:
        lista_lenguajes[i].append(input("Conoces el lenguaje Python, introduce si o no: "))
    else:
        lista_lenguajes[i].append(input("Conoces el lenguaje Dart, introduce si o no: "))

for i in range(len(lista_lenguajes)):
    print(f'{lista_lenguajes[i][0]} : {lista_lenguajes[i][1]}')
