# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
maioridade = 0
maisvelho = ''
maisnovas = 0
for cont in range(1, 5):
    print('Pessoa {}'.format(cont))
    print('=-=-=-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade

    if sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            maisvelho = nome
    elif sexo == 'F':
        if idade < 20:
            maisnovas += 1

medidade = somaidade / 4
print('=-=-=-' * 5)
print('A idade média do grupo é {}.'.format(medidade))
print('O nome do homem mais velho é {}.'.format(maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(maisnovas))
