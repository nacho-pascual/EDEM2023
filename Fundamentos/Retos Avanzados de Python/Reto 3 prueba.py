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
  {"Nombre":"Jose Luis","Edad":72,"Ingresos":1000}
]

meses=12
endeudamiento_total=0
for x in range(len(lista_personas)):
  impuestos_a_pagar=0
  endeudamiento=0
  if lista_personas[x]["Edad"]>16 and lista_personas[x]["Edad"]<70:
    if lista_personas[x]["Ingresos"]<=800:
      endeudamiento+= (lista_personas[x]["Ingresos"]*0.1)
      print(f'{lista_personas[x]["Nombre"]} tiene que pagar {impuestos_a_pagar} € y su endeudamiento es de {endeudamiento} €')
      endeudamiento_total+=endeudamiento*12
    elif lista_personas[x]["Ingresos"]>800 and lista_personas[x]["Ingresos"]<2000:
      impuestos_a_pagar+= (lista_personas[x]["Ingresos"]*0.3)
      print(f'{lista_personas[x]["Nombre"]} tiene que pagar {impuestos_a_pagar} €')
      endeudamiento_total+=endeudamiento*12
    elif lista_personas[x]["Ingresos"]>2000:
        impuestos_a_pagar+= (lista_personas[x]["Ingresos"]*0.5)
        print(f'{lista_personas[x]["Nombre"]} tiene que pagar {impuestos_a_pagar} €')
        endeudamiento_total+=endeudamiento*12

  else:
    impuestos_a_pagar+=0
    print(f'{lista_personas[x]["Nombre"]} tiene que pagar {impuestos_a_pagar} €')


print(endeudamiento_total)


