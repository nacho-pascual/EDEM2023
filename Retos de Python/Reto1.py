discos_tienda=[
  
{"Nombre":"Trhiller","Artista":"Michael Jackson","Precio":15,"Genero":"Pop"},

{"Nombre":"True","Artista":"Avici","Precio":30,"Genero":"Electro"},

{"Nombre":"Viceversa","Artista":"Rauw","Precio":27,"Genero":"Reggaeton"},

{"Nombre":"The Dark Side of the Moon","Artista":"Pink Floyd","Precio":35,"Genero":"Rock"},
  
{"Nombre":"Imperial","Artista":"SOEN","Precio":18,"Genero":"Metal"},
  
{"Nombre":"Focus","Artista":"Cynic","Precio":23,"Genero":"Death Metal"},
 
{"Nombre":"Human","Artista":"Death","Precio":40,"Genero":"Black Metal"},

]

#Bucle para imprimir por consola los discos del usuario
for idx,disco in enumerate(discos_tienda):
    print(idx+1,disco)

#Bucle para que el usuario seleccione un disco
for idx,disco in enumerate(discos_tienda):
    print(f'Num disco {idx+1}: Nombre: {disco["Nombre"]} Precio: {disco["Precio"]} Genero: {disco["Genero"]}')


