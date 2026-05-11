#testando o menu de cadastro:
usuarios = [
    ['kamille', '1234', True],
    ['clara', '5678', True],
    ['teste', '0000', False],
]

while True:
    print('-'*10,'     MENU PRINCIPAL   |   FAZENDA SERTÃO     ','-'*10)
    print('\n')
    print('1 - Cadastrar administrador')
    print('2 - Cadastrar usuário')
    print('3 - Login')
    print('4 - Sair')
    print('\n')
    op = input('Digite a opção que deseja realizar:  ')
    
    if op == '1':
        print('     |  CADASTRO ADM  |     \n')

        while True:
            usuario = input(' Digite um novo usuário:  ').lower()

            for pessoa in usuarios:
                if pessoa[0] == usuario:
                    print(' Já existe usuário com este nome, tente novamente.\n')
                    break

            else:
                break

        while True:
            senha = input(' Crie sua senha:  ')

            if len(senha) <= 3:
                print(' Senha curta | Sua senha deve conter +3 caracteres ')
                continue
            
            if senha == usuario:
                print(' Senha fraca! Senha não pode ser igual ao usuário ')
                continue

            confirmacao = input(' Confirme sua senha:  ')
            print('\n')

            if senha != confirmacao:
                print(' As senhas não coincidem. Tente novamente. \n')
                continue

            usuarios.append([usuario, senha, True])
            break

        print(' ADM cadastrado com sucesso!  |  Realize o login ')
        print('\n')

    if op == '2':
        print('     |  CADASTRO CLIENTE  |     \n')

        while True:
            usuario = input(' Digite um novo usuário:  ').lower()

            for pessoa in usuarios:
                if pessoa[0] == usuario:
                    print(' Já existe usuário com este nome, tente novamente.\n')
                    break
            else:
                break

        while True:
            senha = input(' Crie uma senha:  ')

            if len(senha) <= 3:
                print(' Senha curta | Sua senha deve conter +3 caracteres ')
                continue

            if senha == usuario:
                print(' Senha fraca! Senha não pode ser igual ao usuário ')
                continue

            confirmacao = input(' Confirme sua senha:  ')

            if senha != confirmacao:
                print(' As senhas não coincidem. Tente novamente. \n')
                continue

            usuarios.append([usuario, senha, False])
            break
        
        print(' CLIENTE cadastrado com sucesso!  |  Realize o login ')
        print('\n')

    if op == '4':
        print('\n Encerrando o sistema... \n')
        print(' Salvando dados...')
        print(' Finalizando conexões... ')
        print('\n Sistema encerrado com sucesso. Até logo! ')
        break