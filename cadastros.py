from rich import print
from time import sleep
import fontes_cores
from rich.console import Console
import re
import json
import os

def senhas(usuarios):
    while True:
        nome_completo = input('Digite seu nome completo:  ').strip()

        if nome_completo.isalpha():
            nome_completo = nome_completo.lower()
            break
        
        print('\n[bold red]NOME INVÁLIDO:[/bold red] Digite seu nome completo (apenas letras).\n')

    while True:
        usuario = input('Digite um novo usuário:  ').lower()

        if len(usuario) <= 3:
           print('\n[bold red]Seu usuário deve conter +3 caracteres[/bold red]\n')
           continue

        for pessoa in usuarios:
            if pessoa['usuario'] == usuario:
                print('\n[bold red]Já existe usuário com esse nome. Tente novamente.[/bold red]\n')
                break
        else:
            break
        
    regex_email = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    while True:
        email = input('Digite seu e-mail:  ').lower()
 
        if not re.match(regex_email, email):
            print('\n[bold red]❌ E-MAIL INVÁLIDO:[/bold red] Use o formato padrão (exemplo@email.com)\n')
            continue

        for pessoa in usuarios:
            if pessoa['email'] == email:
                print('\n[bold red]Já existe usuário com esse E-mail. Tente novamente.[/bold red]\n')
                break
        else:
            break

    regex_tel = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
    while True:
        telefone = input('Digite seu Telefone/WhatsApp (com DDD):  ')
        apenas_numeros = re.sub(r'\D', '', telefone)
        if re.match(regex_tel, telefone) and len(apenas_numeros) in [10, 11]:
            break
        print('\n[bold red]❌ TELEFONE INVÁLIDO:[/bold red] Digite o DDD + número (ex: 83999999999)\n')

    while True:
        senha = input('Crie sua senha:  ')

        if len(senha) <= 3:
            print('\n[bold red]SENHA CURTA:[/bold red] Sua senha deve conter +3 caracteres\n')
            continue
        
        if senha == usuario:
            print('\n[bold red]SENHA FRACA:[/bold red] Senha não pode ser igual ao usuário\n')
            continue

        confirmacao = input('Confirme sua senha:  ')

        if senha != confirmacao:
            print('\n[bold red]As senhas não coincidem. Tente novamente.[/bold red]\n')
            continue
        
        break

    return nome_completo, usuario, email, telefone, senha


def cadastro_adm(usuarios):
    nome_completo, usuario, email, telefone, senha = senhas(usuarios)

    usuarios.append({'nome completo': nome_completo, 'usuario': usuario, 'email' : email, 'telefone': telefone, 'senha': senha, 'acesso': True})

    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

    print('\n')
    print('[bold cyan]Realizando cadastro...[/bold cyan]')
    sleep(1)
    print('[bold cyan]Aguarde alguns segundos...[/bold cyan]\n')
    sleep(3)
    print('[bold blue]ADM cadastrado com sucesso!  |  Realize o login[/bold blue]')
    print('\n')


def cadastro_cliente(usuarios):
    nome_completo, usuario, email, telefone, senha = senhas(usuarios)

    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

    usuarios.append({'nome completo': nome_completo, 'usuario': usuario, 'email' : email, 'telefone': telefone, 'senha': senha, 'acesso': False})
    print('\n')
    print('[bold cyan]Realizando cadastro...[/bold cyan]')
    sleep(1)
    print('[bold cyan]Aguarde alguns segundos...[/bold cyan]\n')
    sleep(3)
    print('[bold blue]CLIENTE cadastrado com sucesso!  |  Realize o login[/bold blue]')
    print('\n')


def login(usuarios):
    usuario = input('\033[1;94m|  Usuário  |   \033[m')
    senha = input('\033[1;94m|   Senha   |   \033[m')

    for pessoa in usuarios:
        if usuario == pessoa['usuario'] and senha == pessoa['senha'] and pessoa['acesso'] == True:
            print('\n\n[bold cyan]Acesso administrativo autorizado![/bold cyan]\n')
            sleep(1)
            print('Redirecionando ao painel da fazenda...\n')
            sleep(3)
            fontes_cores.linha()
            print(f'                   Bem vindo(a), {usuario}\n\n')
            sleep(1)
            return pessoa
        
        elif usuario == pessoa['usuario'] and senha == pessoa['senha'] and pessoa['acesso'] == False:
            print('\n\n[bold cyan]Acesso do Cliente autorizado![/bold cyan]\n')
            sleep(1)
            print('Abrindo a nossa lojinha da fazenda...')
            sleep(3)
            fontes_cores.linha()
            print(f'            Seja muito bem-vindo(a) à Fazenda, {pessoa["nome completo"]}!\n\n')
            sleep(1)
            return pessoa
    else:    
        print('\n[bold red]Usuário não encontrado[/bold red]\n')
        input('\nPressione a tecla ENTER para retornar ao menu')
        print('\n')
        return