'''Reto 9
Escribe una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.'''
#Convertir Decimal en Binario
def conversor_binarios(x):
  numero_binario=format(x,"b")
  return numero_binario
    
print(conversor_binarios(5))

#Convertir Binario en Decimal

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal



print(binario_a_decimal('101'))

#Convertir Binario en Decimal otra forma
#Convertimos el entero en una cadena y despeas lo pasamos a binario.
#Base 2.

b = 101
print(int(str(b), 2))
