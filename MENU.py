usuarios = [
    # nome, senha, eh_admin
    ['kamille', '1234', True],
    ['clara', '5678', True],
]

while True:
    print('='*10,   'MENU  PRINCIPAL  |  FAZENDA SERTÃO',   '='*10)
    print('1 - CADRASTRAR USUÁRIO')
    print('2 - LOGIN')
    print('3 - SAIR')
    print('\n')
    op = input('QUAL OPÇÃO VOCÊ DESEJA REALIZAR:   ')

    if op == '1':
        usuario = input('Crie um nome de usuário:  ')

        while True:
            senha = input('Crie sua senha: ')

            if len(senha) <= 3:
                print('Senha curta | Deve conter +3 caracteres.\n')
                continue

            if senha == usuario:
                print('Senha fraca! Não pode conter o mesmo nome do usuário.\n')
                continue

            confirmacao = input('Confirme sua senha:')
            print('\n')

            if senha != confirmacao:
                print('As senhas não coincidem. Tente novamente.\n')
                continue

            usuarios.append([usuario, senha, False])
            break

        print('Usuário cadastrado com sucesso! | Faça o login')
        print()

    if op == '2':
        usuario = input('Usuário:  ').lower()
        senha = input('Senha:  ')

        for usuario in usuarios:
            if usuario == usuario[0] and senha == usuario[1] and usuario[2] == True:
                print('Login ADMIN')
                break
            if usuario == usuario[0] and senha == usuario[1] and usuario[2] == False:
                print('Login')
                break
        
        print('Usuário não encontrado')


# FAZENDO ALTERAÇÕES
'''

        if tipo != 'usuario' and tipo != 'cliente':
            while tipo != 'usuario' and tipo != 'cliente':
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
            if pessoas[2] == 'usuario': #continua com pessoas porque ainda está dentro do for

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
                '''
