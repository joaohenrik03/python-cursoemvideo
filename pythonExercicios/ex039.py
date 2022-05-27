# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sexo = int(input('''Qual é o seu gênero:
[1]-Masculino
[2]-Feminino
Sua opção: '''))
print('-=-=-=-=' * 5)
if sexo == 2:
    print('Você não precisa fazer o alistamento!')
elif sexo == 1:
    ano = int(input('Digite o ano que você nasceu: '))
    dataatual = date.today()
    idade = dataatual.year - ano

    if idade < 18:
        falta = 18 - idade
        print('Você tem {} anos e ainda falta {} anos para você se alistar!'.format(idade, falta))
    elif idade == 18:
        print('Você tem {} anos e está na hora de alistar!'.format(idade))
    else:
        passou = idade - 18
        print('Você tem {} anos, já passou do {} anos do seu alistamento!'.format(idade, passou))
else:
    print('\033[31m[ERRO] insira uma opção válida.\033[m')
print('-=-=-=-=' * 5)


