rebanho = [] # rebanho fora do while aaaaaaaaaaaaaaaaaa
# no menu adm tem 2 variaveis 'op', a primeira é para o menu principal e a 'op2' é para o menu de alteração --> mudar os números qnd passar para o projeto
while True:
    print('---Menu (ADM)---')
    print('1 - Cadastrar animal no rebanho')
    print('2 - Buscar animal')
    print('3 - Atualizar lista de animais')
    op = int(input('Digite o que deseja fazer: '))

    if op == 1: 
        animaisF = ('bovino de leite', 'caprino', 'ovino', 'suino', 'leitao')
        print(f'Animais da fazenda: {animaisF}')
        tipo = input('Informe qual o tipo do animal: ').lower()
        while tipo not in animaisF:
            print('Este tipo de animal não existe na fazenda sertão')
            print(f'Animais da fazenda: {animaisF}')
            tipo = input('Informe qual o tipo do animal: ').lower()

        identificar = ('brinco', 'numero')
        print(f'Tipos de identificação: {identificar}')
        identificacao = input('Digite como identificar o animal: ').lower()
        while identificacao not in identificar:
            print('Digite uma identificação.')
            print(f'Tipos de identificação: {identificar}')
            identificacao = input('Digite como identificar o animal: ').lower()

        numero_ID = int(input('Digite o número de identificação do animal: '))

        stats = ('lactação','engorda', 'disponivel para venda', 'vendido')
        print(f'status programados: {stats}')
        status = input('Informe o status do animal: ').lower()
        while status not in stats:
            print('Status não definido')
            print(f'status programados: {stats}')
            status = input('Informe o status do animal: ').lower()

        rebanho.append([tipo, identificacao, numero_ID, status])
        print(rebanho)

    elif op == 2:
        busca = int(input('Informe o número do animal que está procurando: '))
        achei = False
        for animais in rebanho: # para animais(sublista de rebanho) em rebanho(lista)
            if busca == animais[2]: #buscar na sublista (sublista - animais | lista - rebanho)
                achei = True
                print('Animal encontrado:', animais)
                break
            elif not achei:
                print('Animal não encontrado')

# Testar melhor
    elif op ==3:
        busca = int(input('Informe o número do animal que está procurando: '))
        achei = False
        for animais in rebanho:
            if busca == animais[2]:
                achei = True
                print('Animal encontrado:', animais)

                print()
                print('1 - tipo')
                print('2 - identificação')
                print('3 - número de identificação')
                print('4 - status do animal')
                print('5 - alterar todo o cadastro')
                op2 = int(input('Digite a opção que deseja fazer: '))
                if op2 == 1:

                    # animais = ('bovino de leite', 'caprino', 'ovino', 'suino', 'leitao')
                    print(f'Animais da fazenda: {animaisF}')
                    novo_tipo = input('Informe qual o tipo do animal: ').lower()
                    while novo_tipo not in animaisF:
                        print('Este tipo de animal não existe na fazenda sertão')
                        print(f'Animais da fazenda: {animaisF}')
                        novo_tipo = input('Informe qual o tipo do animal: ').lower()
                        #alteração na lista:
                    animais[0] = novo_tipo
                    print(f'Tipo de animal alterado: novo tipo = {novo_tipo}')
                    break

                elif op2 == 2:
                    print(f'Tipos de identificação: {identificar}')
                    nova_identificacao = input('Digite como identificar o animal: ').lower()
                    while nova_identificacao not in identificar:
                        print('Digite uma identificação.')
                        print(f'Tipos de identificação: {identificar}')
                        nova_identificacao = input('Digite como identificar o animal: ').lower()
                    animais[1] = nova_identificacao
                    print(f'Tipo de identificação alterada: nova identificação = {nova_identificacao}')

                    novo_ID = input('O número de identificação será alterado? (S/N)').upper()
                    if novo_ID == 'S':
                        novo_ID = int(input('Digite o novo número de identificação: '))
                        while novo_ID == numero_ID:
                            print('ID iguais, digite novamente: ')
                            novo_ID = int(input('Digite o novo número de identificação'))
                        animais[2] = novo_ID
                        print(f'Número de identificação alterado: novo número = {novo_ID}')
                    else:
                        break

                elif op2 == 3:
                    novo_ID = int(input('Digite o novo número de identificação: '))
                    while novo_ID == numero_ID:
                        print('ID iguais, digite novamente: ')
                        novo_ID = int(input('Digite o novo número de identificação: '))
                    animais[2] = novo_ID
                    print(f'Número de identificação alterado: novo número = {novo_ID}')
                    break

                elif op2 == 4:
                    print(f'status programados: {stats}')
                    novo_status = input('Informe o status do animal: ').lower()
                    while novo_status not in stats:
                        print('Status não definido')
                        print(f'status programados: {stats}')
                        novo_status = input('Informe o status do animal: ').lower()
                    animais[3] = novo_status
                    print(f'Status alterado: novo status = {novo_status}')
                    break

                elif op2 == 5:
                    print(f'Animais da fazenda: {animaisF}')
                    novo_tipo = input('Informe qual o tipo do animal: ').lower()
                    while novo_tipo not in animaisF:
                        print('Este tipo de animal não existe na fazenda sertão')
                        print(f'Animais da fazenda: {animaisF}')
                        novo_tipo = input('Informe qual o tipo do animal: ').lower()
                    animais[0] = novo_tipo

                    print(f'Tipos de identificação: {identificar}')
                    nova_identificacao = input('Digite como identificar o animal: ').lower()
                    while nova_identificacao not in identificar:
                        print('Digite uma identificação válida.')
                        print(f'Tipos de identificação: {identificar}')
                        nova_identificacao = input('Digite como identificar o animal: ').lower()
                    animais[1] = nova_identificacao
                    
                    novo_ID = int(input('Digite o novo número de identificação: '))
                    while novo_ID == numero_ID:
                        print('ID iguais, digite novamente: ')
                        novo_ID = int(input('Digite o novo número de identificação: '))
                    animais[2] = novo_ID

                    print(f'status programados: {stats}')
                    novo_status = input('Informe o novo status do animal: ').lower()
                    while novo_status not in stats:
                        print('Status não definido')
                        print(f'status programados: {stats}')
                        novo_status = input('Informe o novo status do animal: ').lower()
                    animais[3] = novo_status
                    print(animais)
                    break
        if not achei:
            print('Animal não encontrado')