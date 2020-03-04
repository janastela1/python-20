
def calcular_media(lista):
    try:
        soma, contador = 0, 0
        for numero in lista:
            soma, contador = soma + numero, contador + 1
        return soma / contador
    except ZeroDivisionError:
        return None

resultado = calcular_media([ 1, 2, 3, 4, 5 ])
print(resultado)
