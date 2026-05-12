rebanho = [
    ['bovino', '001', 'lactação', '500', '4', 'F', '5000', 'leite bovino', '22', 'sim', 'doente',],
    ['caprino', '100', 'lactação', '55', '3', 'F', '900', 'leite caprino', '3', 'sim', 'saudável'],
    ['ovino', '201', 'lactação', '60', '4', 'F', '1100', 'leite ovino', '2', 'não', 'doente'],
    ]

relatorio = [] # salvar todas as triagens

while True: 
    print('1 - Triagem de animal doente')
    print('2 - Relatório')

    opc = input('Digite o que deseja fazer: ')
    print()

    if opc == '1':
        for animals in rebanho:
            prioridade = 0
            if animals[10] == 'doente':
                doentes = []
                print('=== CHECAGEM ===')
                print(f'IDD para checagem: {animals[0:2]}')
                doentes.append(animals[0])
                doentes.append(animals[1])

                #TEMPERATURA
                temperatura = float(input('Informe a temperatura do animal: '))
                if temperatura < 35.5:
                    prioridade +=4
                    print('Hipotermia Grave!')

                elif 35.5 <= temperatura <=37.5:
                    prioridade +=2
                    print('Hipotermia Moderada')

                elif  37.5 < temperatura <=39.2:
                    print('Animal não está com febre!')

                elif 39.2 < temperatura <=40.5:
                    print('Febre Moderada.')
                    prioridade +=2

                elif temperatura > 40.5:
                    print('Febre Alta!')
                    prioridade +=4
                doentes.append(f'Temperatura: {temperatura}')

                #TOSSE
                tosse = input('O Animal está tossindo? (s/n): ').lower()
                if tosse == 's':
                    inf_tosse = input('Informe a gravidade: (leve / moderado / grave): ').lower()
                    if inf_tosse == 'leve':
                        prioridade +=1
                    elif inf_tosse == 'moderada':
                        prioridade +=2
                    elif inf_tosse == 'grave':
                        prioridade +=4
                    doentes.append(f'Tosse: {inf_tosse}')

                #FALTA DE APETITE
                falta_apetite = input('O Animal apresenta falta de apetite? (s/n): ').lower()
                if falta_apetite == 's':
                    prioridade += 2
                    doentes.append('Falta de apetite')

                #FERIMENTOS
                ferimentos = input('O Animal apresenta ferimentos? (s/n): ').lower()
                if ferimentos == 's':
                    prioridade +=3
                    ferimentos_local = input('Informe os locais do(s) ferimentos: ')
                    doentes.append(f'Ferimento(s) no(s) local(is): {ferimentos_local}')

                #ANDAR
                andar = input('O Animal apresenta dificuldades para andar? (s/n): ').lower()
                if andar == 's':
                    prioridade +=3
                    doentes.append('Dificuldades para andar')

                #DIARREIA
                diarreia = input('O Animal apresenta diarreia? (s/n): ').lower()
                if diarreia == 's':
                    inf_diarreia = input('Informe o nível (leve / moderada / grave): ').lower()
                    if inf_diarreia == 'leve':
                        prioridade += 1
                    elif inf_diarreia == 'moderada':
                        prioridade += 2
                    elif inf_diarreia == 'grave':
                        prioridade +=4
                    doentes.append(f'Diarreia: {inf_diarreia}')

                #PRODUÇÃO DE LEITE
                if animals[2] == 'lactação':
                    baixa_prod = input('A produção de leite está baixa? (s/n): ').lower()
                    if baixa_prod == 's':
                        prioridade +=2
                        doentes.append('Baixa produção de leite')

                #VACINAÇÃO
                if animals[9] == 'sim':
                    vacina_dia = input('A vacinação do animal está em dia? (s/n): ').lower()
                    if vacina_dia == 'n':
                        prioridade +=2
                        doentes.append('Vacinação não está em dia')
                        
                #MEDICAMENTOS
                medicamento = input('O animal utiliza algum medicamento? (s/n): ').lower()
                if medicamento == 's':
                    prioridade +=1
                    inf_med = input('Informe o(s) medicamento(s) utilizado(s): ')
                    doentes.append(f'Medicamento(s) utilizado(s): {inf_med}')

                #DIAS
                dias_doente = int(input('A quantos dias o animal está doente? '))
                if dias_doente <=3:
                    prioridade +=1
                elif 4<= dias_doente <=7:
                    prioridade += 2
                elif dias_doente > 7:
                    prioridade +=4
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

                doentes.insert(2, prioridade)    
                relatorio.append(doentes)
                animals[10] = 'checado' #não repetir após quebrar o loop

                continuar = input('Deseja continuar fazendo checagens? (s/n): ').lower()
                if continuar == 'n':
                    break #quebra e volta o loop do inicio, se o usuário quiser continuar dps ele tem que fazer do zero


    elif opc =='2':
        busc = input('Deseja ver todos os relatórios ou apenas buscar um animal? ( R - relatório / A - animal ): ').upper()
        if busc == 'R':
            print('=== RELATÓRIOS ===')
            for animals in relatorio:
                print(f'{animals}\n')

        elif busc == 'A':
            buscar_a = input('Digite o IDD do animal que está procurando: ')
            print()
            encontrado = False

            for animals in relatorio:
                if buscar_a == animals[1]: #Animal atual do loop
                    print(f'=== RELATÓRIO DO ANIMAL {buscar_a}===\n')
                    print(f'Animal encontrado:')
                    print(f'{animals}\n')
                    encontrado = True

            if encontrado != True:
                print('Animal não encontrado, tente novamente!\n')
