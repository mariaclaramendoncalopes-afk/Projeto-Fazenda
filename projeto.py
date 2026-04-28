cadastros = []
while True:
    print('--- Fazenda Sertão ---')
    print('1 - criar perfil')
    print('2 - Entrar')
    op = int(input('Qual opção deseja fazer? '))


    if op == 1:
        usuario = input('Digite seu nome de usuário: ')
        cadastros.append(f'usuario: {usuario}')
        senha = input('Digite sua senha: ')
        cadastros.append(f'senha: {senha}')
        tipo = input('Digite o tipo de usuário (ADM / Cliente): ').lower()
        if tipo != 'adm' or tipo != 'cliente':
            while tipo != 'adm' and tipo != 'cliente':
                print('Tipo de usuário não definido')
                tipo = input('Digite o tipo de usuário (ADM / Cliente): ').lower()
            cadastros.append(f'tipo: {tipo}')
        else:
            cadastros.append(f'tipo: {tipo}')

'''
#apenas o ultimo usuario a cadastrar consegue entrar, não sei como ajeitar
    elif op ==2:
        print('--- Bem-vindo(a) de volta ---')
        usuario_entrar = input('Digite seu usuário: ')
        senha_entrar = input('Digite sua senha: ')
        if cadastros == []:
            print('Não há nenhum cadastro feito.')
        elif usuario == usuario_entrar and senha_entrar == senha:
            print('acesso consedido')
            if tipo == 'adm':
                print('você é adm')
            else:
                print('Vc é cliente')
        else:
            print('acesso negado')
'''