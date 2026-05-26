def mostrar_linha():
    print('.__________.__________.__________.__________.__________.__________.')



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

