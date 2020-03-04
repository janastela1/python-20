
string = 'Lucas'
inteiro = 56
flutuante = 12.343
booleano = False

lista = []
dicionario = {}

def getAmbiente():
    return 1, 2, 3, 4
ambiente = getAmbiente()
print(ambiente)

# unpacking
l, s, h, t = ambiente
