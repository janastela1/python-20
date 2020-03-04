import psycopg2
import psycopg2.extras


connection = psycopg2.connect(
    user='admin',
    password='4linux',
    host='localhost',
    port=5432,
    database='projeto'
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def create_user(name,email,password):
    cursor.execute('''

    INSERT INTO users (name,email,password) 

    VALUES (\'{}\',\'{}\',\'{}\');

    '''.format(name,email,password))
    return connection.commit()

name = input('Digite o nome: ')
email = input('Digite seu email: ')
password = input('Digite seu password: ')

users = create_user(name,email,password)

print(users)