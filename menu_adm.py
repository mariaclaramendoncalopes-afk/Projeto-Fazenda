import datetime
from rich import print
from rich.console import Console
import builtins
input = lambda prompt="": builtins.input(print(prompt, end="") or "")

import fontes_cores
from time import sleep

def apenas_int(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("\n[bold red]Erro: Digite apenas números inteiros![/bold red]")

def obter_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).lower().strip()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print('\n[bold red]Resposta inválida! Digite apenas "s" para Sim ou "n" para Não.[/bold red]')


def sintoma_gravidade(gravidade):
    while True:
        entrada = apenas_int(gravidade)
        if 0< entrada <4 :
            if entrada == 1:
                inf = 'leve'
            elif entrada == 2:
                inf = 'moderada'
            else:
                inf = 'grave'
            return inf
        else:
            print('\n[bold red]Informação inválida! Digite o número que melhor descreve a gravidade do sintoma.[/bold red]\n')
        

def exibir_ficha_animal(animal):
    print(f"""
        Brinco:           [bold cyan]{animal['brinco']}[/bold cyan]
        Tipo:             [bold cyan]{animal['tipo']}[/bold cyan]
        Status:           [bold cyan]{animal['status']}[/bold cyan]
        Peso:             [bold cyan]{animal['peso']}[/bold cyan]
        Idade:            [bold cyan]{animal['idade']}[/bold cyan]
        Sexo:             [bold cyan]{animal['sexo']}[/bold cyan]
        Valor:            [bold cyan]{animal['valor']}[/bold cyan]
        Produto:          [bold cyan]{animal['produto']}[/bold cyan]
        Produção Diária:  [bold cyan]{animal['produção diária']}[/bold cyan]
        Vacinado:         [bold cyan]{animal['vacinado']}[/bold cyan]
        Observações:      [bold cyan]{animal['observações']}[/bold cyan]
""")



def cadastrar_animal(animais_d, rebanho):

        while True:
            fontes_cores.linha()
            fontes_cores.título_cadastrar_animal()
            print(f'\n\n[bold cyan]| TIPOS DISPONÍVEIS:  {animais_d}  |[/bold cyan]')
            
            tipo = input('\n  -  Informe qual o tipo de animal deseja cadastrar:  '). lower()

            if tipo not in animais_d:
                criar_tipo = apenas_int(f'''
    [bold red]{tipo}[/bold red]  |  Não existe no sistema. Deseja cadastrá-lo?

            (1)  -  Desejo cadastrá-lo.
            (2)  -  Cancelar cadastro.

  - Escolha uma opção: ''')

                if criar_tipo == 1:
                    animais_d.append(tipo)
                    print(f'\n    [bold red]{tipo}[/bold red]  |  Foi adicionado no rebanho  \n')
                else:
                    print('\nCadastro cancelado.\n')
                    break

            while True:
                brinco = input(f'\nBrinco do animal:  ')

                for animal in rebanho:
                    if animal['brinco'] == brinco:
                        print('\n| [bold red]Brinco inválido[/bold red]  |  Já existe animal cadastrado com esse brinco')
                        break

                else:
                    break

            status = input('\nStatus do animal:  ').lower ()
            peso = apenas_int('\nPeso do animal:  ')
            idade = apenas_int('\nIdade do animal:  ')
            sexo = input('\nSexo do animal:  (F/M)?  ').upper ()
            valor = apenas_int('\nValor do animal:  ')
            produto = input('\nO que ele produz?  (caso não produza nada, deixe o espaço vazio):  ').lower ()
            producao = apenas_int('\nQuanto esse animal produz por dia:  ')
            vacinado = obter_sim_nao('\nÉ vacinado - (s/n)?  ').lower ()
            observacoes = input('\nObservações: (caso não tenha, deixe o espaço vazio)  ').lower ()

            rebanho.append({
                    'brinco': brinco, 'tipo' : tipo, 'status' : status, 'peso' : peso, 'idade' : idade, 'sexo' : sexo,
                    'valor' : valor, 'produto' : produto, 'produção diária' : producao, 'vacinado' : vacinado, 'observações' : observacoes
                        })
            
            print('\nSalvando alterações...', end='', flush=True)
            sleep(1.5)
            print(' [OK]')
            sleep(0.5)
            print('\n')
            fontes_cores.linha()
            print(f'\n          [bold red]{tipo}[/bold red]  |  Cadastrado com sucesso!')

            repetir = apenas_int(f'''
- Deseja cadastrar outro animal?

            (1)  -  Desejo cadastrar outro animal.
            (2)  -  Sair da página cadastros.

- Escolha uma opção: ''')
            
            if repetir != 1:
                print('\n')
                break


def buscar_animal(rebanho):

    while True:
        fontes_cores.linha()
        fontes_cores.título_buscar_animal()
        busca = input('\n- Digite o BRINCO do animal que está buscando:  ')
        print('\n')

        for animal in rebanho:
            if busca == animal['brinco']:
                exibir_ficha_animal(animal)
                break
        
        else:
            print('Animal não encontrado. Digite o [bold red]BRINCO[/bold red] novamente.\n')
            continue

        repetir = apenas_int(f'''
- Deseja buscar outro animal?

        (1)  -  Sim.
        (2)  -  Não.

- Escolha uma opção: ''')
        print('\n')
        
        if repetir != 1:
            print('\n')
            break



def modificar_animal(rebanho):
    while True:
        fontes_cores.linha()
        fontes_cores.título_modificar_animal()
        busca = input('\nDigite o BRINCO do animal que deseja modificar:  ')

        for animal in rebanho:

            if busca == animal['brinco']:
                print('\nAnimal encontrado:\n')
                exibir_ficha_animal(animal)
                
                while True:
                    print('''                             
(1) - Brinco   (2) - Tipo   (3) - Status   (4) - Peso   (5) - Idade   (6) - Sexo   (7) - Valor   (8) - Produto   (9) - Produção diária   (10) - Vacinado   (11) - Observações\n''')
                    modificar = apenas_int('- O que deseja modificar?  ')

                    if modificar == 1:

                        while True:
                            novo_brinco = input('\nAlterar brinco:  ')

                            for brinco in rebanho:
                                if brinco['brinco'] == novo_brinco and brinco != animal:
                                    print('[bold red]Já existe um animal com esse BRINCO. Tente novamente.[/bold red]')
                                    break
                            else:
                                animal['brinco'] = novo_brinco
                                break

                    elif modificar == 2:
                        animal['tipo'] = input('\nAlterar tipo:  ').lower()

                    elif modificar == 3:
                        animal['status'] = input('\nAlterar status:  ').lower()

                    elif modificar == 4:
                        animal['peso'] = apenas_int('\nAlterar peso:  ')

                    elif modificar == 5:
                        animal['idade'] = apenas_int('\nAlterar idade:  ')

                    elif modificar == 6:
                        animal['sexo'] = input('\nAlterar sexo:  ').upper()

                    elif modificar == 7:
                        animal['valor'] = apenas_int('\nAlterar valor:  ')

                    elif modificar == 8:
                        animal['produto'] = input('\nAlterar produto:  ').lower()

                    elif modificar == 9:
                        animal['produção diária'] = apenas_int('\nAlterar produção diária')

                    elif modificar == 10:
                        animal['vacinado'] = obter_sim_nao('\nÉ vacinado -  (s/n):  ')

                    elif modificar == 11:
                        animal['observações'] = input('\nAlterar observações:  ').lower()

                    else:
                        print('\n[bold red]Essa modificação é inválida.[/bold red]')
                        continue

                    print('\nSalvando alterações...', end='', flush=True)
                    sleep(1.5)
                    print(' [OK]')
                    sleep(0.5)
                    fontes_cores.linha_comum()
                    print('       Animal atualizado:\n')
                    sleep(1)
                    exibir_ficha_animal(animal)

                    repetir = obter_sim_nao('\nDeseja alterar mais alguma coisa NESSE animal? (s/n):  ').lower()
                    print('\n')

                    if repetir != 's':
                        break
                
                break

        else:
            print('[bold red]Animal não encontrado.[bold red]\n')
            continue  

        break  
                    


def remover_animal(rebanho):
    while True:
        fontes_cores.linha()
        fontes_cores.título_remover_animal()
        remover = input('Informe o BRINCO do animal que deseja remover:  ')

        for animal in rebanho:

            if remover == animal['brinco']:
                
                print('\nCarregando informações...', end='', flush=True)
                sleep(1.5)
                print(' [OK]')
                sleep(0.5)

                exibir_ficha_animal(animal)

                confirma = obter_sim_nao('\nTem certeza que deseja remover este animal do rebanho? (s/n):  ').lower()

                if confirma == 's':
                    print('\nRemovendo animal do sistema...', end='', flush=True)
                    sleep(1.5)
                    
                    rebanho.remove(animal) 
                    
                    print('[bold red] [REMOVIDO COM SUCESSO] [/bold red]\n\n')
                    sleep(0.5)
                else:
                    print('\n\n[bold cyan]Remoção cancelada.[/bold cyan]\n')
                
                break
                
        else:
            print('\n[bold red]Animal não encontrado.[/bold red]\n')
            continue
        
        break


def monitoramento_rebanho(rebanho, relatorio):
    fontes_cores.linha()
    fontes_cores.título_monitoramento_rebanho()
    while True:
        print('''
              
            (1)  - Triagem de animal doente
            (2)  - Relatório animais
            (3)  - Sair
              
    ''')
        
        opc = apenas_int('Escolha uma opção: ')

        if opc == 1:
            dia_monitoramento = datetime.datetime.now()

            dia_monitoramento = dia_monitoramento.strftime('%d/%m/%Y')

            for animal in rebanho:
                prioridade = 0
                if animal['observações'] == 'checado':
                    seg_checagem = obter_sim_nao(f'O Animal {animal['tipo'], animal['brinco']} continua doente? (s/n): ')
                    if seg_checagem != 's':
                        animal['observações'] = ''
                    else:
                        animal['observações'] = 'doente'

                if animal['observações'] == 'doente':

                    doentes = {'brinco': animal['brinco'], 'tipo': animal['tipo'],'dia do relatório': dia_monitoramento , 'prioridade':prioridade, 'dia(s) doente': 0,
                    'sintomas':[]
                    }

                    print('  | CHECAGEM  |\n')
                    print(f'BRINCO do animal em checagem: {animal['tipo'],animal['brinco']}')
                    temp = float(input('Informe a TEMPERATURA do animal: '))
                    if temp < 35.5:
                        prioridade +=4
                        estado = 'Hipotermia Grave!'
                    elif 35.5 <= temp <= 37.5:
                        prioridade +=2
                        estado = 'Hipotermia Moderada'
                    elif 37.5 < temp <= 39.2:
                        estado = 'Temperatura Saudável!'
                    elif 39.5 < temp <= 40.5:
                        prioridade +=2
                        estado = 'Febre Moderada'
                    else:
                        prioridade +=4
                        estado = 'Febre Alta!'
                    doentes['sintomas'].append({'Temperatura': {'temperatura informada': temp, 'estado': estado}})

                    tosse = obter_sim_nao('O Animal está TOSSINDO? (s/n): ')
                    if tosse != 'n':
                        inf_tosse = sintoma_gravidade('Informe a gravidade: (1) - "Leve", (2) - "Moderada", (3) - "Grave": ')
                        if inf_tosse == 'leve':
                            prioridade +=1
                        elif inf_tosse == 'moderada':
                            prioridade +=2
                        elif inf_tosse == 'grave':
                            prioridade +=4
                        doentes['sintomas'].append({'Tosse': inf_tosse})

                    falta_apetite = obter_sim_nao('O Animal apresenta FALTA DE APETITE? (s/n): ')
                    if falta_apetite != 'n':
                        prioridade +=2
                        doentes['sintomas'].append({'Falta de apetite': 'presente'})
                    
                    ferimentos = obter_sim_nao('O Animal apresenta FERIMENTOS? (s/n): ')
                    if ferimentos != 'n':
                        prioridade +=3
                        ferimentos_local = input('Informe os locais do(s) ferimentos: ')
                        doentes['sintomas'].append({'Ferimento(s)': ferimentos_local})

                    andar = obter_sim_nao('O Animal apresenta DIFICULDADE PARA ANDAR? (s/n): ')
                    if andar != 'n':
                        prioridade +=3
                        doentes['sintomas'].append({'Dificuldades para andar': 'presente'})

                    diarreia = obter_sim_nao('O Animal está com DIARREIA? (s/n): ')
                    if diarreia != 'n':
                        inf_diarreia = sintoma_gravidade('Informe a gravidade: (1) - "Leve", (2) - "Moderada", (3) - "Grave": ')
                        if inf_diarreia == 'leve':
                            prioridade +=1
                        elif inf_diarreia == 'moderada':
                            prioridade +=2
                        elif inf_diarreia == 'grave':
                            prioridade +=4
                        doentes['sintomas'].append({'Diarreia': inf_diarreia})

                    if animal['status'] == 'lactação' or animal['status'] == 'producao':
                        baixa_prod = obter_sim_nao('A produção está BAIXA? (s/n): ')
                        if baixa_prod == 's':
                            prioridade += 2
                            doentes['sintomas'].append({'produção': 'baixa'})

                    if animal['vacinado'] == 's':
                        vacina_dia = obter_sim_nao('A VACINAÇÃO do animal está em dia? (s/n): ')
                        if vacina_dia == 'n':
                            prioridade += 2
                            doentes['sintomas'].append({'Vacinação': 'pendente'})
                    
                    medicamento = obter_sim_nao('O animal utiliza algum MEDICAMENTO? (s/n): ').lower()
                    if medicamento == 's':
                        prioridade += 1
                        inf_med = input('Informe o(s) medicamento(s) utilizado(s): ')
                        doentes['sintomas'].append({'utiliza medicamento': ['sim', inf_med]})

                    dias_doente = apenas_int('A quantos DIAS o animal está doente? ')
                    if dias_doente <= 3:
                        prioridade += 1
                    elif 4 <= dias_doente <= 7:
                        prioridade += 2
                    elif dias_doente > 7:
                        prioridade += 4

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
                    
                    doentes['prioridade'] = prioridade
                    doentes['dia(s) doente'] = dias_doente
                    relatorio.append(doentes)
                    animal['observações'] = 'checado'
                    print()

                    continuar = obter_sim_nao('Deseja continuar fazendo checagens? (s/n): ')
                    if continuar != 's':
                        break 
            else:
                print('Não há animais doentes para a triagem.\n')

        elif opc == 2:
            while True:
                print(' -______-  RELATÓRIO  -______-\n')
                print('''
                (1)  - Relatório de todos os animais doentes
                (2)  - Buscar apenas um animal doente
                (3)  - Sair
                ''')

                busc = apenas_int('Escolha uma opção: ')
                print()

                if busc == 1:
                    print('  |  RELATÓRIOS DE DOENTES  |\n')
                    if len(relatorio) == 0:
                        print('Não foi feito a checagem de nenhum animal.\n')
                    else:
                        for animal in relatorio:
                            print(f'{animal}\n')

                elif busc == 2:
                    buscar_a = input('Digite o BRINCO do animal que está procurando: ')
                    print('\n')
            
                    if len(relatorio) == 0:
                        print('Não foi feito a checagem de nenhum animal.\n')
                        continue

                    for animal in relatorio:
                        if buscar_a == animal['brinco']:
                            print(f'=== RELATÓRIO DO ANIMAL DE BRINCO "{buscar_a}" ===\n')
                            print(f'Animal encontrado:')
                            print(f'{animal}\n')
                            break

                    else:
                        print('Animal não encontrado, faça a checagem ou tente novamente!\n')

                elif busc == 3:
                    break
        elif opc == 3:
            break




def gerenciar_produçoes(rebanho, producao_diaria):
    while True:
        fontes_cores.linha()
        fontes_cores.título_gerenciar_producoes()
        print('''
            (1)  - Registrar produção diária
            (2)  - Ver relatório das produções
            (3)  - Sair
        ''')
        opcao = apenas_int('Escolha uma opção:  ')

        if opcao == 1:
            fontes_cores.linha_comum()
            fontes_cores.título_registrar_producao()
            if len(rebanho) == 0:
                print('\n[bold red]Nenhum animal cadastrado.[/bold red]')
                continue

            data = input('Data:  ')

            totais_do_dia = dict()

            for animal in rebanho:
                if len(animal['produto']) > 0:
                    produziu = apenas_int(f"Quanto o animal de brinco: {animal['brinco']}  produziu de {animal['produto']} hoje?  ")

                    animal['produção diária'] = produziu
                    produto = animal['produto']

                    totais_do_dia[produto] = totais_do_dia.get(produto, 0) + animal['produção diária']

            
            print('\nSalvando alterações...', end='', flush=True)
            sleep(1.5)
            print(' [OK]')
            print(f'\n[bold green]Registros concluídos![/bold green]')
            sleep(0.5)
            producao_diaria[data] = totais_do_dia

        elif opcao == 2:
            fontes_cores.linha_comum()
            fontes_cores.título_relatorio_producao()
            if len(producao_diaria) == 0:
                print('[bold red]Nenhuma produção registrada.[/bold red]')
            
            else:
                for data, produtos in producao_diaria.items():
                    print(f'Data: {data}\n\n{produtos}\n\n')

        elif opcao == 3:
            break

        else:
            print('[bold red]Opção inválida.[/bold red]')
            continue


def gerenciar_derivados(estoque_derivados):
    while True:
        fontes_cores.linha()
        fontes_cores.título_gerenciamento_derivados()
        print('''
            (1)  - Adicionar derivado
            (2)  - Ver estoque
            (3)  - Editar produto no estoque
            (4)  - Sair
        ''')
        opcao = apenas_int('Escolha uma opção:  ')

        if opcao == 1:
            fontes_cores.linha_comum()
            fontes_cores.título_adicionar_derivado()

            nome = input('Nome do produto:  ').lower()
            quantidade = float(input('Quantidade (kg/l) que deseja adicionar no estoque:  '))
            valor_kg = float(input('Valor por KG/L:  '))

            for produto in estoque_derivados:

                if produto['produto'] == nome:

                    produto['quantidade'] += quantidade
                    produto['valor do kg'] = valor_kg
                    produto['valor total do estoque'] = produto['quantidade'] * produto['valor do kg']

                    print('\n[bold green]Estoque atualizado![/bold green]\n')
                    break
            
            else:
                valor_total = quantidade * valor_kg

                estoque_derivados.append({'produto' : nome, 'quantidade' : quantidade, 'valor do kg' : valor_kg, 'valor total do estoque' : valor_total})

                print('\n[bold green]Produto adicionado no estoque![/bold green]')

        elif opcao == 2:
            fontes_cores.linha_comum()
            fontes_cores.título_ver_estoque()

            if len(estoque_derivados) == 0:
                print('\n[bold red]Estoque vazio.[/bold red]\n')

            else:
                for produto in estoque_derivados:
                    print('mostrar produto')

# - melhorar
def mostrar_rebanho_total(rebanho, animal):
    print('-'*5 + animal + '-'*5)
    for tipo in rebanho:
        if tipo['tipo'] == animal:
            print(f'{exibir_ficha_animal(tipo)}\n')

def quantidade_produzidos(data, producao_diaria):
    leite = 0
    for leites in producao_diaria:
        leite += float(leites[data]['leite bovino'])
        leite += float(leites[data]['leite caprino'])
        leite += float(leites[data]['leite ovino'])

        print(f'{leite}L de leite')

    for ovos in producao_diaria:
        ovo = 0
        ovo += float(ovos[data]['ovos'])
        print(f'{ovo} ovo(s)')

def derivados_no_estoque(estoque_derivados):
    derivado = 0
    estoque = 0
    for itens in estoque_derivados:
        derivado += itens['quantidade']
        estoque += itens['valor total do estoque']
        print(f'{itens['produto']} - R${estoque}')


def menu_adm(usuarios, animais_d, rebanho, relatorio, producao_diaria, estoque_derivados, data):
    while True:
        fontes_cores.título_menu_adm()
        print('''
            (1)  -  Cadastrar animal no rebanho
            (2)  -  Buscar animal
            (3)  -  Modificar dados do animal
            (4)  -  Retirar animal da lista
            (5)  -  Monitoramento do rebanho
            (6)  -  Gerenciar produção
            (7)  -  Gerenciar Derivados
            (8)  -  Relatório de vendas
            (9)  -  xxxxxxxxxxxxxxxxxx
            (0)  -  Sair
    ''')
        
        op = apenas_int('Digite qual opção deseja realizar:  ')
        print('\n')

        if op == 1:
            cadastrar_animal(animais_d, rebanho)
        
        elif op == 2:
            buscar_animal(rebanho)

        elif op == 3:
            modificar_animal(rebanho)

        elif op == 4:
            remover_animal(rebanho)

        elif op == 5:
            monitoramento_rebanho(rebanho, relatorio)

        elif op == 6:
            gerenciar_produçoes(rebanho, producao_diaria)

        elif op == 7:
            gerenciar_derivados(estoque_derivados)

        elif op == 9:
            print('Todos animais presentes no rebanho, por tipo:\n')
            for animal in animais_d:
                mostrar_rebanho_total(rebanho, animal)
            print()
            print(f'Quantidade de leite e ovos do dia {data}')
            quantidade_produzidos(data, producao_diaria)
            print()
            print(f'Estoque de Derivados')
            derivados_no_estoque(estoque_derivados)
