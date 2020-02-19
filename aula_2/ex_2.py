
#Exercicio 2 
# Verificar se tem letra na idade

idade = input('Digite sua idade: ')

numerais = ['0','1','2','3','4','5','6','7','8','9']

for letra in idade:
    if letra in numerais:
        print('Digitou um numero')
    else:
        print('Digitou um caractere nao numerico')
    
    
