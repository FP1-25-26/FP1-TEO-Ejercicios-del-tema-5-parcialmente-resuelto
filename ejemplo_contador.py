lista_letras = [
    "a", "a", "b", "c", "b", "j", "b"
]

contador = {}
for letra in lista_letras:
    if letra not in contador:
        contador[letra] = 0
    contador[letra] = contador[letra] + 1
print(contador)

from collections import Counter

contador = Counter(lista_letras)
print(contador)

print(contador.most_common())

contador.most_common(2)
#contador.most_common()[:2]