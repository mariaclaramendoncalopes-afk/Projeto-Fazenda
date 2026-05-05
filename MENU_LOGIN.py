usuarios = []

while True:
    print('='*10,   'MENU  PRINCIPAL  |  FAZENDA SERTÃO',   '='*10)
    print('1 - CADRASTRAR ADM')
    print('2 - CADRASTRAR USUÁRIO')
    print('3 - LOGIN')
    print('4 - SAIR')
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

            usuarios.append([usuario, senha, True])
            break

        print('ADM cadastrado com sucesso! | Faça o login')
        print('\n')
    if op == '2':
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
        print('\n')

    if op == '3':
        usuario = input('Usuário:  ').lower()
        senha = input('Senha:  ')

        for pessoa in usuarios:
            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == True:
                print('Login ADMIN')
                break
            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == False:
                print('Login CLIENTE')
                break
        else:
            print('Usuário não encontrado')

    if op == '4':
        print('\nEncerrando sistema...')
        print('Salvando dados...')
        print('Finalizando conexões...')
        print('\nSistema encerrado com sucesso. Até logo!')
        break