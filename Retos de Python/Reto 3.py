'''Reto 3
El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:
si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
si la persona es menor de 16 años, no tiene que pagar impuestos
Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de personas** durante un año entero (12 meses)'''
lista_personas=[
  {"Nombre":"Juan","Edad":16,"Ingresos":1000},
  {"Nombre":"Pedro","Edad":18,"Ingresos":700},
  {"Nombre":"Antonio","Edad":37,"Ingresos":1800},
  {"Nombre":"Federico","Edad":45,"Ingresos":3000},
  {"Nombre":"Juan","Edad":72,"Ingresos":1000}
]
impuestos_a_pagar=0
endeudamiento=0
meses=12

for x in range(len(lista_personas)):
  if lista_personas[x]["Edad"]>16 and lista_personas[x]["Edad"]<70:
    if lista_personas[x]["Ingresos"]<=800:
      endeudamiento+= (lista_personas[x]["Ingresos"]*0.1)
    elif lista_personas[x]["Ingresos"]>800 and lista_personas[x]["Ingresos"]<2000:
      impuestos_a_pagar+= (lista_personas[x]["Ingresos"]*0.3)
    elif lista_personas[x]["Ingresos"]>2000:
        impuestos_a_pagar+= (lista_personas[x]["Ingresos"]*0.5)
  else:
    impuestos_a_pagar+=0

print(f'El conjunto de impuestos a pagar mensualmente es de {impuestos_a_pagar} € y el endeudamiento es de {endeudamiento}')



