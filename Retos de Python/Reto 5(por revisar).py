'''Reto 5
Escribe un programa que realice lo mismo que el programa del reto 4, pero que elimine de la lista aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce'''


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
  if lista_lenguajes[i][1] == 0:
    lista_lenguajes.pop(i)
    print(f'{lista_lenguajes[i][0]} : {lista_lenguajes[i][1]}')

