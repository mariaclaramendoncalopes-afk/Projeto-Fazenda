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
               print('usuário não encontrado.')
            if pessoas[2] == 'adm': #continua com pessoas porque ainda está dentro do for

                print('---Menu (ADM)---')
                rebanho = []
                animais = ('bovino de leite', 'caprino', 'ovino', 'suíno', 'leitão')
                print(f'Animais da fazenda: {animais}')
                tipo = input('Informe qual o tipo do animal: ').lower()
                if tipo not in animais:
                    while tipo not in animais:
                        print('Este animal não existe na fazenda sertão')
                        tipo = input('Informe qual o tipo do animal: ')
                
                identificação = input('Existe algum tipo de identificação desse animal? (S/N): ').upper()
                if identificação == 'S':
                    identificação = input('Digite como identificar o animal: ')
                else:
                    identificação = 'Não identificavel'
                
                stats = ('lactação','engorda', 'disponível para venda', 'vendido')
                print(f'Status dos animais: {stats}')
                status = input('Informe o status do animal: ').lower()
                if status not in stats:
                    while status not in stats:
                        print('Status não definido')
                        status = input('Informe o status do animal: ')
                rebanho.append([tipo, identificação, status])
                print(rebanho)

            elif pessoas[2] == 'cliente':
                print('cliente')