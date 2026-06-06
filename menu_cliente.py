import fontes_cores
import menu_adm
from rich import print

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



def catálogo(estoque_derivados, rebanho):
    fontes_cores.linha()
    fontes_cores.título_derivados_disponiveis()
    for produto in estoque_derivados:
        menu_adm.exibir_produtos(produto)
    
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
            break

        elif opc == 1:
            nome = input('\nNome do produto:  ').lower()
            qtd = apenas_float('\nQuantidade que deseja (KG/L):  ')

            if qtd <= 0:
                print('[bold red]Quantidade inválida![/bold red]')
                continue

            for produto in estoque_derivados:
                if produto['produto'] == nome:
                    if qtd <= produto['quantidade']:
                        total = qtd * produto['valor do kg']
                        carrinho.append([nome, qtd, total])

                        print(f"[bold green]Adicionado ao carrinho: {nome}   R${total}[/bold green]")

                    else:
                        print('[bold red]Quantidade indisponível.[/bold red]')

                    break

            else:
                print('[bold red]Produto não encontrado.[/bold red]')
                continue   
#falta continuar isso aq, dps continuar a op 2
        


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
        
        op = apenas_int('Digite qual opção deseja realizar:  ')
        print('\n')  

        if op == 1:
            catálogo(estoque_derivados, rebanho)

        elif op == 2:
            adicionar_carrinho(estoque_derivados, rebanho, carrinho)


