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
        print('[bold red] Resposta inválida! Digite apenas "s" para Sim ou "n" para Não.[/bold red]\n')


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
            print(f'\n          [bold red]{tipo}[/bold red]  |  Cadastrado com sucesso!')

            repetir = apenas_int(f'''
- Deseja cadastrar outro animal?

            (1)  -  Desejo cadastrar outro animal.
            (2)  -  Sair da página cadastros.

Escolha uma opção: ''')
            
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


# def monitoramento_rebanho(rebanho):
#     fontes_cores.linha()
#     fontes_cores.título_monitoramento_rebanho()
#     while True:
#         print('''
              
#             (1)  - Triagem de animal doente
#             (2)  - Relatório animais
#             (3)  - Sair
              
#     ''')



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





                



def menu_adm(usuarios, animais_d, rebanho, producao_diaria, estoque_derivados):
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
            print('monitoramento animais')

        elif op == 6:
            gerenciar_produçoes(rebanho, producao_diaria)

        elif op == 7:
            gerenciar_derivados(estoque_derivados)