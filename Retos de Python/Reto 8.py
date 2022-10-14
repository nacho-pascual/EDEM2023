'''Reto 8
Escribe una función que reciba un número entero positivo y devuelva su factorial.'''

def factorial(x:int):
  facorial=1
  for i in range(1,x+1):
    facorial*=i
  return facorial
  
print(factorial(5))
