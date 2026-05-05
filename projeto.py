usuarios = []

# (tipo)(id:001)(status)(peso)(idade)(sexo)(valor)(produção)(vacinado)(observações)
rebanho = [
    ["bovino", "001", "lactação", "510", "4", "F", "5500", "26", "sim", "prenha"],
    ["bovino", "002", "lactação", "508", "5", "F", "5000", "25", "sim", ""],
    ["bovino", "003", "engorda", "550", "3", "M", "4200", "0", "sim", ""],
    ["bovino", "004", "venda", "460", "4", "M", "4000", "0", "nao", ""],
    ["bovino", "005", "lactação", "430", "3", "F", "3800", "18", "sim", ""],
    ["bovino", "006", "doente", "400", "5", "F", "3000", "10", "nao", "febre"],
    ["bovino", "007", "lactação", "470", "6", "F", "4200", "15", "sim", ""],

    ["caprino", "101", "lactação", "55", "3", "F", "900", "3", "sim", ""],
    ["caprino", "102", "lactação", "60", "4", "F", "1100", "4", "sim", ""],
    ["caprino", "103", "engorda", "70", "2", "M", "1200", "0", "sim", ""],
    ["caprino", "104", "venda", "50", "3", "M", "1000", "0", "nao", ""],
    ["caprino", "105", "lactação", "52", "2", "F", "1300", "2", "sim", "prenha"],
    ["caprino", "106", "doente", "45", "4", "F", "600", "1", "nao", "em tratamento"],
    ["caprino", "107", "engorda", "75", "3", "M", "1300", "0", "sim", ""],
    ["caprino", "108", "lactação", "58", "5", "F", "950", "3", "sim", ""],

    ["ovino", "201", "lactação", "65", "3", "F", "1200", "2", "sim", "prenha"],
    ["ovino", "202", "engorda", "80", "2", "M", "1400", "0", "sim", ""],
    ["ovino", "203", "venda", "70", "3", "M", "1300", "0", "nao", ""],
    ["ovino", "204", "lactação", "60", "4", "F", "1100", "2", "sim", ""],

    ["galinha", "401", "producao", "3", "1", "F", "50", "1", "sim", ""],
    ["galinha", "402", "producao", "2", "1", "F", "45", "1", "sim", ""],
    ["galinha", "403", "producao", "2", "2", "F", "55", "1", "sim", ""],
    ["galinha", "404", "producao", "3", "1", "F", "60", "1", "sim", ""],
    ["galinha", "405", "producao", "3", "2", "F", "70", "0", "sim", "chocando"],

    ["galo", "501", "engorda", "4", "2", "M", "80", "0", "sim", ""],
    ["galo", "502", "venda", "3", "1", "M", "70", "0", "sim", ""]
]

producao_leite = [
    ["01/06", "58", "5"],
    ["02/06", "62", "4"]
]

estoque_derivados = [
    ["queijo coalho", "5", "120"],
    ["queijo manteiga", "4", "150"],
    ["requeijão", "3", "90"]
]

vendas = []

while True:
    print('='*10,   'MENU  PRINCIPAL  |  FAZENDA SERTÃO',   '='*10)
    print('1 - CADASTRAR ADM')
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
                while True:
                    print('='*10,   'MENU  |  ADM',   '='*10)
                    print('\n')
                    print('1 - Cadastrar animal no rebanho')
                    print('2 - Buscar animal')
                    print('3 - Modificar dados do animais')
                    print('4 - Retirar animal da lista')
                    print('5 - Gerenciar produção e derivados')
                    print('6 - Vendas')
                    print('7 - Encerrar programa\n')

                    op = input('Digite o que deseja fazer: ')
                    print('\n')

                    if op == '1': 
                        print ('  | CADASTRAR ANIMAL NO REBANHO  |')
                        animais_D = ['bovino', 'caprino', 'ovino', 'galinha', 'galo']
                        print(f'Tipos disponíveis:  {animais_D}\n')
                        tp = input('Informe qual o tipo do animal: ').lower()

                        if tp not in animais_D:
                            confirmacao = input("Esse tipo não existe. Deseja cadastrá-lo? (s/n): ").lower()

                            if confirmacao == 's':
                                animais_D.append(tp)
                                print('Novo tipo adicionado!')
                            else:
                                print('Cadastro cancelado.\n')
                                continue

                        while True:
                            id = input(f"Digite um novo ID de identificação para ({tp}):  ")

                            repetido = False

                            for animal in rebanho:
                                if animal[1] == id:
                                    repetido = True
                                    print("Esse ID já existe, tente outro.\n")
                                    break

                            if repetido:
                                continue

                            status = input('Status do animal:  ')
                            peso = input('Peso do animal:  ')
                            idade = input('Idade do animal:  ')
                            sexo = input('Sexo (F/M):  ')
                            valor = input('Valor:  ')
                            producao = input('Produção diária:  ')
                            vacinado = input('É vacinado? (s/n):  ')
                            observacoes = input('Observação:  ')

                            rebanho.append([tp, id, status, peso, idade, sexo, valor, producao, vacinado, observacoes])

                            print('\nAnimal cadastrado com sucesso!\n')

                            confirmacao = input('Deseja cadastrar mais algum animal (s/n): ').lower()
                            if confirmacao != 's':
                                print('\n')
                                break

                        

                    elif op == '2':
                        print('  |   BUSCAS   |')
                        while True:
                            busca = input('Informe o ID do animal que está procurando: ')
                            achei = False

                            for animal in rebanho:
                                if busca == animal[1]:
                                    achei = True
                                    print('Animal encontrado:', animal)
                                    break

                            if not achei:
                                print('Animal não encontrado')

                            confirmacao = input('Deseja buscar outro animal? (s/n): ')
                            print('\n')
                            if confirmacao != 's':
                                break

                    elif op == '3':
                        print('   |   MODIFICAR DADOS DO ANIMAL  |\n')
                        busca = input('Informe o ID do animal que está procurando: ')
                        achei = False

                        for animais in rebanho:
                            if busca == animais[1]:
                                achei = True

                                while True:
                                    print('Animal encontrado:', animais)
                                    print('\ntipo | id | status | peso | idade | valor | producao | vacinado | observacoes\n')

                                    modificar = input('O que deseja modificar?\n').lower()
                                    alterou = True

                                    if modificar == 'tipo':
                                        animais[0] = input('Novo tipo: ').lower()

                                    elif modificar == 'id':
                                        while True:
                                            novo_ID = input('Novo ID: ')
                                            repetido = False

                                            for animal in rebanho:
                                                if animal[1] == novo_ID and animal != animais:
                                                    repetido = True
                                                    print('Esse ID já existe.')
                                                    break

                                            if not repetido:
                                                animais[1] = novo_ID
                                                break

                                    elif modificar == 'status':
                                        animais[2] = input('Novo status: ').lower()

                                    elif modificar == 'peso':
                                        animais[3] = input('Novo peso: ')

                                    elif modificar == 'idade':
                                        animais[4] = input('Nova idade: ')

                                    elif modificar == 'valor':
                                        animais[6] = input('Novo valor: ')

                                    elif modificar == 'producao':
                                        animais[7] = input('Nova produção: ')

                                    elif modificar == 'vacinado':
                                        animais[8] = input('Vacinado (sim/nao): ')

                                    elif modificar == 'observacoes':
                                        animais[9] = input('Observações: ')

                                    else:
                                        print('Campo inválido')
                                        alterou = False

                                    if alterou:
                                        print('\nAnimal atualizado:', animais)

                                    continuar = input('\nDeseja alterar mais alguma coisa? (s/n): ').lower()
                                    if continuar != 's':
                                        print()
                                        break

                                break

                        if not achei:
                            print('Animal não encontrado')

                    elif op == '4':
                        while True:
                            busca = input('Informe o ID do animal que deseja remover: ')
                            achei = False

                            for animais in rebanho:
                                if busca == animais[1]:
                                    achei = True

                                    print('\n--- ANIMAL ENCONTRADO ---')
                                    print('Tipo:', animais[0])
                                    print('ID:', animais[1])
                                    print('Status:', animais[2])
                                    print('Peso:', animais[3])
                                    print('Idade:', animais[4])
                                    print('Sexo:', animais[5])
                                    print('Valor:', animais[6])
                                    print('Produção:', animais[7])
                                    print('Vacinado:', animais[8])
                                    print('Observações:', animais[9])
                                    print('-------------------------')

                                    confirmacao = input('\nTem certeza que deseja remover este animal? (s/n): ').lower()

                                    if confirmacao == 's':
                                        rebanho.remove(animais)
                                        print('\nAnimal removido com sucesso!\n')
                                    else:
                                        print('\nRemoção cancelada.\n')

                                    break

                            if achei:
                                break
                            else:
                                print('Animal não encontrado\n')
                    
                    elif op == '5':
                        while True:
                            print('='*10,   'GERENCIAMENTO',   '='*10)
                            print('\n')
                            print('1 - Registrar produção diária')
                            print('2 - Adicionar derivado')
                            print('3 - Ver estoque')
                            print('4 - Ver produção')
                            print('5 - Sair de gerenciamento\n')

                            esc = input('Qual opção deseja realizar: \n')

                            if esc == '1':
                                print('================= PRODUÇÃO =================')
                                data = input('Data: ')
                                leite = 0
                                ovos = 0

                                for animal in rebanho:
                                    if animal[2] == 'lactação':
                                        leite += int(animal[7])

                                    if animal[0] == 'galinha' and animal[2] == 'producao':
                                        ovos += int(animal[7])

                                producao_leite.append([data, str(leite), str(ovos)])

                                print(f'\nProdução do dia {data}:')
                                print(f'Leite: {leite} litros')
                                print(f'Ovos: {ovos} unidades\n')

                            elif esc == '2':
                                print('================= DERIVADOS =================')
                                nome = input('Nome do produto: ').lower()
                                peso = input('Peso (kg): ')
                                valor = input('Valor: ')

                                estoque_derivados.append([nome, peso, valor])

                                print('\nProduto adicionado!\n')

                            elif esc == '3':
                                print('\n================= VER ESTOQUE =================')
                                for p in estoque_derivados:
                                    print('----------------')
                                    print(f'Produto: {p[0]}')
                                    print(f'Peso: {p[1]} kg')
                                    print(f'Valor: R${p[2]}')
                                    print('\n')

                            elif esc == '4':
                                print('\n================= VER PRODUÇÃO =================')
                                for p in producao_leite:
                                    print('----------------')
                                    print(f'Data: {p[0]}')
                                    print(f'Leite: {p[1]} litros')
                                    print(f'Ovos: {p[2]} unidades')
                                print()

                            else:
                                break

                            continuar = input('Deseja fazer outra operação? (s/n): ').lower()
                            if continuar != 's':
                                break

                    elif op == '6':
                        while True:
                            print('='*10,   'VENDAS',   '='*10)
                            print('\n')
                            print('1 - Vender animal')
                            print('2 - Vender derivado')
                            print('3 - Ver vendas')
                            print('4 - Sair de vendas\n')

                            esc = input('Digite uma opção: ')

                            if esc == '1':
                                print('\n--- ANIMAIS DISPONÍVEIS PARA VENDA ---')
                                tem = False

                                for a in rebanho:
                                    if a[2] == 'venda':
                                        print(f'ID: {a[1]} | Tipo: {a[0]} | Valor: R${a[6]}')
                                        tem = True

                                if not tem:
                                    print('Nenhum animal disponível\n')
                                    continue

                                busca = input('\nDigite o ID: ')
                                achei = False

                                for a in rebanho:
                                    if a[1] == busca and a[2] == 'venda':
                                        achei = True

                                        confirmar = input('Confirmar venda? (s/n): ').lower()
                                        if confirmar == 's':
                                            vendas.append(['animal', a[0], a[6]])
                                            rebanho.remove(a)
                                            print('\nAnimal vendido!\n')
                                        else:
                                            print('\nCancelado\n')
                                        break

                                if not achei:
                                    print('Animal inválido\n')


                            elif esc == '2':
                                print('\n--- ESTOQUE ---')
                                for p in estoque_derivados:
                                    print(f'{p[0]} | {p[1]}kg | R${p[2]}')

                                nome = input('\nProduto: ').lower()
                                achei = False

                                for p in estoque_derivados:
                                    if p[0] == nome:
                                        achei = True

                                        confirmar = input('Confirmar venda? (s/n): ').lower()
                                        if confirmar == 's':
                                            vendas.append(['derivado', p[0], p[2]])
                                            estoque_derivados.remove(p)
                                            print('\nProduto vendido!\n')
                                        else:
                                            print('\nCancelado\n')
                                        break

                                if not achei:
                                    print('Produto não encontrado\n')
                                    continue

                            elif esc == '3':
                                print('\n--- VENDAS ---')
                                total = 0

                                for v in vendas:
                                    print(f'{v[0]} | {v[1]} | R${v[2]}')
                                    total += int(v[2])

                                print(f'\nTotal: R${total}\n')

                            else:
                                break

                    elif op == '7':
                        break



            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == False:
                print('Login CLIENTE')
                break
            else:
                print('Usuário não encontrado\n')
                continue
    
    if op == '4':
        print('\nEncerrando sistema...')
        print('Salvando dados...')
        print('Finalizando conexões...')
        print('\nSistema encerrado com sucesso. Até logo!')
        break