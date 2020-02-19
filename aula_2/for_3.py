
lista = [
    47,
    80,
    50,
    69,
    41,
    50,
    5,
    14,
    14,
    88,
]

# Se for numeros pares multiplica por 2 e insire na lista secundaria e se for impar multiplica por 3 e inseri na lista secundaria

lista_secundaria = []

for numero in lista:
    if numero % 2 == 0:
        lista_secundaria = lista_secundaria + [numero *2]
    else:
        lista_secundaria = lista_secundaria + [numero * 3]

print(lista)
print(lista_secundaria)
