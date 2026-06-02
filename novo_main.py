import fontes_cores
import cadastros
import menu_adm
from rich import print
import builtins

input = lambda prompt="": builtins.input(print(prompt, end="") or "")




usuarios = [
    {'nome completo': 'kamille vieira da silva', 'usuario' : 'kamille', 'email' : 'kamille@gmail.com', 'telefone' : '83974007252', 'senha' : '1234', 'acesso' : True},
    {'nome completo': 'maria clara', 'usuario' : 'clara', 'email' : 'clara@hotmail.com', 'telefone' : '83000000000', 'senha' : '5678', 'acesso' : False},
]

rebanho = [
    {
        'brinco' : '001', 'tipo' : 'bovino', 'status' : 'lactação', 'peso' : 500, 'idade' : 4, 'sexo' : 'F',
        'valor' : 5000, 'produto' : 'leite bovino', 'produção diária' : 22, 'vacinado' : 's', 'observações' : ''
    },
    {
        'brinco' : '002', 'tipo' : 'bovino', 'status' : 'venda', 'peso' : 460, 'idade' : 5, 'sexo' : 'F',
        'valor' : 4700, 'produto' : 'leite bovino', 'produção diária' : 19, 'vacinado' : 'n', 'observações' : '' 
    },
    {
        'brinco' : '003', 'tipo' : 'bovino', 'status' : 'venda', 'peso' : 460, 'idade' : 5, 'sexo' : 'F',
        'valor' : 4700, 'produto' : 'leite bovino', 'produção diária' : 19, 'vacinado' : 's', 'observações' : '' 
    },
    {
        'brinco' : '100', 'tipo' : 'caprino', 'status' : 'lactação', 'peso' : 55, 'idade' : 3, 'sexo' : 'F',
        'valor' : 900, 'produto' : 'leite caprino', 'produção diária' : 3, 'vacinado' : 's', 'observações' : 'doente'        
    },
    {
        'brinco' : '101', 'tipo' : 'caprino', 'status' : 'venda', 'peso' : 60, 'idade' : 4, 'sexo' : 'F',
        'valor' : 950, 'produto' : 'leite caprino', 'produção diária' : 4, 'vacinado' : 's', 'observações' : ''  
    },
    {
        'brinco' : '201', 'tipo' : 'ovino', 'status' : 'venda', 'peso' : 60, 'idade' : 4, 'sexo' : 'F',
        'valor' : 1100, 'produto' : 'leite ovino', 'produção diária' : 2, 'vacinado' : 's', 'observações' : ''  
    },
    {
        'brinco' : '301', 'tipo' : 'galinha', 'status' : 'produção', 'peso' : 3, 'idade' : 1, 'sexo' : 'F',
        'valor' : 50, 'produto' : 'ovos', 'produção diária' : 1, 'vacinado' : 's', 'observações' : 'doente'  
    }
]

animais_d = ['bovino', 'caprino', 'ovino', 'galinha']

relatorio = list()

producao_diaria = dict()

estoque_derivados = [
    {'produto' : 'queijo coalho', 'quantidade' : 5 , 'valor do kg' : 24, 'valor total do estoque' : 120},
    {'produto' : 'queijo manteiga', 'quantidade' : 8 , 'valor do kg' : 15, 'valor total do estoque' : 120},
    {'produto' : 'requeijão', 'quantidade' : 3, 'valor do kg' : 30, 'valor total do estoque' : 90}
]

relatorio_vendas = []

carrinho = []

while True:
    fontes_cores.linha()
    fontes_cores.título_fazenda()
    print('\n')
    print('''
            [1]  CADASTRAR ADMINISTRADOR
            [2]  CADASTRAR CLIENTE
            [3]  LOGIN
            [0]  SAIR
    ''')
    print('\n')
    op = input(' - Qual opção deseja realizar:  ')
    print('\n')

    if op == '0':
        break

    elif op == '1':
        fontes_cores.linha_comum()
        fontes_cores.título_cadastro_adm()
        cadastros.cadastro_adm(usuarios)

    elif op == '2':
        fontes_cores.linha_comum()
        fontes_cores.título_cadastro_cliente()
        cadastros.cadastro_cliente(usuarios)

    elif op == '3':
        fontes_cores.linha_comum()
        fontes_cores.título_login()
        
        login = cadastros.login(usuarios)

        if login == 'administrador':
            menu_adm.menu_adm(usuarios, animais_d, rebanho, relatorio, producao_diaria, estoque_derivados)
            
        
        elif login == 'cliente':
            print('menu cliente')