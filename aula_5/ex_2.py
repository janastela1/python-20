
class Usuario:

    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade
    
    def envelhecer(self):
        self.idade = self.idade + 1

    def tirar_habilitacao(self):
        if self.idade > 17:
            print('Estou habitado')
        else:
            print('Ainda faltam ' + str(18 - self.idade) + ' anos')


usuario = Usuario(1, 'José', 10)

while usuario.idade < 18:
    usuario.envelhecer()
    usuario.tirar_habilitacao()


