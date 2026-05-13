rebanho = [
    ['bovino', '001', 'lactação', '500', '4', 'F', '5000', 'leite bovino', '22', 'sim', 'doente',],
    ['caprino', '100', 'lactação', '55', '3', 'F', '900', 'leite caprino', '3', 'sim', 'checado'],
    ['ovino', '201', 'lactação', '60', '4', 'F', '1100', 'leite ovino', '2', 'nao', 'doente'],
    ]

relatorio = [] # salvar todas as triagens

while True:
    print('=== MONITORAMENTO DO REBANHO ===') 
    print('1 - Triagem de animal doente')
    print('2 - Relatório')

    opc = input('Digite o que deseja fazer: ')
    print()

    if opc == '1':
        animal_doente = False
        for animals in rebanho:
            prioridade = 0
            if animals[10] == 'doente':
                animal_doente = True

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
                    inf_tosse = input('Informe a gravidade: (leve / moderada / grave): ').lower()
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

                #PRODUÇÃO
                if animals[2] == 'lactação' or animals[2] == 'producao':
                    baixa_prod = input('A produção está baixa? (s/n): ').lower()
                    if baixa_prod == 's':
                        prioridade +=2
                        doentes.append('Baixa produção')

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
                print()

                doentes.insert(2, prioridade)    
                relatorio.append(doentes)
                animals[10] = 'checado' #não repetir após quebrar o loop

                continuar = input('Deseja continuar fazendo checagens? (s/n): ').lower()
                if continuar != 's':
                    break 
        if not animal_doente:
            print('Não há animais doentes para a triagem.\n')


    elif opc =='2':
        while True:
            print('1 - Relatório de todos os animais doentes')
            print('2 - Buscar apenas um animal doente')
            print('3 - Animais que não estão vacinados')
            print('4 - Sair\n')
            busc = input('Digite a opção: ')
            print()

            if busc == '1':
                print('=== RELATÓRIOS DE DOENTES ===')
                if len(relatorio) == 0:
                    print('Não foi feito a checagem de nenhum animal.\n')
                else:
                    for animals in relatorio:
                        print(f'{animals}\n')

            elif busc == '2':
                buscar_a = input('Digite o IDD do animal que está procurando: ')
                print()
                encontrado = False
                if len(relatorio) == 0:
                    print('Não foi feito a checagem de nenhum animal.\n')

                for animals in relatorio:
                    if buscar_a == animals[1]: #Animal atual do loop
                        print(f'=== RELATÓRIO DO ANIMAL {buscar_a}===\n')
                        print(f'Animal encontrado:')
                        print(f'{animals}\n')
                        encontrado = True

                if not encontrado:
                    print('Animal não encontrado, tente novamente!\n')
                

            elif busc == '3':
                nao_vac = 0
                for animals in rebanho:
                    if animals[9] == 'nao':
                        nao_vac += 1
                        print(f'{animals[0:2]}: Não vacinado!')
                print(f'Total de animais não vacinados: {nao_vac}\n') #não mostra os que estão com a vacina pendente
                if nao_vac == 0:
                    print('Todos os animais estão vacinados.')
                # for animals in relatorio:
                #     if 'Vacinação não está em dia' in animals:
                #         nao_vac +=1
                #         print(f'{animals[0:2]}: Não está com a vacinação em dia!')
            elif busc == '4':
                break

