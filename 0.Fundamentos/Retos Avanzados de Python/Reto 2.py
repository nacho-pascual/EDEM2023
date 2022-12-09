'''Reto 2
El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar ("Introducir otro elemento al carrito (Si / No)".
Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.'''
cesta_articulos={}
coste_total_compra=0
introduccion=(input("Desea introducir un elemento al carrito: "))
introduccion.lower()

while introduccion=="si" or introduccion !="no":
  if introduccion=="si":
    articulo=(input("Introduce el nombre del articulo: "))
    precio=(float(input("Introduce el precio del articulo: ")))
    cesta_articulos[articulo]=precio
    coste_total_compra+=precio
    introduccion=(input("Desea introducir un elemento al carrito: "))
  elif introduccion !="no":
    print("Respuesta incorrecta , vuelva a probar: " )
    introduccion=(input("Desea introducir un elemento al carrito: "))
else:
   for key,value in cesta_articulos.items():
      print(key.capitalize(),":",value,"€")
      print(f' El coste total de la compra asciende a {coste_total_compra} €')


  






