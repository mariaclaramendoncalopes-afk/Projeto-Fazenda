import fontes_cores
import menu_adm
from rich import print
from pick import pick
import brazilcep
from datetime import datetime, timedelta
from fpdf import FPDF
from time import sleep

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

def emitir_recibo(dados_pedidos):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 10, 'RECIBO DE COMPRA', ln=True, align='C')

    pdf.ln(10)

    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'DADOS DO CLIENTE', ln=True)

    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 8, f"Nome: {dados_pedidos['nome completo']}", ln=True)
    pdf.cell(0, 8, f"Email: {dados_pedidos['email']}", ln=True)
    pdf.cell(0, 8, f"Telefone: {dados_pedidos['telefone']}", ln=True)

    pdf.ln(5)

    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'ITENS COMPRADOS', ln=True)

    pdf.set_font('Arial', '', 12)

    for item in dados_pedidos['itens']:
        
        if 'brinco' in item:
            
            nome_animal = item.get('produto', item.get('nome', 'Animal'))
            pdf.cell(0, 8, f"Animal: {nome_animal} | Brinco: {item['brinco']} | R$ {item['valor']:.2f}", ln=True)

        else:
            
            qtd_item = item.get('quantidade', item.get('qtd', item.get('Quantidade', 1)))
            valor_item = item.get('valor total do estoque', item.get('valor', 0.0))

            pdf.cell(0, 8, f"{item['produto']} | Quantidade: {qtd_item} | R$ {valor_item:.2f}", ln=True)

    pdf.ln(5)

    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'ENDERECO DE ENTREGA', ln=True)

    pdf.set_font('Arial', '', 12)

    pdf.cell(0, 8, f"Rua: {dados_pedidos['rua']}", ln=True)
    pdf.cell(0, 8, f"Numero: {dados_pedidos['numero']}", ln=True)
    pdf.cell(0, 8, f"Bairro: {dados_pedidos['bairro']}", ln=True)
    pdf.cell(0, 8, f"Cidade: {dados_pedidos['cidade']}", ln=True)
    pdf.cell(0, 8, f"Estado: {dados_pedidos['estado']}", ln=True)
    pdf.cell(0, 8, f"CEP: {dados_pedidos['cep']}", ln=True)

    pdf.ln(5)

    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'ENTREGA', ln=True)

    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 8, f"Data da entrega: {dados_pedidos['data_entrega']}", ln=True)

    pdf.ln(5)

    total_final = dados_pedidos['valor'] + dados_pedidos['frete']

    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'RESUMO FINANCEIRO', ln=True)

    pdf.set_font('Arial', '', 12)

    pdf.cell(0, 8, f"Subtotal: R$ {dados_pedidos['valor']:.2f}", ln=True)
    pdf.cell(0, 8, f"Frete: R$ {dados_pedidos['frete']:.2f}", ln=True)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"TOTAL: R$ {total_final:.2f}", ln=True)

    pdf.output('recibo.pdf')

    print('[bold green]Recibo gerado com sucesso![/bold green]')

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


def finalizar_pedido(login, carrinho, dados_pedidos):
    fontes_cores.linha()
    fontes_cores.título_finalizar_pedido()

    if len(carrinho) == 0:
        print('\n[bold red]Seu carrinho está vazio.[/bold red]\n')
        return
    
    total = 0

    for item in carrinho:

        if 'valor do kg' in item:

            print(f'Produto: {item["produto"]}')
            print(f'Quantidade: {item["quantidade"]}')
            print(f'Valor: R$ {item["valor total do estoque"]:.2f}\n')

            total += item['valor total do estoque']

        else:

            print(f'Animal: {item["tipo"]}')
            print(f'Brinco: {item["brinco"]}')
            print(f'Valor: R$ {item["valor"]:.2f}\n')

            total += item["valor"]

    print(f'Total parcial: R$ {total:.2f}')

    confirmar = obter_sim_nao('\nConfirmar pedido? (s/n):   ').lower()

    if confirmar != 's':
        return

    for item in carrinho:
        print

    cep = input('Digite o CEP: ').strip()

    endereco = brazilcep.get_address_from_cep(cep)

    print('\nEndereço encontrado:')
    print(f"Rua: {endereco['street']}")
    print(f"Bairro: {endereco['district']}")
    print(f"Cidade: {endereco['city']}")
    print(f"Estado: {endereco['uf']}")

    numero = input('\nNúmero da residência: ')

    hoje = datetime.today()

    data1 = hoje + timedelta(days=5)
    data2 = hoje + timedelta(days=10)
    data3 = hoje + timedelta(days=15)

    print(f'''
    Datas disponíveis:

    (1) {data1.strftime("%d/%m/%Y")}
    (2) {data2.strftime("%d/%m/%Y")}
    (3) {data3.strftime("%d/%m/%Y")}
    ''')

    opcao = apenas_int('Escolha uma data: ')

    if opcao == 1:
        data_entrega = data1.strftime("%d/%m/%Y")
    elif opcao == 2:
        data_entrega = data2.strftime("%d/%m/%Y")
    else:
        data_entrega = data3.strftime("%d/%m/%Y")


    if total >= 500:
        frete = 50
    else:
        frete = 145

    dados_pedidos = {
        'nome completo': login['nome completo'],
        'email': login['email'],
        'telefone': login['telefone'],
        'cep': cep,
        'rua': endereco['street'],
        'bairro': endereco['district'],
        'cidade': endereco['city'],
        'estado': endereco['uf'],
        'numero': numero,
        'data_entrega': data_entrega,
        'valor': total,
        'frete': frete,
        'itens': carrinho.copy()
    }

    print(f'Frete: R$ {frete:.2f}')
    print('\n[bold green]Pedido confirmado com sucesso.[/bold green]')
    print('[bold green]Emitindo recibo de compra...[/bold green]')
    sleep(2)
    emitir_recibo(dados_pedidos)

    return dados_pedidos



def menu_cliente(login, estoque_derivados, rebanho, carrinho, dados_pedidos):
    while True:
        fontes_cores.menu_cliente()
        print('''
            (1) - Visualizar catálogo
            (2) - Adicionar itens ao carrinho de compras
            (3) - Remover itens ou esvaziar carrinho
            (4) - Finalizar pedido | Agendar entrega
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

        elif op == 4:
            finalizar_pedido(login, carrinho, dados_pedidos)

