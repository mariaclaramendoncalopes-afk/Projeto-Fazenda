from rich import print
from rich.console import Console
from rich.table import Table

def linha():
    print("▂" * 75)
    print('\n')

def linha_comum():
    print('_' * 75)
    print('\n')

def título_fazenda():
    console = Console()
    console.print('''[bold blue]
    █▀▀ ▄▀█ ▀█ █▀▀ █▄ █ █▀▄ ▄▀█    █▀ █▀▀ █▀█ ▀█▀ ▄▀█ ▄▀
    █▀  █▀█ █▄ ██▄ █ ▀█ █▄▀ █▀█    ▄█ ██▄ █▀▄  █  █▀█ █▄█[/bold blue]''')

def título_cadastro_adm():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＣＡＤＡＳＴＲＯ  ＡＤＭＩＮＩＳＴＲＡＤＯＲ")
    console.print(tabela_titulo)
    print('\n')

def título_cadastro_cliente():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＣＡＤＡＳＴＲＯ  ＣＬＩＥＮＴＥ")
    console.print(tabela_titulo)
    print('\n')

def título_login():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＬＯＧＩＮ")
    console.print(tabela_titulo)
    print('\n')

def título_menu_adm():
    console = Console()
    console.print('''[bold blue]
           █▀▄▀█ █▀▀ █▄ █ █  █     ▄▀█ █▀▄ █▀▄▀█
           █ ▀ █ ██▄ █ ▀█ █▄▄█     █▀█ █▄▀ █ ▀ █[/bold blue]''')
    
def menu_cliente():
    console = Console()
    console.print('''[bold cyan]
           █▀▄▀█ █▀▀ █▄ █ █  █     █▀▀ █   █ █▀▀ █▄ █ ▀█▀ █▀▀
           █ ▀ █ ██▄ █ ▀█ █▄▄█     █▄▄ █▄▄ █ ██▄ █ ▀█  █  ██▄[/bold cyan]''')

def título_cadastrar_animal():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＣＡＤＡＳＴＲＡＲ  ＡＮＩＭＡＬ  ＮＯ  ＲＥＢＡＮＨＯ")
    console.print(tabela_titulo)

def título_buscar_animal():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＢＵＳＣＡＲ  ＡＮＩＭＡＬ  ＮＯ  ＲＥＢＡＮＨＯ")
    console.print(tabela_titulo)
    print('\n')

def título_modificar_animal():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＭＯＤＩＦＩＣＡＲ  ＤＡＤＯＳ  ＤＯ  ＡＮＩＭＡＬ")
    console.print(tabela_titulo)
    print('\n')

def título_remover_animal():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＭＯＶＥＲ  ＡＮＩＭＡＬ")
    console.print(tabela_titulo)
    print('\n')

def título_monitoramento_rebanho():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＭＯＮＩＴＯＲＡＭＥＮＴＯ  ＤＯ  ＲＥＢＡＮＨＯ")
    console.print(tabela_titulo)
    print('\n')

def título_gerenciar_producoes():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＧＥＲＥＮＣＩＡＲ  ＰＲＯＤＵＣＯＥＳ")
    console.print(tabela_titulo)
    print('\n')

def título_registrar_producao():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＧＩＳＴＲＡＲ  ＰＲＯＤＵＣＡＯ  ＤＩＡＲＩＡ")
    console.print(tabela_titulo)
    print('\n')

def título_relatorio_producao():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＬＡＴＯＲＩＯ  ＤＡＳ  ＰＲＯＤＵＣＯＥＳ")
    console.print(tabela_titulo)
    print('\n')

def título_gerenciamento_derivados():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＧＥＲＥＮＣＩＡＭＥＮＴＯ ＤＥ ＤＥＲＩＶＡＤＯＳ")
    console.print(tabela_titulo)
    print('\n')

def título_adicionar_derivado():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＡＤＩＣＩＯＮＡＲ 　ＤＥＲＩＶＡＤＯ")
    console.print(tabela_titulo)
    print('\n')

def título_ver_estoque():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＶＥＲ 　ＥＳＴＯＱＵＥ")
    console.print(tabela_titulo)
    print('\n')

def título_editar_produto():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＥＤＩＴＡＲ 　ＰＲＯＤＵＴＯ")
    console.print(tabela_titulo)
    print('\n')

def título_checagem():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＣＨＥＣＡＧＥＭ")
    console.print(tabela_titulo)
    print('\n')

def título_relatorio():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＬＡＴＯＲＩＯ")
    console.print(tabela_titulo)
    print('\n')

def título_editar_produto():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＥＤＩＴＡＲ  ＰＲＯＤＵＴＯ")
    console.print(tabela_titulo)
    print('\n')

def título_relatorio_pdf():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＬＡＴＯＲＩＯ ＥＭ ＰＤＦ")
    console.print(tabela_titulo)
    print('\n')

def título_animais_não_vacinados():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＡＮＩＭＡＩＳ  ＮＡＯ  ＶＡＣＩＮＡＤＯＳ")
    console.print(tabela_titulo)
    print('\n')

def título_relatorio_vendas():
    console = Console()
    tabela_titulo = Table(border_style="bold blue", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＬＡＴＯＲＩＯ ＤＥ ＶＥＮＤＡＳ")
    console.print(tabela_titulo)
    print('\n')

def título_derivados_disponiveis():
    console = Console()
    tabela_titulo = Table(border_style="bold cyan", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＤＥＲＩＶＡＤＯＳ  ＤＩＳＰＯＮＩＶＥＩＳ")
    console.print(tabela_titulo)
    print('\n')

def título_animais_disponiveis():
    console = Console()
    tabela_titulo = Table(border_style="bold cyan", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＡＮＩＭＡＩＳ  ＤＩＳＰＯＮＩＶＥＩＳ")
    console.print(tabela_titulo)
    print('\n')

def título_adicionar_carrinho():
    console = Console()
    tabela_titulo = Table(border_style="bold cyan", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＡＤＩＣＩＯＮＡＲ  ＮＯ  ＣＡＲＲＩＮＨＯ")
    console.print(tabela_titulo)
    print('\n')

def remover_itens_carrinho():
    console = Console()
    tabela_titulo = Table(border_style="bold cyan", show_header=False, padding=(0, 0), expand=False)
    tabela_titulo.add_column(width=60, justify="center")
    tabela_titulo.add_row("ＲＥＭＯＶＥＲ  ＩＴＥＮＳ ＤＯ ＣＡＲＲＩＮＨＯ")
    console.print(tabela_titulo)
    print('\n')