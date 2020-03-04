
import sqlalchemy
import sqlalchemy.orm

import core.db

import models.user
import models.message


def create_user(name, email, password):
    user = models.user.User(
        name=name,
        email=email,
        password=password
    )
    try:
        session = core.db.Session()
        session.add(user)
        session.commit()
    except:
        print('Email duplicado')
        exit()
    
def find_user_by_email(email):
    session = core.db.Session()
    return session.query(models.user.User).filter(
        models.user.User.email == email
    ).one()

name = input('Digite seu nome: ')
email = input('Digite seu email: ')
password = input('Digite sua senha: ')

create_user(name, email, password)
user = find_user_by_email(email)
print(user.id)

