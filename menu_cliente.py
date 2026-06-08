import fontes_cores
import menu_adm
from rich import print
from pick import pick

def apenas_int(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("\n[bold red]Erro: Digite apenas números inteiros![/bold red]")

def apenas_float(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print('[bold red]Erro! Digite um número válido (ex: 1.5 ou 2).[/bold red]')

def obter_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).lower().strip()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print('\n[bold red]Resposta inválida! Digite apenas "s" para Sim ou "n" para Não.[/bold red]')



def catálogo_venda_derivados(estoque_derivados):
    fontes_cores.linha()
    fontes_cores.título_derivados_disponiveis()
    for produto in estoque_derivados:
        menu_adm.exibir_produtos(produto)
    
def catálogo_venda_animal(rebanho):
    fontes_cores.linha()
    fontes_cores.título_animais_disponiveis()
    for animal in rebanho:
        if animal['status'] == 'venda':
            menu_adm.exibir_ficha_animal(animal)

    
def adicionar_carrinho(estoque_derivados, rebanho, carrinho):
    while True:
        fontes_cores.linha()
        fontes_cores.título_adicionar_carrinho()
        print('''
            (1) Adicionar derivado no carrinho
            (2) Adicionar animal no carrinho
            (0) Sair
              ''')
        
        opc = apenas_int('Escolha uma opção:  ')
        print('\n')

        if opc == 0:
            fontes_cores.linha()
            break

        elif opc == 1:
            catálogo_venda_derivados(estoque_derivados)

            if len(estoque_derivados) == 0:
                print('[bold red]Não há derivados disponíveis no momento.[/bold red]\n')
                fontes_cores.linha()
                break
            
            opcoes_menu = []
            for produto in estoque_derivados:
                opcoes_menu.append(produto['produto'])
                
            titulo = "Escolha o produto com as setas (↑ e ↓) e aperte ENTER:"
            nome, indice = pick(opcoes_menu, titulo, indicator='=>', default_index=0)
            
            qtd = apenas_float('\nQuantidade que deseja (KG/L):  ')

            if qtd <= 0:
                print('[bold red]Quantidade inválida![/bold red]')
                continue

            for produto in estoque_derivados:
                if produto['produto'] == nome:
                    if qtd <= produto['quantidade']:

                        total = qtd * produto['valor do kg']

                        item_carrinho = {'produto': produto['produto'], 'quantidade': qtd, 'valor do kg': produto['valor do kg'], 'valor total do estoque': total}

                        carrinho.append(item_carrinho)

                        produto['quantidade'] -= qtd
                        produto['valor total do estoque'] = produto['quantidade'] * produto['valor do kg']

                        if produto['quantidade'] <= 0:
                            estoque_derivados.remove(produto)

                        print(f"[bold green]Adicionado ao carrinho: {nome}   R${total}[/bold green]")

                    else:
                        print('[bold red]Quantidade indisponível.[/bold red]')

                    break
            else:
                print('[bold red]Produto não encontrado.[/bold red]')
                continue

        elif opc == 2:
            catálogo_venda_animal(rebanho)

            if len([animal for animal in rebanho if animal['status'] == 'venda']) == 0:
                print('[bold red]Não há animais disponíveis para venda no momento.[/bold red]\n')
                fontes_cores.linha()
                break

            brinco = input('Digite o BRINCO do animal:  ')

            for item in carrinho:
                if 'brinco' in item and item['brinco'] == brinco:
                    print('[bold red]Esse animal já está no carrinho.[/bold red]\n')
                    break
            else:
                for animal in rebanho:
                    if animal['brinco'] == brinco and animal['status'] == 'venda':
                        rebanho.remove(animal)
                        carrinho.append(animal)
                        print('[bold green]Animal adicionado ao carrinho![/bold green]')
                        break
                else:
                    print('[bold red]Animal não encontrado.[/bold red]')


def remover_carrinho(carrinho, rebanho, estoque_derivados):

    if len(carrinho) == 0:
        print('[bold red]Carrinho vazio.[/bold red]')
        fontes_cores.linha()
        
    else:
        for item in carrinho:

            if 'brinco' in item:
                print(f"Animal | Brinco: {item['brinco']}")

            elif 'produto' in item:
                print(f"Produto | {item['produto']} | Qtd: {item['quantidade']}")

        print('''
        (1) Remover animal
        (2) Remover produto
        ''')

        opc = apenas_int('Escolha: ')

        if opc == 1:

            brinco = input('Brinco do animal: ')

            for item in carrinho:

                if 'brinco' in item and item['brinco'] == brinco:

                    carrinho.remove(item)
                    rebanho.append(item)

                    print('Animal removido do carrinho.')
                    break

            else:
                print('Animal não encontrado no carrinho.')

        elif opc == 2:

            nome = input('Nome do produto: ').lower()

            for item in carrinho:

                if 'produto' in item and item['produto'].lower() == nome:

                    for produto in estoque_derivados:

                        if produto['produto'] == item['produto']:

                            produto['quantidade'] += item['quantidade']
                            produto['valor total do estoque'] = (produto['quantidade'] * produto['valor do kg'])
                            break

                    else:
                        estoque_derivados.append({'produto': item['produto'], 'quantidade': item['quantidade'], 'valor do kg': item['valor do kg'], 'valor total do estoque': item['valor total do estoque']})

                    carrinho.remove(item)

                    print('Produto removido do carrinho.')
                    break

            else:
                print('Produto não encontrado no carrinho.')




def menu_cliente(usuarios, estoque_derivados, rebanho, carrinho):
    while True:
        fontes_cores.menu_cliente()
        print('''
            (1) - Visualizar catálogo
            (2) - Adicionar itens ao carrinho de compras
            (3) - Remover itens ou esvaziar carrinho
            (4) - Agendar transporte
            (5) - Finalizar pedido e emitir Recibo Detalhado
            (6) - Emitir segunda via de recibos anteriores
            (7) - Alterar dados cadastrais do comprador
            (0) - Sair
    ''')
        
        op = apenas_int('- Digite qual opção deseja realizar:  ')
        print('\n')  

        if op == 1:
            catálogo_venda_derivados(estoque_derivados)
            catálogo_venda_animal(rebanho)
            fontes_cores.linha()

        elif op == 2:
            adicionar_carrinho(estoque_derivados, rebanho, carrinho)

        elif op == 3:
            remover_carrinho(carrinho, rebanho, estoque_derivados)

