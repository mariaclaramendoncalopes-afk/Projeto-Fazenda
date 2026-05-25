def mostrar_linha():
    print('.__________.__________.__________.__________.')


usuarios = [
    ['kamille', '1234', True],
    ['clara', '5678', True],
    ['teste', '0000', False],
]


def Cadastro_ADM():
        print('     |  CADASTRO ADM  |\n')

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





def Menu_Inicial():
    while True:
        mostrar_linha()
        print('''
    (1)  -  Cadastrar Administrador'
    (2)  -  Cadastrar Usuário'
    (3)  -  Login'
    (0)  -  Encerrar Programa
        ''')

        op = input('Digite qual opção deseja realizar:  ')

        if op == 0:
            break  #colocar opção bonitinha pra encerrar programa

        elif op == '1':
            Cadastro_ADM()

        elif op == '2':
            print('Cadastro usuários')

        elif op == '3':
            print('login')

        #colocar um else, caso for inválido

        



Menu_Inicial()
