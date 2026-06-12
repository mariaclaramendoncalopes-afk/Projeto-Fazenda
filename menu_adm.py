import datetime
import matplotlib.pyplot as plt
from rich import print
from rich.console import Console
import fontes_cores
from time import sleep
from rich.table import Table
from rich.panel import Panel
from fpdf import FPDF
import historico


def apenas_int(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("\n[bold red]Erro: Digite apenas números inteiros![/bold red]\n")

def apenas_float(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print('\n[bold red]Erro! Digite um número válido (ex: 1.5 ou 2).[/bold red]\n')

def obter_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).lower().strip()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print('\n[bold red]Resposta inválida! Digite apenas "s" para Sim ou "n" para Não.[/bold red]')

def apenas_letras(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada and entrada.replace(" ", "").isalpha():
            return entrada.lower()
        print('\n[bold red]Erro! Digite apenas letras.[/bold red]\n')


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

def exibir_produtos(produto):
    print(f"""
        Produto:  {produto['produto']}
        Quantidade disponível: {produto['quantidade']}
        Valor do Kg:  R$ {produto['valor do kg']:.2f}
        Valor total do estoque:  R$ {produto['valor total do estoque']:.2f}

""")
    

def exibir_producao_diaria(producao_diaria):
    for data, produtos in producao_diaria.items():
        print(f'Data: {data}\n\n{produtos}\n\n')


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

            status = apenas_letras('\nStatus do animal?  (lactação|venda|produção|etc):  ').lower ()
            peso = apenas_float('\nPeso do animal?  ')
            idade = apenas_int('\nIdade do animal?  ')
            sexo = apenas_letras('\nSexo do animal:  (F/M)?  ').upper ()
            valor = apenas_float('\nValor do animal?  ')
            produto = input('\nO que ele produz?  (caso não produza nada, deixe o espaço vazio):  ').lower ()
            producao = apenas_int('\nQuanto esse animal produz por dia?  (caso não produza nada, digite 0):  ')
            vacinado = obter_sim_nao('\nÉ vacinado?  (s/n)?  ').lower ()
            observacoes = input('\nObservações? (caso não tenha, deixe o espaço vazio)  ').lower ()

            rebanho.append({
                    'brinco': brinco, 'tipo' : tipo, 'status' : status, 'peso' : peso, 'idade' : idade, 'sexo' : sexo,
                    'valor' : valor, 'produto' : produto, 'produção diária' : producao, 'vacinado' : vacinado, 'observações' : observacoes
                        })
            
            print('\n\nSalvando alterações...', end='', flush=True)
            sleep(1.5)
            print(' [bold green][OK][/bold green]')
            sleep(1)
            print('\n')
            print(f'\n          [bold green]{tipo}[/bold green]  |  Cadastrado com sucesso!\n')

            repetir = apenas_int(f'''
- Deseja cadastrar outro animal?

            (1)  -  Desejo cadastrar outro animal.
            (2)  -  Sair da página cadastros.

- Escolha uma opção: ''')
            
            if repetir != 1:
                print('\n')
                fontes_cores.linha()
                break


def todos_animais(rebanho):
    fontes_cores.linha()
    fontes_cores.título_animais_rebanho()

    for animal in rebanho:
        exibir_ficha_animal(animal)

    input('\n\nPressione a tecla ENTER para sair')
    fontes_cores.linha()


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
            fontes_cores.linha()
            break



def modificar_animal(rebanho):
    while True:
        fontes_cores.linha()
        fontes_cores.título_modificar_animal()
        busca = input('\n- Digite o BRINCO do animal que deseja modificar:  ')

        for animal in rebanho:

            if busca == animal['brinco']:
                print('\nAnimal encontrado:\n')
                exibir_ficha_animal(animal)
                
                while True:
                    print('''                             
(1) Brinco   (2) Tipo   (3) Status   (4) Peso   (5) Idade   (6) Sexo   (7) Valor   (8) Produto   (9) Produção diária   (10) Vacinado   (11) Observações\n''')
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
                        animal['peso'] = apenas_float('\nAlterar peso:  ')

                    elif modificar == 5:
                        animal['idade'] = apenas_int('\nAlterar idade:  ')

                    elif modificar == 6:
                        animal['sexo'] = input('\nAlterar sexo:  ').upper()

                    elif modificar == 7:
                        animal['valor'] = apenas_float('\nAlterar valor:  ')

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
                    print(' [bold green][OK][/bold green]\n')
                    sleep(1)
                    print('       - Animal atualizado:\n')
                    sleep(1)
                    exibir_ficha_animal(animal)

                    repetir = obter_sim_nao('\n- Deseja alterar mais alguma coisa NESSE animal? (s/n):  ').lower()
                    print('\n')

                    if repetir != 's':
                        fontes_cores.linha()
                        break
                
                break

        else:
            print('\n[bold red]Animal não encontrado.[bold red]\n')
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
                print(' [bold green][OK][/bold green]')
                sleep(1)

                exibir_ficha_animal(animal)

                confirma = obter_sim_nao('\nTem certeza que deseja remover este animal do rebanho? (s/n):  ').lower()

                if confirma == 's':
                    print('\nRemovendo animal do sistema...', end='', flush=True)
                    sleep(1.5)
                    
                    rebanho.remove(animal) 
                    
                    print('[bold green] [REMOVIDO COM SUCESSO] [/bold green]\n\n')
                    sleep(0.5)
                else:
                    print('\n\n[bold cyan]Remoção cancelada.[/bold cyan]\n')
                
                fontes_cores.linha()
                break
                
        else:
            print('\n[bold red]Animal não encontrado.[/bold red]\n')
            continue
        
        break


def monitoramento_rebanho(rebanho, relatorio):
    console = Console()

    while True:
        fontes_cores.linha()
        fontes_cores.título_monitoramento_rebanho()
        print('''
            (1)  - Triagem de animal doente
            (2)  - Relatório animais (Terminal)
            (3)  - Buscar animal doente pelo brinco
            (4)  - Exportar Relatório para PDF
            (5)  - Animais não vacinados
            (6)  - Sair
    ''')
        
        opc = apenas_int('\n- Escolha uma opção: ')
        print('\n')
        fontes_cores.linha_comum()

        if opc == 1:
            dia_monitoramento = datetime.datetime.now().strftime('%d/%m/%Y')

            for animal in rebanho:
                prioridade = 0
                if animal['observações'] == 'checado':
                    seg_checagem = obter_sim_nao(f"\nO Animal {animal['tipo'], animal['brinco']} continua doente? (s/n): ")
                    if seg_checagem != 's':
                        animal['observações'] = ''
                    else:
                        animal['observações'] = 'doente'

                if animal['observações'] == 'doente':
                    doentes = {
                        'brinco': animal['brinco'], 
                        'tipo': animal['tipo'],
                        'dia do relatório': dia_monitoramento, 
                        'prioridade': prioridade, 
                        'dia(s) doente': 0,
                        'sintomas': []
                    }

                    fontes_cores.título_checagem()
                    print(f'     [bold cyan]BRINCO do animal em checagem: {animal["brinco"]}  |  {animal["tipo"]}[/bold cyan]')
                    temp = apenas_float('\nInforme a TEMPERATURA do animal: ')
                    if temp < 35.5:
                        prioridade += 4
                        estado = 'Hipotermia Grave!'
                    elif temp <= 37.5:
                        prioridade += 2
                        estado = 'Hipotermia Moderada'
                    elif temp <= 39.2:
                        estado = 'Temperatura Saudável!'
                    elif temp <= 40.5:
                        prioridade += 2
                        estado = 'Febre Moderada'
                    else:
                        prioridade += 4
                        estado = 'Febre Alta!'

                    doentes['sintomas'].append({'Temperatura': {'temperatura informada': temp, 'estado': estado}})

                    tosse = obter_sim_nao('\nO Animal está TOSSINDO? (s/n): ')
                    if tosse != 'n':
                        inf_tosse = sintoma_gravidade('\nInforme a gravidade   (1) Leve   (2) Moderada   (3) Grave   :')
                        if inf_tosse == 'leve':
                            prioridade += 1
                        elif inf_tosse == 'moderada':
                            prioridade += 2
                        elif inf_tosse == 'grave':
                            prioridade += 4
                        doentes['sintomas'].append({'Tosse': inf_tosse})

                    falta_apetite = obter_sim_nao('\nO Animal apresenta FALTA DE APETITE? (s/n): ')
                    if falta_apetite != 'n':
                        prioridade += 2
                        doentes['sintomas'].append({'Falta de apetite': 'presente'})
                    
                    ferimentos = obter_sim_nao('\nO Animal apresenta FERIMENTOS? (s/n): ')
                    if ferimentos != 'n':
                        prioridade += 3
                        ferimentos_local = input('\nInforme os locais do(s) ferimentos: ')
                        doentes['sintomas'].append({'Ferimento(s)': ferimentos_local})

                    andar = obter_sim_nao('\nO Animal apresenta DIFICULDADE PARA ANDAR? (s/n): ')
                    if andar != 'n':
                        prioridade += 3
                        doentes['sintomas'].append({'Dificuldades para andar': 'presente'})

                    diarreia = obter_sim_nao('\nO Animal está com DIARREIA? (s/n): ')
                    if diarreia != 'n':
                        inf_diarreia = sintoma_gravidade('\nInforme a gravidade   (1) Leve   (2) Moderada   (3) Grave   :')
                        if inf_diarreia == 'leve':
                            prioridade += 1
                        elif inf_diarreia == 'moderada':
                            prioridade += 2
                        elif inf_diarreia == 'grave':
                            prioridade += 4
                        doentes['sintomas'].append({'Diarreia': inf_diarreia})

                    if animal['status'] == 'lactação' or animal['status'] == 'producao':
                        baixa_prod = obter_sim_nao('\nA produção está BAIXA? (s/n): ')
                        if baixa_prod == 's':
                            prioridade += 2
                            doentes['sintomas'].append({'Produção': 'baixa'})

                    if animal['vacinado'] == 's':
                        vacina_dia = obter_sim_nao('\nA VACINAÇÃO do animal está em dia? (s/n): ')
                        if vacina_dia == 'n':
                            prioridade += 2
                            doentes['sintomas'].append({'Vacinação': 'pendente'})
                    
                    medicamento = obter_sim_nao('\nO animal utiliza algum MEDICAMENTO? (s/n): ').lower()
                    if medicamento == 's':
                        prioridade += 1
                        inf_med = input('\nInforme o(s) medicamento(s) utilizado(s): ')
                        doentes['sintomas'].append({'utiliza medicamento': ['sim', inf_med]})

                    dias_doente = apenas_int('\nA quantos DIAS o animal está doente? ')
                    if dias_doente <= 3:
                        prioridade += 1
                    elif dias_doente <= 7:
                        prioridade += 2
                    elif dias_doente > 7:
                        prioridade += 4

                    print('\nSalvando alterações...', end='', flush=True)
                    sleep(1.5)
                    print(' [bold green][OK][/bold green]\n')
                    sleep(1)
                    print(f'\n[bold green]Fim da checagem.[/bold green]\n')
                    print(f'Prioridade do animal: {prioridade}')

                    if prioridade <= 5:
                        print('[bold green]Prioridade Baixa. Continue monitorando o animal.[/bold green]')
                    elif 6 <= prioridade <= 10:
                        print('[bold yellow]Prioridade Média. Isole, observe e trate do animal.[/bold yellow]')
                    elif 11 <= prioridade <= 17:
                        print('[bold orange3]Prioridade Alta! Necessita de avaliação rapidamente![/bold orange3]')
                    else:
                        print('[bold red]PRIORIDADE CRÍTICA! Necessita de atendimento IMEDIATO![/bold red]')
                    print('\n')
                    
                    doentes['prioridade'] = prioridade
                    doentes['dia(s) doente'] = dias_doente

                    for animal_registro in relatorio:
                        if animal_registro['brinco'] == doentes['brinco']:
                            print('Animal já registrado. Excluindo relatório antigo...')
                            sleep(3)
                            relatorio.remove(animal_registro)
                            print('Novo relatório registrado!')
                            break

                    relatorio.append(doentes)
                    animal['observações'] = 'checado'
                    print('\n')

            else:
                print('\n[bold red]Não há mais animais doentes para a triagem.[/bold red]\n')

        elif opc == 2:
            fontes_cores.título_relatorio()
            print('\n')

            if len(relatorio) == 0:
                console.print('[bold yellow]Não foi feita a checagem de nenhum animal.[/bold yellow]\n')
            else:
                tabela = Table(title="ANIMAIS DOENTES REGISTRADOS", title_style="bold cyan", border_style="blue")
                tabela.add_column("Brinco", justify="center", style="bold white")
                tabela.add_column("Tipo", justify="center")
                tabela.add_column("Data Relatório", justify="center")
                tabela.add_column("Dias Doente", justify="center")
                tabela.add_column("Prioridade", justify="center")

                for animal in relatorio:
                    prio = animal['prioridade']
                    if prio <= 5:
                        cor_prio = f"[bold green]{prio}[/bold green]"
                    elif prio <= 10:
                        cor_prio = f"[bold yellow]{prio}[/bold yellow]"
                    elif prio <= 17:
                        cor_prio = f"[bold orange]{prio}[/bold orange]"
                    else:
                        cor_prio = f"[bold red]{prio}[/bold red]"

                    tabela.add_row(
                        str(animal['brinco']),
                        animal['tipo'].capitalize(),
                        animal['dia do relatório'],
                        str(animal['dia(s) doente']),
                        cor_prio
                    )
                
                console.print(tabela)
                print('\n')
                input('Pressione a tecla ENTER para sair')
                print('\n')

        elif opc == 3:
            while True:
                fontes_cores.título_buscar_animal()
                
                if len(relatorio) == 0:
                    console.print('[bold yellow]Não foi feita a checagem de nenhum animal ainda.[/bold yellow]\n')
                    break

                busca = input('- Digite o BRINCO do animal que está procurando (ou "sair" para voltar): ')
                print('\n')
                
                if busca.lower() == 'sair':
                    break

                for animal in relatorio:
                    if str(busca) == str(animal['brinco']):
                        prio = animal['prioridade']
                        if prio <= 5:
                            cor, txt = "green", "Baixa"
                        elif prio <= 10:
                            cor, txt = "yellow", "Média"
                        elif prio <= 17:
                            cor, txt = "orange3", "Alta"
                        else:
                            cor, txt = "red", "Crítica"

                        sintomas_formatados = ""
                        for s in animal['sintomas']:
                            for chave, valor in s.items():
                                sintomas_formatados += f"• [bold]{chave}:[/bold] {valor}\n"

                        conteudo_painel = f"[bold]Tipo:[/bold] {animal['tipo'].capitalize()}\n"
                        conteudo_painel += f"[bold]Data do Registro:[/bold] {animal['dia do relatório']}\n"
                        conteudo_painel += f"[bold]Dias Doente:[/bold] {animal['dia(s) doente']}\n"
                        conteudo_painel += f"[bold]Prioridade:[/bold] [{cor}]{prio} ({txt})[/{cor}]\n\n"
                        conteudo_painel += f"[cyan][bold]Sintomas Detectados:[/bold][/cyan]\n{sintomas_formatados}"

                        painel = Panel(conteudo_painel, title=f"RELATÓRIO DO ANIMAL {busca}", border_style=cor, expand=False)
                        console.print(painel)
                        print('\n')
                        sleep(2)
                        break

                else:
                    console.print('[bold red]Animal não encontrado, faça a checagem ou tente novamente![/bold red]\n\n')
                    fontes_cores.linha_comum()
                    continue
                
                opc = obter_sim_nao('Deseja buscar outro animal pelo brinco? (s/n): ')
                print('\n')
                if opc != 's':
                    break

        elif opc == 4:
            fontes_cores.título_relatorio_pdf()

            if len(relatorio) == 0:
                console.print('[bold yellow]Não há dados de triagem para gerar o documento PDF.[/bold yellow]\n')
                input('\nPressione a tecla ENTER para sair')
            else:
                print('Gerando relatório detalhado em PDF...', end='', flush=True)
                
                pdf = FPDF()
                pdf.add_page()
                
                pdf.set_font("Helvetica", "B", 16)
                pdf.cell(0, 10, "SISTEMA DE MONITORAMENTO DE REBANHO", ln=True, align="C")
                pdf.set_font("Helvetica", "I", 10)
                pdf.cell(0, 8, f"Documento gerado em: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True, align="C")
                pdf.ln(10)
                
                for animal in relatorio:
                    pdf.set_font("Helvetica", "B", 12)
                    pdf.set_fill_color(230, 240, 255)  
                    pdf.cell(0, 8, f"ANIMAL BRINCO: {animal['brinco']}", ln=True, border=1, fill=True)
                    
                    pdf.set_font("Helvetica", "", 11)
                    pdf.cell(95, 8, f"  Tipo: {animal['tipo'].capitalize()}", border="LR")
                    pdf.cell(95, 8, f"Data da Triagem: {animal['dia do relatório']}", border="R", ln=True)
                    
                    prio = animal['prioridade']
                    txt_prio = f"{prio} (Baixa)" if prio <= 5 else f"{prio} (Média)" if prio <= 10 else f"{prio} (Alta)" if prio <= 17 else f"{prio} (Crítica)"
                    
                    pdf.cell(95, 8, f"  Dias Observados: {animal['dia(s) doente']}", border="LRB")
                    pdf.cell(95, 8, f"Nível de Prioridade: {txt_prio}", border="RB", ln=True)

                    pdf.set_font("Helvetica", "B", 11)
                    pdf.cell(0, 8, f"  Sintomas e Observações Clínicas:", border="LR", ln=True)
                    
                    pdf.set_font("Helvetica", "", 10)
                    sintomas_texto = ""
                    
                    for s in animal['sintomas']:
                        for chave, valor in s.items():
                            if chave == 'Temperatura':
                                temp_inf = valor.get('temperatura informada', 'N/A')
                                est_inf = valor.get('estado', 'N/A')
                                sintomas_texto += f"  * Temperatura: {temp_inf}°C ({est_inf})\n"
                            elif chave == 'utiliza medicamento':
                                sintomas_texto += f"  * Medicamento: {valor[1]}\n"
                            else:
                                sintomas_texto += f"  * {chave}: {valor}\n"
                    
                    if not sintomas_texto:
                        sintomas_texto = "  Nenhum sintoma grave registrado nesta triagem.\n"
                    
                    pdf.multi_cell(0, 6, sintomas_texto, border="LRB")
                    pdf.ln(8)

                pdf.output("relatorio_rebanho.pdf")
                sleep(1)
                console.print(' [bold green][CONCLUÍDO][/bold green]')
                console.print('[bold green]Arquivo "relatorio_rebanho.pdf" atualizado com sucesso![/bold green]\n')
                sleep(1.5)
                print('\n')
                input('Pressione a tecla ENTER para sair')
                print('\n')

        elif opc == 5:
            fontes_cores.título_animais_não_vacinados()

            qnt = 0
            for animal in rebanho:
                if animal['vacinado'] == 'n':
                    qnt +=1
                    print(f'Brinco: {animal['brinco']}')
                    print(f'{animal['tipo']} - NÃO vacinado \n')
            for animal in relatorio:
                for sintoma in animal['sintomas']: 
                    if 'Vacinação' in sintoma and sintoma['Vacinação'] == 'pendente':
                        qnt +=1
                        print(f'Brinco: {animal['brinco']}')
                        print(f'{animal['tipo']} - Vacinação PENDENTE \n')
            print(f'Quantidade de animais que precisam de vacina: {qnt}')
            input('\n\nPressione a tecla ENTER para sair')
        
        elif opc == 6:
            break
        else:
            console.print('[bold red]Opção inválida! Selecione um número válido do menu.[/bold red]\n')



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

            data = datetime.datetime.now().strftime('%d/%m/%Y')

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
            input('\nPressione ENTER para sair.')

        elif opcao == 2:
            fontes_cores.linha_comum()
            fontes_cores.título_relatorio_producao()
            if len(producao_diaria) == 0:
                print('[bold red]Nenhuma produção registrada.[/bold red]')
                input('\nPressione ENTER para sair.')
            
            else:
                exibir_producao_diaria(producao_diaria)
                input('\nPressione ENTER para sair.')

        elif opcao == 3:
            print('\n')
            fontes_cores.linha()
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
            (0)  - Sair
        ''')
        opcao = apenas_int('Escolha uma opção:  ')

        if opcao == 0:
            print('\n')
            fontes_cores.linha()
            break

        elif opcao == 1:
            fontes_cores.linha_comum()
            fontes_cores.título_adicionar_derivado()

            nome = apenas_letras('Nome do produto:  ').lower()
            quantidade = apenas_float('Quantidade (kg/l) que deseja adicionar no estoque:  ')
            valor_kg = apenas_float('Valor por KG/L:  ')

            for produto in estoque_derivados:

                if produto['produto'] == nome:

                    produto['quantidade'] += quantidade
                    produto['valor do kg'] = valor_kg
                    produto['valor total do estoque'] = produto['quantidade'] * produto['valor do kg']

                    registrar_historico_mov(historico.historico_mov, data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), acao= 'Produção', item = produto['produto'], quantidade = produto['quantidade'])
                    print('\n[bold green]Estoque atualizado![/bold green]\n')
                    break
            
            else:
                valor_total = quantidade * valor_kg

                estoque_derivados.append({'produto' : nome, 'quantidade' : quantidade, 'valor do kg' : valor_kg, 'valor total do estoque' : valor_total})

                registrar_historico_mov(historico.historico_mov, data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), acao= 'Produção', item = nome, quantidade = produto['quantidade'])
                print('\n[bold green]Produto adicionado no estoque![/bold green]')

        elif opcao == 2:
            fontes_cores.linha_comum()
            fontes_cores.título_ver_estoque()

            if len(estoque_derivados) == 0:
                print('\n[bold red]Estoque vazio.[/bold red]\n')

            else:
                for produto in estoque_derivados:
                    exibir_produtos(produto)
            
            input('Pressione ENTER para sair.')
            print('\n\n')
        
        elif opcao == 3:
            fontes_cores.linha_comum()
            fontes_cores.título_editar_produto()

            nome_produto = input('Digite o nome do produto que deseja editar:  ').lower()

            for produto in estoque_derivados:
                
                if produto['produto'] == nome_produto:
                    while True:
                        print(f'''
(1) Nome do produto    (2) Quantidade    (3) Valor do KG    (4) Cancelar edição''')
                        editar = apenas_int('\n- O que deseja editar?  ')

                        if editar == 1:
                            novo_nome = input('\nNovo nome:  ').lower()
                            produto['produto'] = novo_nome
                            print('\n[bold green]Nome atualizado![/bold green]\n')
                            sleep(1)
                            exibir_produtos(produto)
                            sleep(4)

                        elif editar == 2:
                            nova_quantidade = apenas_float('\nNova quantidade:  ')
                            produto['quantidade'] = nova_quantidade
                            produto['valor total do estoque'] = produto['quantidade'] * produto['valor do kg']
                            print('\n[bold green]Quantidade atualizada![/bold green]\n')  
                            sleep(1)  
                            exibir_produtos(produto)

                            registrar_historico_mov(historico.historico_mov, data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), acao= 'Produção', item = produto['produto'], quantidade = produto['quantidade'])
                            
                            sleep(4)

                        elif editar == 3:
                            novo_valor = apenas_float('\nNovo valor:  ')
                            produto['valor do kg'] = novo_valor
                            produto['valor total do estoque'] = produto['quantidade'] * produto['valor do kg']
                            print('\n[bold green]Valor do KG atualizado![/bold green]\n')
                            sleep(1)
                            exibir_produtos(produto)
                            sleep(4)

                        else:
                            break
                    break
            
            else:
                print('\n[bold red]Produto não encontrado.[/bold red]\n')


def relatorio_vendas(historico_pedidos):
    fontes_cores.linha()
    fontes_cores.título_relatorio_vendas()
    if not historico_pedidos:
        print("\n[bold red]Nenhum pedido encontrado.[/bold red]\n")
        input('Pressione a tecla ENTER para retornar ao menu.')
        fontes_cores.linha()
        return

    total_vendas = 0
    total_pedidos = len(historico_pedidos)

    vendas_por_dia = {}
    vendas_por_cliente = {}


    for pedido in historico_pedidos:

        valor_total = pedido["valor"] + pedido["frete"]
        total_vendas += valor_total

        data = pedido["data_entrega"]
        vendas_por_dia[data] = vendas_por_dia.get(data, 0) + valor_total

        cliente = pedido["nome completo"]
        vendas_por_cliente[cliente] = vendas_por_cliente.get(cliente, 0) + valor_total

        print("\n----------------------------")
        print(f"Cliente: {pedido['nome completo']}")
        print(f"Email: {pedido['email']}")
        print(f"Telefone: {pedido['telefone']}")
        print(f"Endereço: {pedido['rua']}, {pedido['numero']}")
        print(f"Cidade: {pedido['cidade']} - {pedido['estado']}")
        print(f"Data entrega: {pedido['data_entrega']}")
        print(f"Valor produtos: R$ {pedido['valor']:.2f}")
        print(f"Frete: R$ {pedido['frete']:.2f}")
        print(f"TOTAL: R$ {valor_total:.2f}")
        print("-------------------------------")


    print("\nRESUMO GERAL")
    print(f"Total de pedidos: {total_pedidos}")
    print(f"Faturamento total: R$ {total_vendas:.2f}")


    print("\nTOP CLIENTES")

    top_clientes = sorted(vendas_por_cliente.items(), key=lambda x: x[1], reverse=True)

    for cliente, valor in top_clientes:
        print(f"{cliente}: R$ {valor:.2f}")


    datas = list(vendas_por_dia.keys())
    valores = list(vendas_por_dia.values())

    plt.figure(figsize=(10,5))
    plt.plot(datas, valores, marker='o')
    plt.title("Faturamento por Data de Entrega")
    plt.xlabel("Data")
    plt.ylabel("R$")
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.show()



def painel_de_controle(rebanho, animais_d, producao_diaria, estoque_derivados, relatorio, historico):
    while True:
        fontes_cores.linha()
        fontes_cores.título_painelcontrolePC()
        print('''
            (1) - Visualizar Rebanho Total (por Tipo)
            (2) - Verificar Produção Diária
            (3) - Consultar Estoque de Derivados
            (4) - Ver Resumo de Animais Doentes
            (5) - Histórico de Modificações no Estoque
            (6) - Histórico de Derivados Vendidos
            (7) - Voltar ao Menu Principal
        ''')
        
        opc = apenas_int('\n- Escolha uma opção do Painel: ')
        print('\n')
        
        if opc == 1:
            print('[bold green]Todos animais presentes no rebanho, por tipo:[/bold green]\n')
            for tipo in animais_d:
                fontes_cores.título_tipos_animaisPC(tipo)
                
                houve_animal = False
                for animal in rebanho:
                    if animal['tipo'].lower() == tipo.lower():
                        exibir_ficha_animal(animal)
                        houve_animal = True
                        
                if not houve_animal:
                    print(f"Nenhum animal do tipo {tipo} encontrado no rebanho.\n")

            input('\nPressione ENTER para continuar...')

        elif opc == 2:
            fontes_cores.linha_comum()
            fontes_cores.título_producao_diariaPC()
            if len(producao_diaria) == 0:
                print('[bold red]Nenhuma produção registrada.[/bold red]')
            else:
                exibir_producao_diaria(producao_diaria)

            input('\nPressione ENTER para continuar...')

        elif opc == 3:
            fontes_cores.linha_comum()
            fontes_cores.título_estoque_derivadosPC()
            derivados_no_estoque(estoque_derivados)

            input('\nPressione ENTER para continuar...')

        elif opc == 4:
            fontes_cores.linha_comum()
            fontes_cores.título_animais_doentePC()
            mostrar_animais_doentes(rebanho, relatorio)

            input('\nPressione ENTER para continuar...')

        elif opc == 5:
            fontes_cores.linha_comum()
            fontes_cores.título_historico_estoquePC()

            for h in historico.historico_mov:
                if h['Ação'] == 'Produção':
                    print(f"Data: {h['Data']} | Item: {h['Item']} | Qtd: {h['Quantidade']}")

            else:
                print('[bold red]Nenhuma modificação de estoque registrada.[bold red]')

            input('\nPressione ENTER para continuar...')

        elif opc == 7:
            print('Saindo do Painel de Controle...')
            sleep(1)
            fontes_cores.linha()
            break
        else:
            print('[bold red]Opção inválida do Painel de Controle![/bold red]')


def derivados_no_estoque(estoque_derivados):
    derivado = 0
    estoque = 0
    qnt_derivados = 0
    for itens in estoque_derivados:
        qnt_derivados += 1
        derivado += itens['quantidade']
        estoque += itens['valor total do estoque']
        exibir_produtos(itens)
    print(f'''
    [bold purple]Resumo:[/bold purple]
    Quantidade de Derivados: {qnt_derivados}
    Total de Derivados: {derivado} 
    Estoque Total: R$ {estoque:.2f}
    ''')


def mostrar_animais_doentes(rebanho, relatorio):
    qnt = 0
    for animal in rebanho:
        if animal['observações'] == 'doente':
            qnt += 1
            print(f'Brinco: {animal["brinco"]}')
            print(f'{animal["tipo"]} - DOENTE \n')
        elif animal['observações'] == 'checado':
            qnt += 1            
            print(f'Brinco: {animal["brinco"]}')
            print(f'{animal["tipo"]} - DOENTE (Checado)\n')
            
    print(f'Número de animais que estão [bold red]DOENTES[/bold red]: {qnt}')
    print('Para maior informação sobre os sintomas, procure: Relatório animais, no Monitoramento do rebanho.\n')


def registrar_historico_mov(historico, data, acao, item, quantidade):
    historico.historico_mov.append({
        'Data': data,
        'Ação': acao,
        'Item': item,
        'Quantidade': quantidade
    })






def menu_adm(login, animais_d, rebanho, relatorio, producao_diaria, estoque_derivados, data, historico_pedidos):
    while True:
        fontes_cores.título_menu_adm()
        print('''
            (1)  -  Cadastrar animal no rebanho
            (2)  -  Listar todos os animais do rebanho
            (3)  -  Buscar animal pelo brinco
            (4)  -  Modificar dados do animal
            (5)  -  Retirar animal da lista
            (6)  -  Monitoramento do rebanho
            (7)  -  Gerenciar Produção
            (8)  -  Gerenciar Derivados
            (9)  -  Relatório de vendas
            (10) -  Painel de Controle
            (0)  -  Sair
    ''')
        
        op = apenas_int('Digite qual opção deseja realizar:  ')
        print('\n')

        if op == 0:
            break

        elif op == 1:
            cadastrar_animal(animais_d, rebanho)

        elif op == 2:
            todos_animais(rebanho)
        
        elif op == 3:
            buscar_animal(rebanho)

        elif op == 4:
            modificar_animal(rebanho)

        elif op == 5:
            remover_animal(rebanho)

        elif op == 6:
            monitoramento_rebanho(rebanho, relatorio)

        elif op == 7:
            gerenciar_produçoes(rebanho, producao_diaria)

        elif op == 8:
            gerenciar_derivados(estoque_derivados)

        elif op == 9:
            relatorio_vendas(historico_pedidos)

        elif op == 10:
            painel_de_controle(rebanho, animais_d, producao_diaria, estoque_derivados, relatorio, historico)
