# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('-=-' * 10)
print('CADASTRE UMA PESSOA')

idade = deMaior = homens = mulheresMenorDeVinte = 0
while True:
    print('-=-' * 10)
    idade = int(input('Idade: '))
    if idade < 0:
        break
    elif idade >= 18:
        deMaior += 1

    sexo = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if sexo == 'M':
            homens += 1
    print('-=-' * 10)

    if sexo == 'F' and idade < 20:
        mulheresMenorDeVinte += 1

    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=-' * 10)
print(f'Pessoas que tem mais de 18 anos: {deMaior}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheresMenorDeVinte}')
