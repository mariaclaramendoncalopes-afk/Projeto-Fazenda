usuarios = [
    ['kamille', '1234', True],
    ['clara', '5678', True],
    ['teste', '0000', False],
]

# tipo,  ID,  status,  peso,  idade,  sexo,  valor,  produção diária,  vacinado,  observações
rebanho = [
    ['bovino', '001', 'lactação', '500', '4', 'F', '5000', '22', 'sim', ''],
    ['bovino', '002', 'venda', '460', '5', 'F', '4500', '19', 'sim', ''],
    ['bovino', '003', 'venda', '490', '5', 'F', '4700', '20', 'sim', ''],

    ['caprino', '100', 'lactação', '55', '3', 'F', '900', '3', 'sim', ''],
    ['caprino', '101', 'venda', '60', '4', 'F', '1000', '4', 'sim', ''],

    ["ovino", "200", "venda", "70", "3", "M", "1300", "0", "nao", ""],
    ["ovino", "201", "lactação", "60", "4", "F", "1100", "2", "sim", ""],

    ["galinha", "401", "producao", "3", "1", "F", "50", "1", "sim", ""],
    ["galinha", "402", "producao", "2", "1", "F", "45", "1", "sim", ""],
    ["galinha", "403", "producao", "2", "2", "F", "55", "1", "sim", ""],
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

            existe = False

            for pessoa in usuarios:
                if pessoa[0] == usuario:
                    existe = True
                    print(' Já existe usuário com este nome, tente novamente.\n')
                    break

            if not existe:
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

            existe = False

            for pessoa in usuarios:
                if pessoa[0] == usuario:
                    existe = True
                    print(' Já existe usuário com este nome, tente novamente.\n')
                    break

            if not existe:
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

    if op == '3':
        print('\n     |  lOGIN  |     \n')
        usuario = input(' Usuário:  ').lower ()
        senha = input(' Senha:  ')

        for pessoa in usuarios:
            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == True:
                while True:
                    print('='*10, '     MENU ADM     |     FAZENDA SERTÃO     ', '='*10)
                    print('\n')
                    print(' '*18,   f'Bem vindo(a), {usuario}\n')
                    print(' 1  -  Cadastrar animal no rebanho')
                    print(' 2  -  Buscar animal')
                    print(' 3  -  Modificar dados do animal')
                    print(' 4  -  Retirar animal da lista')
                    print(' 5  -  Gerenciar produção e derivados')
                    print(' 6  -  Relatório')
                    print(' 7  -  Sair\n')

                    op = input('Digite uma opção:  ')

                    if op == '1':
                        print('\n           |  CADASTRAR ANIMAL NO RABANHO  |\n')
                        animais_d = ['bovino', 'caprino', 'ovino', 'galinha']
                        print(f' Tipos disponíveis:  {animais_d}')
                        tipo = input(' Informe qual o tipo de animal:  ').lower ()

                        if tipo not in animais_d:
                            criar_tipo = input('Esse tipo não existe. Deseja cadastrá-lo  (s/n)?  ').lower ()

                            if criar_tipo == 's':
                                animais_d.append(criar_tipo)
                                print(' Novo tipo adicionado!\n')
                            else:
                                print('Cadastro cancelado.\n')
                                continue
                        
                        while True:
                            id = input(f'Digite um novo ID para ({tipo}):  ')

                            repetido = False

                            for animal in rebanho:
                                if animal[1] == id:
                                    repetido = True
                                    print(' Esse ID já existe, tente outro.')
                                    break

                            if not repetido:
                                break






                    break
                break





            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == False:
                print('Menu cliente')
                break





        else:
            print('\n Usuário não encontrado \n')



    if op == '4':
        print('\n Encerrando o sistema... \n')
        print(' Salvando dados...')
        print(' Finalizando conexões... ')
        print('\n Sistema encerrado com sucesso. Até logo! ')
        break