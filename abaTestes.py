import menu_cadastros




usuarios = [
    {'usuario' : 'kamille', 'senha' : '1234', 'acesso' : True},
    {'usuario' : 'clara', 'senha' : '5678', 'acesso' : True},
    {'usuario' : 'teste', 'senha' : '0000', 'acesso' : False},
]

rebanho = [
    {
        'brinco' : '001', 'tipo' : 'bovino', 'status' : 'lactação', 'peso' : 500, 'idade' : 4, 'sexo' : 'F',
        'valor' : 5000, 'produto' : 'leite bovino', 'produção diária' : 22, 'vacinado' : 'sim', 'observações' : ''
    },

    {
        'brinco' : '002', 'tipo' : 'bovino', 'status' : 'venda', 'peso' : 460, 'idade' : 5, 'sexo' : 'F',
        'valor' : 4700, 'produto' : 'leite bovino', 'produção diária' : 19, 'vacinado' : 'sim', 'observações' : '' 
    },

    {
        'brinco' : '002', 'tipo' : 'bovino', 'status' : 'venda', 'peso' : 460, 'idade' : 5, 'sexo' : 'F',
        'valor' : 4700, 'produto' : 'leite bovino', 'produção diária' : 19, 'vacinado' : 'sim', 'observações' : '' 
    },

    {
        'brinco' : '100', 'tipo' : 'caprino', 'status' : 'lactação', 'peso' : 55, 'idade' : 3, 'sexo' : 'F',
        'valor' : 900, 'produto' : 'leite caprino', 'produção diária' : 3, 'vacinado' : 'sim', 'observações' : 'doente'        
    },

    {
        'brinco' : '101', 'tipo' : 'caprino', 'status' : 'venda', 'peso' : 60, 'idade' : 4, 'sexo' : 'F',
        'valor' : 950, 'produto' : 'leite caprino', 'produção diária' : 4, 'vacinado' : 'sim', 'observações' : ''  
    },

    {
        'brinco' : '201', 'tipo' : 'ovino', 'status' : 'venda', 'peso' : 60, 'idade' : 4, 'sexo' : 'F',
        'valor' : 1100, 'produto' : 'leite ovino', 'produção diária' : 2, 'vacinado' : 'sim', 'observações' : ''  
    },

    {
        'brinco' : '301', 'tipo' : 'galinha', 'status' : 'produção', 'peso' : 3, 'idade' : 1, 'sexo' : 'F',
        'valor' : 50, 'produto' : 'ovos', 'produção diária' : 1, 'vacinado' : 'sim', 'observações' : 'doente'  
    }
]

animais_d = ['bovino', 'caprino', 'ovino', 'galinha']

relatorio = dict()

producao_diaria = dict()

estoque_derivados = [
    {'produto' : 'queijo coalho', 'quantidade' : 5 , 'valor do kg' : 24, 'valor total do estoque' : 120},
    {'produto' : 'queijo manteiga', 'quantidade' : 8 , 'valor do kg' : 15, 'valor total do estoque' : 120},
    {'produto' : 'requeijão', 'quantidade' : 3, 'valor do kg' : 30, 'valor total do estoque' : 90}
]

relatorio_vendas = []

carrinho = []



while True:
    menu_cadastros.mostrar_linha()
    menu_cadastros.nome_fazenda()
    print('''
          
    (1)  -  Cadastrar Administrador
    (2)  -  Cadastrar Usuário
    (3)  -  Login
    (0)  -  Encerrar Programa
          
    ''')

    op = input('Digite qual opção deseja realizar:  ')

    if op == '0':
        break  

    elif op == '1':
        menu_cadastros.cadastro_adm(usuarios)

    elif op == '2':
        menu_cadastros.cadastro_cliente(usuarios)

    elif op == '3':
        menu_cadastros.login(usuarios, animais_d)

    else:
        print('inválido')
