# (expresion_resultado for variables in iterable if condicion)

lista = [10, 20, 30]

for elem in lista: # puedo usar lista en for porque es ITERABLE
    print(elem)

generador = (n*2 for n in lista) #generador ES ITERABLE
for elem in generador:
    print(elem)
