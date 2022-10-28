'''Reto 7
Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios. Al finalizar, deberá mostrar por consola la media de los precios introducidos.'''

lista_precios=[]

for i in range(5):
  lista_precios.append(int(input("Introduce un numero en la lista: ")))

suma_total=0


for i in lista_precios:
  suma_total+=i
  
media=(suma_total/5)  
print(f'La media de los datos introducidos es : {media}')