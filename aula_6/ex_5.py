import pymongo


client = pymongo.MongoClient()
db = client.projeto

def update_password(email, password):
    db.users.update({
        'email': email
    }, {
        '$set': {
            'password': password
        }
    })

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

update_password(email, password)
