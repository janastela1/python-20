
# encontrar somente os usuarios que tem o cpf informado

usuarios  = [

    {
        'id' : 1 ,
        'email' : 'user_1@email.com' ,
        'pagou_conta' : falso
    }

]

def  filtro ( usuario ):
    se  usuario [ 'pagou_conta' ] ==  True :
        retornar  falso
    return  True

def  filtar_usuarios ( lista ):
     lista de retorno ( filtro ( filtro , lista ))



