
# Exercicio 4

emails = [
	'petyfezygniyg@msddvqiytmpogire',
	'yjozbkgirsfchbjtlnigqqeohaj',
	'axukkfdcpemkruogaemqlcyfngun',
	'czmymzvhdyfltqe@rktzjljbs',
	'@yoeisikhawyno@b',
	'dfeydhfnlydwrlvpmsomi',
	'xogsqaxph@btippxiz',
	'hxkuqlyxreuwfzwypvw',
	'togaczelhzijnafhyg@czp@f',
	'jxtmqikapfv@uqqckowiz@hyi',
]


def verificar_se_e_email(email):
    contador = 0
    for letra in email:
        if letra == '@':
            contador = contador + 1
    if contador == 1:
        return True
    return False

for email in emails:
    if verificar_se_e_email(email):
        print('e um mail')
    else:
        print('num é não')