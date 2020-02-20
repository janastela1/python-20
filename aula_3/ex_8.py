
   
def somente_os_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

lista_1 = [ 1, 2, 3, 4, 5, 6 ]

print(lista_1)

lista_2 = somente_os_pares(lista_1)
print(lista_2)