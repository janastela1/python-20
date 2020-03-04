
import sqlalchemy
import sqlalchemy.orm

import core.db

import models.user
import models.message


core.db.Base.metadata.create_all(
    core.db.engine
)

user = models.user.User(
    name='Lucas Ricciardi', 
    email='lucas2@email.com', 
    password='admin'
)

session = core.db.Session()
session.add(user)
session.commit()

session = core.db.Session()
results = session.query(models.user.User).filter()

for user in results:
    message = models.message.Message(
        content='Minha mensagem',
        user=user.id
    )
    session = core.db.Session()
    session.add(message)
    session.commit()

