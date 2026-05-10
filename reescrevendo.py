usuarios = [
    ['kamille', '1234', True],
    ['clara', '5678', True],
    ['teste', '0000', False],
]

# tipo,  ID,  status,  peso,  idade,  sexo,  valor,  produto, produção diária,  vacinado,  observações
rebanho = [
    ['bovino', '001', 'lactação', '500', '4', 'F', '5000', 'leite bovino', '22', 'sim', ''],
    ['bovino', '002', 'venda', '460', '5', 'F', '4500', 'leite bovino', '19', 'sim', ''],
    ['bovino', '003', 'venda', '490', '5', 'F', '4700', 'leite bovino', '20', 'sim', ''],

    ['caprino', '100', 'lactação', '55', '3', 'F', '900', 'leite caprino', '3', 'sim', ''],
    ['caprino', '101', 'venda', '60', '4', 'F', '1000', 'leite caprino', '4', 'sim', ''],

    ['ovino', '201', 'lactação', '60', '4', 'F', '1100', 'leite ovino', '2', 'sim', ''],

    ['galinha', '401', 'producao', '3', '1', 'F', '50', 'ovos', '1', 'sim', ''],
    ['galinha', '402', 'producao', '2', '1', 'F', '45', 'ovos', '1', 'sim', ''],
]

producao_diaria = [
    ["01/06", "22", "2"],
]

#nome, kilos, valor do kilo
estoque_derivados = [
    ["queijo coalho", "5", "24", "120"],
    ["queijo manteiga", "4", "37.5", "150"],
    ["requeijão", "3", "30", "90"]
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

                            for animal in rebanho:
                                if animal[1] == id:
                                    print(' Esse ID já existe, tente outro.')
                                    break

                            else:
                                break

                        status = input('Status do animal:  ').lower ()
                        peso = input('Peso do animal:  ')
                        idade = input('Idade do animal:  ')
                        sexo = input('Sexo do animal:  (F/M)?  ').upper ()
                        valor = input('Valor do animal:  ')
                        produto = input('O que ele produz:  ').lower ()
                        producao = input('Quanto esse animal produz por dia:  ')
                        vacinado = input('É vacinado?  (s/n)?  ').lower ()
                        observacoes = input('Observações: (caso não tenha, deixe o espaço vazio)  ').lower ()

                        rebanho.append([tipo, id, status, peso, idade, sexo, valor, produto, producao, vacinado, observacoes])

                        print(f'\nAnimal | {tipo} | cadastrado com sucesso!!\n')

                        repetir = input('Deseja cadastrar outro animal?  (s/n)  ').lower ()

                        if repetir != 's':
                            print('\n')
                            break

                    elif op == '2':
                        print('     |  BUSCAS  |\n')
                        while True:
                            busca = input(' Digite o ID do animal que está procurando:  ')
                            print('\n')

                            for animal in rebanho:
                                if busca == animal[1]:
                                    print(f'Animal encontrado:  {animal}')
                                    break
                            
                            else:
                                print('Animal não encontrado. Digite o ID novamente.\n')
                                continue

                            repetir = input('\nDeseja buscar outro animal?  (s/n)  ').lower ()
                            print('\n')
                            
                            if repetir != 's':
                                break


                    elif op == '3':
                        print('     |  MODIFICAR DADOS DO ANIMAL  |')

                        while True:
                            busca = input('\nDigite o ID do animal que está procurando:  ')

                            for animais in rebanho:

                                if busca == animais[1]:

                                    print(f'\nAnimal encontrado: {animais}')

                                    while True:

                                        print('\n  tipo | id | status | peso | idade | valor | produto | producao | vacinado | observacoes\n')

                                        modificar = input('O que deseja modificar?  ').lower()

                                        if modificar == 'tipo':
                                            animais[0] = input('Novo tipo:  ')

                                        elif modificar == 'id':

                                            while True:
                                                novo_id = input('Novo ID:  ')

                                                for animal in rebanho:

                                                    if animal[1] == novo_id and animal != animais:
                                                        print('Esse ID já existe')
                                                        break

                                                else:
                                                    animais[1] = novo_id
                                                    break

                                        elif modificar == 'status':
                                            animais[2] = input(' Novo status:  ')

                                        elif modificar == 'peso':
                                            animais[3] = input('Novo peso: ')

                                        elif modificar == 'idade':
                                            animais[4] = input('Nova idade: ')

                                        elif modificar == 'valor':
                                            animais[6] = input('Novo valor: ')
                                    
                                        elif modificar == 'produto':
                                            animais[7] == input('O que ele produz: ')

                                        elif modificar == 'producao':
                                            animais[8] = input('Total produção diária: ')

                                        elif modificar == 'vacinado':
                                            animais[9] = input('Vacinado (sim/nao): ')

                                        elif modificar == 'observacoes':
                                            animais[10] = input('Observações: ')

                                        else:
                                            print('Essa modificação é inválida.')

                                        print('\nAnimal atualizado:', animais)

                                        continuar = input('\nDeseja alterar mais alguma coisa NESSE animal? (s/n): ').lower()
                                        print('\n')

                                        if continuar != 's':
                                            break
                                    
                                    break

                            else:
                                print('Animal não encontrado.')
                                continue  

                            break           

                    elif op == '4':
                        while True:
                            busca = input('Informe o ID do animal que deseja remover: ')

                            for animais in rebanho:

                                if busca == animais[1]:

                                    print('\n--- ANIMAL ENCONTRADO ---')
                                    print('Tipo:', animais[0])
                                    print('ID:', animais[1])
                                    print('Status:', animais[2])
                                    print('Peso:', animais[3])
                                    print('Idade:', animais[4])
                                    print('Sexo:', animais[5])
                                    print('Valor:', animais[6])
                                    print('Produto:)', animais[7])
                                    print('Produção diária:', animais[8])
                                    print('Vacinado:', animais[9])
                                    print('Observações:', animais[10])
                                    print('---------------------------')

                                    confirmacao = input('\nTem certeza que deseja remover este animal? (s/n): ').lower()

                                    if confirmacao == 's':
                                        rebanho.remove(animais)
                                        print('\nAnimal removido com sucesso!\n')

                                    else:
                                        print('\nRemoção cancelada.\n')

                                    break

                            else:
                                print('Animal não encontrado\n')
                                continue

                            break

                    elif op == '5':
                        while True:
                            print('='*10, 'GERENCIAMENTO', '='*10)
                            print('\n')
                            print('1 - Registrar produção diária')
                            print('2 - Adicionar derivado')
                            print('3 - Ver estoque')
                            print('4 - Ver produção')
                            print('5 - Sair de gerenciamento\n')

                            esc = input('Qual opção deseja realizar: ')

                            if esc == '1':

                                print('\n================= PRODUÇÃO =================')

                                data = input('Data: ')

                                producoes = []

                                for animal in rebanho:

                                    produto = animal[7]
                                    quantidade = int(animal[8])

                                    for item in producoes:

                                        if item[0] == produto:
                                            item[1] += quantidade
                                            break

                                    else:
                                        producoes.append([produto, quantidade])

                                producao_diaria.append([data, producoes])

                                print(f'\nProdução do dia {data}:\n')

                                for item in producoes:
                                    print(item[0], ':', item[1])

                                print('\nProdução diária registrada com sucesso!\n')

                            elif esc == '2':

                                print('================= DERIVADOS =================')

                                nome = input('Nome do produto: ').lower()
                                quantidade = float(input('Quantidade (kg/L): '))
                                valor_unitario = float(input('Valor por kg/L: '))

                                for produto in estoque_derivados:

                                    if produto[0] == nome:

                                        produto[1] = str(float(produto[1]) + quantidade)
                                        produto[2] = str(valor_unitario)
                                        produto[3] = str(float(produto[1]) * float(produto[2]))

                                        print('\nEstoque atualizado!\n')
                                        break

                                else:

                                    valor_total = quantidade * valor_unitario

                                    estoque_derivados.append([
                                        nome,
                                        str(quantidade),
                                        str(valor_unitario),
                                        str(valor_total)
                                    ])

                                    print('\nProduto adicionado!\n')

                            elif esc == '3':

                                print('\n================= VER ESTOQUE =================')

                                if len(estoque_derivados) == 0:
                                    print('\nEstoque vazio.\n')

                                else:
                                    for p in estoque_derivados:
                                        print('----------------')
                                        print(f'Produto: {p[0]}')
                                        print(f'Peso no estoque: {p[1]} kg')
                                        print(f'Valor do kg: R$ {p[2]}')
                                        print(f'Valor total do estoque: R$ {p[3]}')
                                        print('\n')

'''                            elif esc == '4':

                                print('\n================= VER PRODUÇÃO =================\n')

                                if len(producao_diaria) == 0:
                                    print('Nenhuma produção registrada.\n')

                                else:

                                    for registro in producao_diaria:

                                        print('----------------')
                                        print(f'Data: {registro[0]}')

                                        for item in registro[1]:
                                            print(f'{item[0]} : {item[1]}')

                                        print('\n')

                            else:
                                break

                            continuar = input('Deseja fazer outra operação? (s/n): ').lower()
                            if continuar != 's':
                                break


                    elif op == '7':
                        break'''
'''
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
        break'''