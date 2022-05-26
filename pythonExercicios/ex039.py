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


