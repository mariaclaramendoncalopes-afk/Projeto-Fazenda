cadastros = []
while True:
    print('--- Fazenda Sertão ---')
    print('1 - criar perfil')
    print('2 - Entrar')
    op = int(input('Qual opção deseja fazer? '))


    if op == 1:

        usuario = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        tipo = input('Digite o tipo de usuário (ADM / Cliente): ').lower()

        if tipo != 'adm' and tipo != 'cliente':
            while tipo != 'adm' and tipo != 'cliente':
                print('Tipo de usuário não definido')
                tipo = input('Digite o tipo de usuário (ADM / Cliente): ').lower()
            cadastros.append([usuario,senha,tipo])
        else:
            cadastros.append([usuario,senha,tipo]) #lista dentro de lista, usuario = 0, senha = 1, tipo = 2
        print(cadastros)

    elif op ==2:

        print('--- Bem-vindo(a) de volta ---')
        usuario_entrar = input('Digite seu usuário: ')
        senha_entrar = input('Digite sua senha: ')
        usuario_encontrado = False

        for pessoas in cadastros:
            if usuario_entrar == pessoas[0] and senha_entrar == pessoas[1]:
                usuario_encontrado = True
                print(f'bem-vindo(a), {pessoas[0]}')
            else:
                if cadastros == []:
                    print('Não há nenhum usuário cadastrado.')
                elif usuario_encontrado == False:
                    print('usuário não encontrado.')
            if pessoas[2] == 'adm': #continua com pessoas porque ainda está dentro do for
                print('adm')
            else:
                print('cliente')