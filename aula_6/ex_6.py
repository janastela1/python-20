import pymongo


client = pymongo.MongoClient()
db = client.projeto

def find_by_email(email):
    return db.users.find_one({
        'email': email
    })

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

user = find_by_email(email)

if user:
    if password == user['password']:
        print('Autenticado')
    else:
        print('Algo de errado aconteceu')


