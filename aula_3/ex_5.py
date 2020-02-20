
lista = [ 6, 4, 1, 8, 8, 10, 1 ]


def calcular_media(lista_1):
    return sum(lista) / len(lista)


#def multiplicar_por_dois(x):
 #   return x * 2

def multiplicar_tudo_por_dois(lista):
    #return list(map(multiplicar_por_dois, lista))
    return list(map(lambda x: x * 2, lista))

lista_1 = [1,2,3,4,5]

print(lista_1)

# referente a segunda funcao
lista_2 = multiplicar_tudo_por_dois(lista_1)
print(lista_2)

# referente a primeira funcao da media
media = calcular_media(lista_1)
print(media)





