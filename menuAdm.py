print('---Menu (ADM)---')
rebanho = []
animais = ('bovino de leite', 'caprino', 'ovino', 'suíno', 'leitão')
print(f'Animais da fazenda: {animais}')
tipo = input('Informe qual o tipo do animal: ').lower()
if tipo not in animais:
    while tipo not in animais:
        print('Este animal não existe na fazenda sertão')
        tipo = input('Informe qual o tipo do animal: ')

identificação = input('Existe algum tipo de identificação desse animal? (S/N): ').upper()
if identificação == 'S':
    identificação = input('Digite como identificar o animal: ')
else:
    identificação = 'Não identificavel'

stats = ('lactação','engorda', 'disponível para venda', 'vendido')
print(stats)
status = input('Informe o status do animal: ').lower()
if status not in stats:
    while status not in stats:
        print('Status não definido')
        status = input('Informe o status do animal: ')
rebanho.append([tipo, identificação, status])
print(rebanho)