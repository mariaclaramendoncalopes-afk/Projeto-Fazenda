cadastros = []
adms = [['kamille', '1234'], ['clara', '5678']]
while True:
    print('='*10,   'MENU  PRINCIPAL  |  FAZENDA SERTÃO',   '='*10 )
    print('1 - CADRASTRAR USUÁRIO')
    print('2 - LOGIN')
    print('3 - SAIR')
    print('\n')
    op = int(input('QUAL OPÇÃO VOCÊ DESEJA REALIZAR:   '))

    if op == 1:

        usuario = input('Crie um nome de usuário:  ').lower()

        while True:
            senha = input('Crie sua senha: ')
            
            if len(senha) <= 3:
                print('Senha curta | Deve conter +3 caracteres.\n')
                continue
            elif senha == usuario:
                print('Senha fraca! Não pode conter o mesmo nome do usuário.\n')
                continue
            
            confirmacao = input('Confirme sua senha:')
            print('\n')
            
            if senha != confirmacao:
                print('As senhas não coincidem. Tente novamente.\n')
            else:
                cadastros.append([usuario, senha])
                break

        print('Usuário cadastrado com sucesso! | Faça o login')
        print()
        


    if op == 2:
        usuario = input('Usuário:  ').lower ()
        senha = input('Senha:  ')

        for adm in adms:
            if usuario == adm[0] and senha == adm[1]:
                print('Login ADMIN')
                break
        else:
            for pessoa in cadastros:
                if usuario == pessoa[0] and senha == pessoa[1]:
                    print('Login CLIENTE')
                    break
            else:
                print('Usuário ou senha incorretos')
        break            




#FAZENDO ALTERAÇÕES

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
            # retirar o else, porque msm achando o usuário ele ainda imprime q não encontrou
            #  utilizar só dps dos menus, se não ainda vai aparecer

                if pessoas[2] == 'adm': #continua com 'pessoas' porque ainda está dentro do for
                    # o if dos menus deve estar dentro do if de login para evitar o loop
                    rebanho = []
                    while True:
                        print('---Menu (ADM)---')
                        print('1 - Cadastrar animal no rebanho')
                        op = int(input('Digite o que deseja acessar: '))

                        if op == 1:
                            animais = ('bovino de leite', 'caprino', 'ovino', 'suino', 'leitao')
                            print(f'Animais da fazenda: {animais}')
                            tipo = input('Informe qual o tipo do animal: ').lower()

                            while tipo not in animais:
                                print('Este tipo de animal não existe na fazenda sertão')
                                print(f'Animais da fazenda: {animais}')
                                tipo = input('Informe qual o tipo do animal: ').lower()
                            
                            identificar = ('brinco', 'numero')
                            print(f'Tipos de identificação: {identificar}')
                            identificacao = input('Digite como identificar o animal: ').lower()
                            while identificacao not in identificar:
                                print('Digite uma identificação.')
                                print(f'Tipos de identificação: {identificar}')
                                input('Digite como identificar o animal: ').lower()

                            numero_ID = int(input('Digite o número de identificação do animal: '))
                            
                            stats = ('lactação','engorda', 'disponivel para venda', 'vendido')
                            print(f'Status dos animais: {stats}')
                            status = input('Informe o status do animal: ').lower()

                            while status not in stats:
                                print('Status não definido')
                                print(f'Status dos animais: {stats}')
                                status = input('Informe o status do animal: ').lower()

                            rebanho.append([tipo, identificacao, numero_ID, status])
                            print(rebanho)
                            break

                elif pessoas[2] == 'cliente':
                    print('cliente')
                    break
