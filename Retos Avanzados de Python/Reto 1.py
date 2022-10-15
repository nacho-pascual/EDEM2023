'''Reto 1
Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock almacenado durante meses, se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.
Cada disco (usa un diccionario para esto) tendrá:
Nombre
Artista
Año
Precio
Género (solo pueden ser de los siguientes)
Pop
Electro
Reggaeton
Rock
Metal
Death Metal
Black Metal
Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.
Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final de la compra.
'''
from datetime import datetime

discos_tienda=[
  
{"Nombre":"Trhiller","Artista":"Michael Jackson","Precio":15,"Genero":"Pop"},

{"Nombre":"True","Artista":"Avici","Precio":30,"Genero":"Electro"},

{"Nombre":"Viceversa","Artista":"Rauw","Precio":27,"Genero":"Reggaeton"},

{"Nombre":"The Dark Side","Artista":"Pink Floyd","Precio":35,"Genero":"Rock"},
  
{"Nombre":"Imperial","Artista":"SOEN","Precio":18,"Genero":"Metal"},
  
{"Nombre":"Focus","Artista":"Cynic","Precio":23,"Genero":"Death Metal"},
 
{"Nombre":"Human","Artista":"Death","Precio":40,"Genero":"Black Metal"},

]
print("Buenos días , estos son los discos de los que disponemos en la tienda :")
print(" ")

for idx,disco in enumerate(discos_tienda):
    print(f'Num disco {idx+1}: Nombre: {disco["Nombre"]} Precio: {disco["Precio"]} Genero: {disco["Genero"]}')
print(" ")

print("Introduce el 0 para finalizar tu compra")
print(" ")

eleccion_disco=int(input("Selecciona el disco que quieres comprar marcando su numero :"))
importe_compra=0
ahorro=0
while eleccion_disco!=0:  
  if eleccion_disco==2:
    for i in discos_tienda:
      for key in i:
        if (key=="Genero" and i[key]=="Electro") :
          ahorro+=(i["Precio"]*0.3)
          importe_compra+=(i["Precio"])-(i["Precio"]*0.3)
          print("El Genero seleecionado cuenta con un 30% de descuento")
          eleccion_disco=int(input("Añade otro disco a la cesta marcando su numero :"))
  elif eleccion_disco==7:
    for i in discos_tienda:
      for key in i:
        if (key=="Genero" and i[key]=="Black Metal"):
          ahorro+=(i["Precio"]*0.3)
          importe_compra+=(i["Precio"])-(i["Precio"]*0.3)
          print("El Genero seleecionado cuenta con un 30% de descuento")
          eleccion_disco=int(input("Añade otro disco a la cesta marcando su numero :"))
  elif eleccion_disco>7 or eleccion_disco<0 :
    eleccion_disco=int(input("No existe el disco seleccionado , vuelva a intentarlo porfavor :"))

  else:
    importe_compra+=(discos_tienda[eleccion_disco-1]["Precio"])
    eleccion_disco=int(input("Añade otro disco a la cesta marcando su numero :"))

else:
  print(" ")
  print("Tu compra ha finalizado")
  print(datetime.today())
  print(f"{ahorro} Son lo euros ahorrados")
  print(f"{importe_compra} Es el importe final de la compra")

    
  