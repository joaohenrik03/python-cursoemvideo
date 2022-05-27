# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import date

ano = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano - nasc
    if idade > 18:
        maior += 1
    else:
        menor += 1
print('{} pessoa(s) ainda não atingiram a maioridade. mas {} já são de maiores!'.format(menor, maior))
