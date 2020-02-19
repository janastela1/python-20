
# imprimi os numeros de 10 ate 90
for i in range(10,99):
    print(i)


# Faca uma media da lista

lista = [1,2,3,4,5,6,7,8,9]

soma = 0  #zero, porque 'None' nao da para fazer contagem matematica e dai faz 0+1, 1+2...total 45
contador = 0

for numero in lista:
    soma = soma + numero
    contador = contador + 1

media = soma/contador

print(media)


