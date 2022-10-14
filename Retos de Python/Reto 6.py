'''Reto 6
Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo**
** Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda'''

palabra=(input("Introduce una palabra por consola para ver si es un palindromo: "))

lista=list(palabra)
x = list(reversed(palabra))
print(lista)
print(x)
if lista==x:
  print("Es un palindromo")
else:
  print("No un palindromo")