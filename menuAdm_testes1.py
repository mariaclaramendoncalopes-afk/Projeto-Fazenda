rebanho = [['bovino de leite', 'brinco', 1, 'lactação'], ['caprino', 'numero', 2, 'engorda'], ['ovino', 'numero', 3, 'vendido'], ['suino', 'brinco', 4, 'disponivel para venda'], ['leitao', 'brinco', 5, 'engorda']] # rebanho fora do while aaaaaaaaaaaaaaaaaa
# ESSE NÃO É O MENU OFICIAL




# no menu adm tem 2 variaveis 'op', a primeira é para o menu principal e a 'op2' é para o menu de alteração --> mudar os números qnd passar para o projeto
while True:
    print('---Menu (ADM)---')
    print('1 - Cadastrar animal no rebanho')
    print('2 - Buscar animal')
    print('3 - Atualizar lista de animais')
    print('4 - Retirar animal da lista')
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

                #tipo de animal
                animaisF = ('bovino de leite', 'caprino', 'ovino', 'suino', 'leitao')
                modificar = input('Você deseja modificar o tipo de animal? (S/N): ').upper()
                if modificar == 'S':
                    print(f'Animais da fazenda: {animaisF}')
                    novo_tipo = input('Informe qual o tipo do animal: ').lower()
                    while novo_tipo not in animaisF:
                        print('Este tipo de animal não existe na fazenda sertão')
                        print(f'Animais da fazenda: {animaisF}')
                        novo_tipo = input('Informe qual o tipo do animal: ').lower()
                    animais[0] = novo_tipo
                    print(f'Tipo de animal alterado: novo tipo = {novo_tipo}')
                else:
                    print(f'Tipo de animal inalterado. {animais[0]}')

                #tipo de identificação
                modificar = input('você deseja modificar o tipo de identificação do animal? (S/N): ').upper()
                if modificar == 'S':
                    identificar = ('brinco', 'numero')
                    print(f'Tipos de identificação: {identificar}')
                    nova_identificacao = input('Digite como identificar o animal: ').lower()
                    while nova_identificacao not in identificar:
                        print('Digite uma identificação programada.')
                        print(f'Tipos de identificação: {identificar}')
                        nova_identificacao = input('Digite como identificar o animal: ').lower()
                    animais[1] = nova_identificacao
                    print(f'Tipo de identificação alterada: nova identificação = {nova_identificacao}')
                else:
                    print(f'Identificação do animal inalterada. identificação = {animais[1]}')

                #numero de id
                modificar = input('O número de identificação será alterado? (S/N): ').upper()
                if modificar == 'S':
                    novo_ID = int(input('Digite o novo número de identificação: '))
                    while novo_ID == numero_ID:
                        print('ID iguais, digite novamente: ')
                        novo_ID = int(input('Digite o novo número de identificação: '))
                    animais[2] = novo_ID
                    print(f'Número de identificação alterado: novo número = {novo_ID}')
                else:
                    print(f'Número de identificação inalterado. Número = {animais[2]}')

                #status do animal
                modificar = input('Deseja alterar o status do animal? (S/N): ').upper()
                if modificar == 'S':
                    print(f'status programados: {stats}')
                    novo_status = input('Informe o status do animal: ').lower()
                    while novo_status not in stats:
                        print('Status não definido')
                        print(f'status programados: {stats}')
                        novo_status = input('Informe o status do animal: ').lower()
                    animais[3] = novo_status
                    print(f'Status alterado: novo status = {novo_status}')
                else:
                    print(f'Status inalterado. Status = {animais[3]}')
                print(animais)
        if not achei:
            print('Animal não encontrado')

## novooo -> testar melhor (não coloquei no menuADm)
    elif op == 4:
        busca = int(input('Informe o número do animal que está procurando: '))
        achei = False
        for animais in rebanho: # para animais(sublista de rebanho) em rebanho(lista)
            if busca == animais[2]: #buscar na sublista, no item de indice 2 - numero de id -  (sublista - animais | lista - rebanho)
                achei = True
                rebanho.remove(animais) #pop é usado pela posição do indice, mas sabemos apenas o número do animal(que é um valor dentro da lista), então utilizamos remove
                print(f'Animal removido da lista com sucesso! Cadastro = {animais}')
                print()
                print(rebanho)
                break