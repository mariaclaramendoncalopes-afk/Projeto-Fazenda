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


producao_diaria = []

estoque_derivados = [
    ["queijo coalho", "5", "24", "120"],
    ["queijo manteiga", "4", "37.5", "150"],
    ["requeijão", "3", "30", "90"]
]

carrinho = []


while True:
    print('='*10, '     MENU ADM     |     FAZENDA SERTÃO     ', '='*10)
    print('\n')
    print(' '*18,   f'Bem vindo(a)\n')
    print(' 1  -  Cadastrar animal no rebanho')
    print(' 2  -  Buscar animal')
    print(' 3  -  Modificar dados do animal')
    print(' 4  -  Retirar animal da lista')
    print(' 5  -  Gerenciar produção')
    print(' 6  -  Gerenciar derivados')
    print(' 7  -  Relatório')
    print(' 8  -  Sair\n')

    op = input('Digite uma opção:  ')

    if op == '1':
        print('\n           |  CADASTRAR ANIMAL NO RABANHO  |\n')
        animais_d = ['bovino', 'caprino', 'ovino', 'galinha']
        while True:
            print(f'| Tipos disponíveis:  {animais_d} |')
            tipo = input('Informe qual o tipo de animal você deseja cadastrar:  ').lower ()

            if tipo not in animais_d:
                criar_tipo = input('Esse tipo não existe. Deseja cadastrá-lo  (s/n)?  ').lower ()

                if criar_tipo == 's':
                    animais_d.append(tipo)
                    print('\nNovo tipo adicionado!\n')
                else:
                    print('Cadastro cancelado.\n')
                    break
            
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