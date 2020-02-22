
class Usuario:

    #id = 1
    #nome = 'Janaina Stela'
    #idade = 26


    def __init__(self, id, nome, idade): # o self 'e ele mesmo e o usuario
        self.id = id
        self.nome = nome
        self.idade = idade


usuario = Usuario(id = 1, nome='lucas', idade=26) #propriedade estao na instancia e cada usuario e uma instancia da classe 
usuario_2= Usuario(id=2,nome = 'Cary', idade=0)


print(usuario.id)
print(usuario.nome)
print(usuario.idade)
