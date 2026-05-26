from time import sleep

def mostrar_linha():
    print('.__________.__________.__________.__________.__________.')



def usuario_senha(usuarios):
    
    while True:
        usuario = input('Digite um novo usuário:  ').lower()

        for pessoa in usuarios:
            if pessoa['usuario'] == usuario:
                print('Já existe usuário com este nome, tente novamente.\n')
                break

        else:
            break

    while True:
        senha = input('Crie sua senha:  ')

        if len(senha) <= 3:
            print('Senha curta | Sua senha deve conter +3 caracteres ')
            continue
        
        if senha == usuario:
            print('Senha fraca! Senha não pode ser igual ao usuário ')
            continue

        confirmacao = input('Confirme sua senha:  ')
        print('\n')

        if senha != confirmacao:
            print('As senhas não coincidem. Tente novamente. \n')
            continue

        break
    return usuario, senha



def cadastro_adm(usuarios):
        mostrar_linha()
        print('''
            
  ＣＡＤＡＳＴＲＯ  ＡＤＭＩＮＩＳＴＲＡＤＯＲ

              ''')
        usuario, senha = usuario_senha(usuarios)

        usuarios.append({'usuario':usuario, 'senha': senha, 'acesso' : True})
        print('Realizando cadastro...')
        sleep(1)
        print('Aguarde alguns segundos...\n')
        sleep(3)
        print('ADM cadastrado com sucesso!  |  Realize o login ')
        print('\n')
         


def cadastro_cliente(usuarios):
        mostrar_linha()
        print('''
            
  ＣＡＤＡＳＴＲＯ  ＣＬＩＥＮＴＥ

              ''')
        usuario, senha = usuario_senha(usuarios)

        usuarios.append({'usuario':usuario, 'senha': senha, 'acesso' : False})
        print('Realizando cadastro...')
        sleep(1)
        print('Aguarde alguns segundos...\n')
        sleep(3)
        print('  Cliente cadastrado com sucesso!  |  Realize o login')
        print('\n')


def login(usuarios, animais_d):
        mostrar_linha()
        print('''
              
  ＲＥＡＬＩＺＡＲ  ＬＯＧＩＮ

              ''')
        usuario = input('Usuário:  ')
        senha = input('Senha:  ')

        for pessoa in usuarios:
            if usuario == pessoa['usuario'] and senha == pessoa['senha'] and pessoa['acesso'] == True:
                print('\nAcesso administrativo autorizado!')
                sleep(1)
                print('Redirecionando ao painel da fazenda...\n')
                sleep(3)
                print(f'\n\nBem vindo(a), {usuario}\n')
                sleep(1)
                mostrar_linha()
                print('\n')
                nome_fazenda()
                menu_adm(usuarios, usuario, animais_d)





def menu_adm(usuarios, usuario, animais_d):
    while True:
        print('\n')
        print('  ＭＥＮＵ  ＡＤＭＩＮＩＳＴＲＡＤＯＲ')
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

        op = input('Digite a opção que deseja realizar:  ')

        if op == '1':
            mostrar_linha()
            print('\n ＣＡＤＡＳＴＲＡＲ  ＡＮＩＭＡＬ  ＮＯ  ＲＥＢＡＮＨＯ\n')
            while True:
                print(f'| Tipo disponíveis: {animais_d} |\n')
                tipo = input('Informe qual tipo de animal deseja cadastrar:  ')
        break

          
     
                     






def Menu_Inicial():
    while True:
        mostrar_linha()
        print('''
    (1)  -  Cadastrar Administrador'
    (2)  -  Cadastrar Usuário'
    (3)  -  Login'
    (0)  -  Encerrar Programa
        ''')

        op = input('Digite qual opção deseja realizar:  ')

        '''if op == 0:
            break  #colocar opção bonitinha pra encerrar programa

        elif op == '1':
            Cadastro_ADM()

        elif op == '2':
            print('Cadastro usuários')

        elif op == '3':
            print('login')

        #colocar um else, caso for inválido
        '''

        



def nome_fazenda():
    print('''
  █▀▀ ▄▀█ ▀█ █▀▀ █▄ █ █▀▄ ▄▀█   █▀ █▀▀ █▀█ ▀█▀ ▄▀█ ▄▀█
  █▀  █▀█ █▄ ██▄ █ ▀█ █▄▀ █▀█   ▄█ ██▄ █▀▄  █  █▀█ █▄█
''')
                                                               
