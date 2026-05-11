rebanho = [
    ['bovino', '001', 'lactação', '500', '4', 'F', '5000', 'leite bovino', '22', 'sim', 'doente',],
    ['caprino', '100', 'lactação', '55', '3', 'F', '900', 'leite caprino', '3', 'sim', 'saudável'],
    ['ovino', '201', 'lactação', '60', '4', 'F', '1100', 'leite ovino', '2', 'não', 'doente'],
    ]


for a in rebanho:
    prioridade = 0
    if a[10] == 'doente':
        print('== Checagem rápida ==')
        print(f'IDD para checagem: {a[0:2]}')

        #TEMPERATURA
        temperatura = float(input('Informe a temperatura do animal: '))
        if temperatura < 35.5:
            prioridade +=4
            print('Hipotermia Grave!')

        elif 36.5 <= temperatura <=37.5:
            prioridade +=2
            print('Hipotermia Moderada')

        elif  37.5 < temperatura <=39.2:
            print('Animal não está com febre!')

        elif 39.2 < temperatura <=40.5:
            print('Febre Moderada.')
            prioridade +=2

        elif temperatura > 40.5:
            print('Febre Alta.')
            prioridade +=4

        #TOSSE
        tosse = input('O Animal está tossindo? (s/n): ').lower()
        if tosse == 's':
            inf_tosse = input('Informe a gravidade: (leve / moderado / grave)').lower()
            if inf_tosse == 'leve':
                prioridade +=1
            elif inf_tosse == 'moderada':
                prioridade +=2
            elif inf_tosse == 'grave':
                prioridade +=4

        #FALTA DE APETITE
        falta_apetite = input('O Animal apresenta falta de apetite? (s/n): ').lower()
        if falta_apetite == 's':
            prioridade += 2

        #FERIMENTOS
        ferimentos = input('O Animal apresenta ferimentos? (s/n): ').lower()
        if ferimentos == 's':
            prioridade +=3
            ferimentos_local = input('Informe os locais do(s) ferimentos: ')

        #ANDAR
        andar = input('O Animal apresenta dificuldades para andar? (s/n): ').lower()
        if andar == 's':
            prioridade +=3

        #DIARREIA
        diarreia = input('O Animal apresenta diarreia? (s/n): ').lower()
        if diarreia == 's':
            inf_diarreia = input('Informe o nível (leve / moderada / grave):').lower()
            if inf_diarreia == 'leve':
                prioridade += 1
            elif inf_diarreia == 'moderada':
                prioridade += 2
            elif inf_diarreia == 'grave':
                prioridade +=4

        #PRODUÇÃO DE LEITE
        if a[2] == 'lactação':
            baixa_prod = input('A produção de leite está baixa? (s/n): ').lower()
            if baixa_prod == 's':
                prioridade +=2

        #VACINAÇÃO
        if a[9] == 'sim':
            vacina_dia = input('A vacinação do animal está em dia? (s/n): ').lower()
            if vacina_dia == 'n':
                prioridade +=3
                
        #MEDICAMENTOS
        medicamento = input('O animal utiliza algum medicamento? (s/n): ').lower()
        if medicamento == 's':
            prioridade +=1
            inf_med = input('Informe o medicamento utilizado: ')

        #DIAS
        dias_doente = int(input('A quantos dias o animal está doente? '))
        if dias_doente <=3:
            prioridade +=1
        elif 4<= dias_doente <=7:
            prioridade += 2
        elif dias_doente > 7:
            prioridade +=4

        print('== Fim da Triagem ==')
        if prioridade <= 5:
            print('Prioridade Baixa. Continue monitorando o animal.')
        elif 6<= prioridade <=10:
            print('Prioridade Média. Isole, observe e trate do animal.')
        elif 11<= prioridade <= 17:
            print('Prioridade Alta! Necessita de avaliação rápidamente!')
        elif prioridade >17:
            print('PRIORIDADE CRÍTICA! Necessita de atendimento IMEDIATO!')
