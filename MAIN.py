usuarios = [
    ['kamille', '1234', True],
    ['clara', '5678', True],
    ['teste', '0000', False],
]

# tipo,  IDD,  status,  peso,  idade,  sexo,  valor,  produto, produção diária,  vacinado,  observações
rebanho = [
    ['bovino', '001', 'lactação', '500', '4', 'F', '5000', 'leite bovino', '22', 'sim', ''],
    ['bovino', '002', 'venda', '460', '5', 'F', '4500', 'leite bovino', '19', 'sim', ''],
    ['bovino', '003', 'venda', '490', '5', 'F', '4700', 'leite bovino', '20', 'sim', ''],

    ['caprino', '100', 'lactação', '55', '3', 'F', '900', 'leite caprino', '3', 'sim', 'doente'],
    ['caprino', '101', 'venda', '60', '4', 'F', '1000', 'leite caprino', '4', 'sim', ''],

    ['ovino', '201', 'lactação', '60', '4', 'F', '1100', 'leite ovino', '2', 'sim', ''],

    ['galinha', '401', 'producao', '3', '1', 'F', '50', 'ovos', '1', 'sim', 'doente'],
    ['galinha', '402', 'producao', '2', '1', 'F', '45', 'ovos', '1', 'sim', ''],
]

animais_d = ['bovino', 'caprino', 'ovino', 'galinha']

relatorio = []

producao_diaria = []

estoque_derivados = [
    ["queijo coalho", "5", "24", "120"],
    ["queijo manteiga", "4", "37.5", "150"],
    ["requeijão", "3", "30", "90"]
]

relatorio_vendas = []

carrinho = []

while True:
    print('-______- FAZENDA SERTÃO -______-')
    print('\n')
    print('1 - |  Cadastrar administrador  |')
    print('2 - |  Cadastrar usuário        |')
    print('3 - |  Login                    |')
    print('4 - |  Sair                     |')
    print('\n')
    op = input('Digite a opção que deseja realizar:  ')
    
    if op == '1':
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

    if op == '2':
        print('     |  CADASTRO CLIENTE  |\n')

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

    if op == '3':
        print('\n     |  lOGIN  |     \n')
        usuario = input(' Usuário:  ').lower ()
        senha = input(' Senha:  ')

        for pessoa in usuarios:
            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == True:
                while True:
                    print('\n-______-  MENU ADM   |   FAZENDA SERTÃO -______-\n')
                    print(' '*18,   f'Bem vindo(a), {usuario}\n')
                    print(' 1  -  |  Cadastrar animal no rebanho  |')
                    print(' 2  -  |  Buscar animal                |')
                    print(' 3  -  |  Modificar dados do animal    |')
                    print(' 4  -  |  Retirar animal da lista      |')
                    print(' 5  -  |  Monitoramento do rebanho     |')
                    print(' 6  -  |  Gerenciar produção           |')
                    print(' 7  -  |  Gerenciar derivados          |')
                    print(' 8  -  |  Relatório de vendas          |')
                    print(' 9  -  |  Sair                         |')

                    op = input('\n Digite uma opção:  ')
                    print('\n')

                    if op == '1':
                        print('\n     |  CADASTRAR ANIMAL NO REBANHO  |\n')
                        while True:
                            print(f'| Tipos disponíveis:  {animais_d} |')
                            tipo = input('Informe qual o tipo de animal:  ').lower ()

                            if tipo not in animais_d:
                                criar_tipo = input('Esse tipo não existe. Deseja cadastrá-lo  (s/n)?  ').lower ()

                                if criar_tipo == 's':
                                    animais_d.append(tipo)
                                    print('\nNovo tipo adicionado!\n')
                                else:
                                    print('\nCadastro cancelado.\n')
                                    break
                            
                            while True:
                                idd = input(f'Digite um novo IDD para ({tipo}):  ')

                                for animal in rebanho:
                                    if animal[1] == idd:
                                        print('\nEsse IDD já existe, tente outro.\n')
                                        break

                                else:
                                    break

                            status = input('Status do animal:  ').lower ()
                            peso = input('Peso do animal:  ')
                            idade = input('Idade do animal:  ')
                            sexo = input('Sexo do animal:  (F/M)?  ').upper ()
                            valor = input('Valor do animal:  ')
                            produto = input('O que ele produz:  ').lower ()
                            producao = input('Quanto esse animal produz por dia? (digite apenas a quantidade em números):  ')
                            vacinado = input('É vacinado?  (sim/nao)?  ').lower ()
                            observacoes = input('Observações: (caso não tenha, deixe o espaço vazio)  ').lower ()

                            rebanho.append([tipo, idd, status, peso, idade, sexo, valor, produto, producao, vacinado, observacoes])

                            print(f'\nAnimal | {tipo} | cadastrado com sucesso!!\n')

                            repetir = input('Deseja cadastrar outro animal?  (s/n)  ').lower ()
                            print('\n')

                            if repetir != 's':
                                print('\n')
                                break

                    elif op == '2':
                        print('     |  BUSCAS  |\n')
                        while True:
                            busca = input(' Digite o IDD do animal que está procurando:  ')
                            print('\n')

                            for animal in rebanho:
                                if busca == animal[1]:
                                    print(f'Animal encontrado:  {animal}')
                                    break
                            
                            else:
                                print('Animal não encontrado. Digite o IDD novamente.\n')
                                continue

                            repetir = input('\nDeseja buscar outro animal?  (s/n)  ').lower ()
                            print('\n')
                            
                            if repetir != 's':
                                break


                    elif op == '3':
                        print('     |  MODIFICAR DADOS DO ANIMAL  |')

                        while True:
                            busca = input('\nDigite o IDD do animal que está procurando:  ')

                            for animais in rebanho:

                                if busca == animais[1]:

                                    print(f'\nAnimal encontrado: {animais}')

                                    while True:

                                        print('\n  tipo | idd | status | peso | idade | sexo | valor | produto | producao | vacinado | observacoes\n')

                                        modificar = input('O que deseja modificar?  ').lower()

                                        if modificar == 'tipo':
                                            animais[0] = input('Novo tipo:  ').lower()

                                        elif modificar == 'idd':

                                            while True:
                                                novo_id = input('Novo IDD:  ')

                                                for animal in rebanho:

                                                    if animal[1] == novo_id and animal != animais:
                                                        print('Esse IDD já existe')
                                                        break

                                                else:
                                                    animais[1] = novo_id
                                                    break

                                        elif modificar == 'status':
                                            animais[2] = input(' Novo status:  ').lower()

                                        elif modificar == 'peso':
                                            animais[3] = input('Novo peso: ')

                                        elif modificar == 'idade':
                                            animais[4] = input('Nova idade: ')

                                        elif modificar == 'sexo':
                                            animais[5] = input('Alterar sexo:  ').upper ()

                                        elif modificar == 'valor':
                                            animais[6] = input('Novo valor: ')
                                    
                                        elif modificar == 'produto':
                                            animais[7] = input('O que ele produz: ').lower()

                                        elif modificar == 'producao':
                                            animais[8] = input('Total produção diária: ')

                                        elif modificar == 'vacinado':
                                            animais[9] = input('Vacinado (sim/nao): ').lower()

                                        elif modificar == 'observacoes':
                                            animais[10] = input('Observações: ').lower()

                                        else:
                                            print('\nEssa modificação é inválida.')
                                            continue

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
                            busca = input('Informe o IDD do animal que deseja remover: ')

                            for animais in rebanho:

                                if busca == animais[1]:

                                    print('\n      | ANIMAL ENCONTRADO  |')
                                    print('Tipo:', animais[0])
                                    print('IDD:', animais[1])
                                    print('Status:', animais[2])
                                    print('Peso:', animais[3])
                                    print('Idade:', animais[4])
                                    print('Sexo:', animais[5])
                                    print('Valor:', animais[6])
                                    print('Produto:', animais[7])
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
                            print('\n -______-  MONITORAMENTO DO REBANHO  -______-\n') 
                            print(' 1 -  |  Triagem de animal doente  |')
                            print(' 2 -  |  Relatório                 |')
                            print(' 3 -  |  Sair                      |')
                            print('\n')
                    
                            opc = input('Digite o que deseja fazer: ')
                            print('\n')

                            if opc == '1':
                                dia_monitoramento = input('Data: ')

                                for animal in rebanho:
                                    prioridade = 0
                                    if animal[10] == 'doente':

                                        doentes = []
                                        print('  | CHECAGEM  |\n')
                                        print(f'IDD para checagem: {animal[0:2]}')
                                        doentes.append(animal[0])
                                        doentes.append(animal[1])

                                        temperatura = float(input('Informe a temperatura do animal: '))
                                        if temperatura < 35.5:
                                            prioridade += 4
                                            print('Hipotermia Grave!')

                                        elif 35.5 <= temperatura <=37.5:
                                            prioridade += 2
                                            print('Hipotermia Moderada')

                                        elif  37.5 < temperatura <=39.2:
                                            print('Animal não está com febre!')

                                        elif 39.2 < temperatura <=40.5:
                                            print('Febre Moderada.')
                                            prioridade += 2

                                        elif temperatura > 40.5:
                                            print('Febre Alta!')
                                            prioridade +=4
                                        doentes.append(f'Temperatura: {temperatura}')

                                        tosse = input('O Animal está tossindo? (s/n): ').lower()
                                        if tosse == 's':
                                            inf_tosse = input('Informe a gravidade: (leve / moderada / grave): ').lower()
                                            if inf_tosse == 'leve':
                                                prioridade += 1
                                            elif inf_tosse == 'moderada':
                                                prioridade += 2
                                            elif inf_tosse == 'grave':
                                                prioridade += 4
                                            doentes.append(f'Tosse: {inf_tosse}')

                                        falta_apetite = input('O Animal apresenta falta de apetite? (s/n): ').lower()
                                        if falta_apetite == 's':
                                            prioridade += 2
                                            doentes.append('Falta de apetite')

                                        ferimentos = input('O Animal apresenta ferimentos? (s/n): ').lower()
                                        if ferimentos == 's':
                                            prioridade += 3
                                            ferimentos_local = input('Informe os locais do(s) ferimentos: ')
                                            doentes.append(f'Ferimento(s) no(s) local(is): {ferimentos_local}')

                                        andar = input('O Animal apresenta dificuldades para andar? (s/n): ').lower()
                                        if andar == 's':
                                            prioridade += 3
                                            doentes.append('Dificuldades para andar')

                                        diarreia = input('O Animal apresenta diarreia? (s/n): ').lower()
                                        if diarreia == 's':
                                            inf_diarreia = input('Informe o nível (leve / moderada / grave): ').lower()
                                            if inf_diarreia == 'leve':
                                                prioridade += 1
                                            elif inf_diarreia == 'moderada':
                                                prioridade += 2
                                            elif inf_diarreia == 'grave':
                                                prioridade += 4
                                            doentes.append(f'Diarreia: {inf_diarreia}')

                                        if animal[2] == 'lactação' or animal[2] == 'producao':
                                            baixa_prod = input('A produção está baixa? (s/n): ').lower()
                                            if baixa_prod == 's':
                                                prioridade += 2
                                                doentes.append('Baixa produção')

                                        if animal[9] == 'sim':
                                            vacina_dia = input('A vacinação do animal está em dia? (s/n): ').lower()
                                            if vacina_dia == 'n':
                                                prioridade += 2
                                                doentes.append('Vacinação não está em dia')
                                                
                                        medicamento = input('O animal utiliza algum medicamento? (s/n): ').lower()
                                        if medicamento == 's':
                                            prioridade += 1
                                            inf_med = input('Informe o(s) medicamento(s) utilizado(s): ')
                                            doentes.append(f'Medicamento(s) utilizado(s): {inf_med}')

                                        dias_doente = int(input('A quantos dias o animal está doente? '))
                                        if dias_doente <= 3:
                                            prioridade += 1
                                        elif 4 <= dias_doente <= 7:
                                            prioridade += 2
                                        elif dias_doente > 7:
                                            prioridade += 4
                                        doentes.append(f'{dias_doente} dia(s) doente')

                                        print(f'Fim da checagem.\n')

                                        print(f'Prioridade do animal: {prioridade}')
                                        if prioridade <= 5:
                                            print('Prioridade Baixa. Continue monitorando o animal.')
                                        elif 6<= prioridade <=10:
                                            print('Prioridade Média. Isole, observe e trate do animal.')
                                        elif 11<= prioridade <= 17:
                                            print('Prioridade Alta! Necessita de avaliação rápidamente!')
                                        elif prioridade >17:
                                            print('PRIORIDADE CRÍTICA! Necessita de atendimento IMEDIATO!')
                                        print('\n')

                                        doentes.insert(2, f'Prioridade:{prioridade}')
                                        doentes.append(f'Data do relatório: {dia_monitoramento}')    
                                        relatorio.append(doentes)
                                        animal[10] = 'checado'

                                        continuar = input('Deseja continuar fazendo checagens? (s/n): ').lower()
                                        if continuar != 's':
                                            break 
                                else:
                                    print('Não há animais doentes para a triagem.\n')


                            elif opc =='2':
                                while True:
                                    print(' -______-  RELATÓRIO  -______-\n')
                                    print(' 1 -  |  Relatório de todos os animais doentes  |')
                                    print(' 2 -  |  Buscar apenas um animal doente         |')                                    
                                    print(' 3 -  |  Sair                                   |')
                                    print('\n')
                                    busc = input('Digite a opção: ')
                                    print()

                                    if busc == '1':
                                        print('  |  RELATÓRIOS DE DOENTES  |\n')
                                        if len(relatorio) == 0:
                                            print('Não foi feito a checagem de nenhum animal.\n')
                                        else:
                                            for animal in relatorio:
                                                print(f'{animal}\n')

                                    elif busc == '2':
                                        buscar_a = input('Digite o IDD do animal que está procurando: ')
                                        print('\n')
                                
                                        if len(relatorio) == 0:
                                            print('Não foi feito a checagem de nenhum animal.\n')
                                            continue

                                        for animal in relatorio:
                                            if buscar_a == animal[1]:
                                                print(f'=== RELATÓRIO DO ANIMAL {buscar_a}===\n')
                                                print(f'Animal encontrado:')
                                                print(f'{animal}\n')

                                        else:
                                            print('Animal não encontrado, faça a checagem ou tente novamente!\n')

                                    elif busc == '3':
                                        break

                            elif opc =='3':
                                break 

                    elif op == '6':
                        while True:
                            print('\n -______-  GERENCIAR  PRODUÇÕES  -______-\n')
                            print(' 1 -  |  Registrar produção diária    |')
                            print(' 2 -  |  Ver relatório das produções  |')
                            print(' 3 -  |  Sair                         |')
                            print('\n')

                            esc = input('Qual opção deseja realizar: ')

                            if esc == '1':

                                print('\n  |  REGISTRAR   PRODUÇÃO  |  \n')
                                
                                if len(rebanho) == 0:
                                    print('Nenhum animal cadastrado.\n')
                                    continue

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
                                input('ENTER para continuar')


                            elif esc == '2':

                                print('\n===== RELATÓRIO DE PRODUÇÃO =====\n')

                                if len(producao_diaria) == 0:
                                    print('Nenhuma produção registrada ainda.\n')

                                else:
                                    for registro in producao_diaria:

                                        data = registro[0]
                                        producoes = registro[1]

                                        print(f'DATA: {data}')
                                        print('--------------------------')

                                        for item in producoes:
                                            print(f'{item[0]}: {item[1]}')

                                        print('\n')

                                input('ENTER para continuar')

                            else:
                                break

                    elif op == '7':
                        while True:
                            print('='*10, 'GERENCIAMENTO  DERIVADOS', '='*10)
                            print('\n')
                            print('1 - Adicionar derivado')
                            print('2 - Ver estoque')
                            print('3 - Editar produto')
                            print('4 - Sair\n')

                            esc = input('Qual opção deseja realizar: ')

                            if esc == '1':

                                print('===== ADICIONAR  DERIVADOS =====')

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

                                    estoque_derivados.append([nome, str(quantidade), str(valor_unitario), str(valor_total)])

                                    print('\nProduto adicionado!\n')
                                input("Pressione ENTER para voltar ao menu...")
                                print('\n'*2)

                            elif esc == '2':

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

                                input("Pressione ENTER para voltar ao menu...")
                                print('\n'*2)

                            elif esc == '3':

                                print('\n===== EDITAR PRODUTO =====\n')

                                nome_editar = input('Digite o nome do produto: ').lower()

                                for produto in estoque_derivados:

                                    if produto[0] == nome_editar:

                                        while True:

                                            print('\nO que deseja editar?\n')
                                            print('1 - Nome')
                                            print('2 - Quantidade')
                                            print('3 - Valor por kg/L')
                                            print('4 - Sair\n')

                                            editar = input('Escolha: ')

                                            if editar == '1':

                                                novo_nome = input('Novo nome: ').lower()
                                                produto[0] = novo_nome

                                                print('\nNome atualizado!\n')

                                            elif editar == '2':

                                                nova_quantidade = float(input('Nova quantidade: '))
                                                produto[1] = str(nova_quantidade)

                                                produto[3] = str(
                                                    float(produto[1]) * float(produto[2])
                                                )

                                                print('\nQuantidade atualizada!\n')

                                            elif editar == '3':

                                                novo_valor = float(input('Novo valor por kg/L: '))
                                                produto[2] = str(novo_valor)

                                                produto[3] = str(float(produto[1]) * float(produto[2]))

                                                print('\nValor atualizado!\n')

                                            else:
                                                break

                                        break

                                else:
                                    print('\nProduto não encontrado!\n')

                                input("Pressione ENTER para voltar ao menu...")
                                print('\n')

                            else:
                                break


                    elif op == '8':

                        print('\n===== RELATÓRIO DE VENDAS =====\n')

                        if len(relatorio_vendas) == 0:

                            print('Nenhuma venda realizada.\n')

                        else:

                            for venda in relatorio_vendas:

                                print('CLIENTE:', venda[0])

                                print('\nITENS:')

                                for item in venda[1]:

                                    print(f'{item[0]} | Qtd: {item[1]} | R$ {item[2]}')

                                print('\nTOTAL:', venda[2])

                                print('PAGAMENTO:', venda[3])

                                print('\n---------------------------\n')

                        input('ENTER para continuar...')
                
                    elif op == '9':
                        break
                break

            if usuario == pessoa[0] and senha == pessoa[1] and pessoa[2] == False:

                carrinho = []

                while True:
                    print('\n -______-  MENU | CLIENTE  -______-\n')
                    print('1 - |  Ver catálogo                                      |')
                    print('2 - |  Adicionar ao carrinho                             |')
                    print('3 - |  Carrinho / Agendar transporte / Confirmar compra  |')
                    print('4 - |  Sair                                              |')
                    print('\n')

                    op = input('Digite o que deseja fazer: ')
                    print()

                    if op == '1':

                        print('=== DERIVADOS DISPONÍVEIS ===')
                        for p in estoque_derivados:
                            print(f'{p[0]} | {p[1]} kg | R$ {p[2]} por kg')

                        print('\n=== ANIMAIS DISPONÍVEIS ===')
                        for a in rebanho:
                            if a[2] == 'venda':
                                print(f'IDD: {a[1]} | Tipo: {a[0]} | Valor: R$ {a[6]}')

                        input("\nENTER para voltar...")

                    elif op == '2':

                        while True:

                            tipo = input('Comprar (D - derivado / A - animal / S - sair): ').upper()

                            if tipo == 'S':
                                break

                            elif tipo == 'D':

                                nome = input('Nome do produto: ').lower()
                                qtd = float(input('Quantidade (kg/L): '))

                                if qtd <= 0:
                                    print('Quantidade inválida!\n')
                                    continue

                                for p in estoque_derivados:

                                    if p[0] == nome:

                                        if qtd <= float(p[1]):

                                            total = qtd * float(p[2])
                                            carrinho.append([nome, qtd, total])

                                            print(f'\nAdicionado ao carrinho: {nome} - R$ {total}')

                                        else:
                                            print('Quantidade indisponível')

                                        break

                                else:
                                    print('Produto não encontrado')

                                input("\nENTER para continuar...")

                            elif tipo == 'A':

                                id_animal = input('IDD do animal: ')

                                for a in rebanho:

                                    if a[1] == id_animal and a[2] == 'venda':

                                        carrinho.append([a[0] + ' IDD ' + a[1], 1, float(a[6])])

                                        print('Animal adicionado ao carrinho!')
                                        break

                                else:
                                    print('Animal não encontrado')

                                input("\nENTER para continuar...")

                            else:
                                print('Opção inválida!')
                                continue

                    elif op == '3':

                        print('\n===== SEU CARRINHO =====\n')

                        if len(carrinho) == 0:
                            print('Carrinho vazio\n')
                            input("ENTER para continuar...")
                            continue

                        total_geral = 0

                        for item in carrinho:
                            print(f'{item[0]} | Quantidade: {item[1]} | R$ {item[2]}')
                            total_geral += float(item[2])

                        print('\nTOTAL: R$', total_geral)

                        while True:

                            print('\n1 - Confirmar compra')
                            print('2 - Remover item')
                            print('3 - Voltar')

                            escolha = input('\nOpção: ')

                            if escolha == '1':

                                print('\n=== FINALIZANDO COMPRA ===')
                                print('Total dos produtos:', total_geral)

                                print('\n===== ENTREGA =====\n')

                                endereco = input('Endereço: ')
                                dias = int(input('Prazo (dias): '))

                                if dias <= 2:
                                    frete = 20

                                elif dias <= 5:
                                    frete = 10

                                else:
                                    frete = 0

                                total_final = total_geral + frete

                                print('\nResumo da entrega:')
                                print('Endereço:', endereco)
                                print('Prazo:', dias, 'dias')
                                print('Frete: R$', frete)

                                print('\nTOTAL FINAL: R$', total_final)

                                while True:
                                    print('\nForma de pagamento:')
                                    print('1 - PIX')
                                    print('2 - Cartão')

                                    opcao = input('Escolha a opção: ')

                                    if opcao == '1':
                                        pagamento = 'PIX'
                                        break

                                    elif opcao == '2':
                                        pagamento = 'Cartão'
                                        break

                                    else:
                                        print('Opção inválida! Digite 1 ou 2.')

                                print('\nCompra realizada com sucesso!')
                                print('Pagamento:', pagamento)
                                print('Pedido em processamento...\n')

                                relatorio_vendas.append([usuario, carrinho.copy(), total_final, pagamento, endereco, dias])

                                for item in carrinho:

                                    nome_item = item[0]
                                    quantidade = item[1]

                                    for p in estoque_derivados:

                                        if p[0] == nome_item:

                                            p[1] = str(float(p[1]) - float(quantidade))
                                            break

                                    for a in rebanho:

                                        nome_animal = a[0] + ' IDD ' + a[1]

                                        if nome_item == nome_animal:

                                            rebanho.remove(a)
                                            break

                                carrinho = []

                                input('ENTER para continuar...')
                                break

                            elif escolha == '2':

                                rem = input('Nome ou IDD do item: ').lower()

                                for item in carrinho:

                                    if rem in item[0].lower():

                                        carrinho.remove(item)

                                        total_geral = 0

                                        for itens in carrinho:
                                            total_geral += float(itens[2])

                                        print('Item removido!')
                                        print(f'Novo total: R$ {total_geral}')

                                        break
                                else:
                                    print('Item não encontrado')

                            elif escolha == '3':
                                break

                            else:
                                print('Opção inválida!')
                                continue

                    elif op == '4':
                        print('Saindo...\n')
                        break

                    else:
                        print('Opção inválida!')
                        input("ENTER para continuar...")
                break
        else:
            print('\n Usuário não encontrado \n')



    if op == '4':
        print('\n Encerrando o sistema... \n')
        print(' Salvando dados...')
        print(' Finalizando conexões... ')
        print('\n Sistema encerrado com sucesso. Até logo! ')
        break