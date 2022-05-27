# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

count = 0
maior = 0
menor = 0
somaDosNumeros = 0

res = 'S'
while res.upper() == 'S':
    num = int(input('Digite um número: '))

    if count == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    count += 1
    somaDosNumeros += num

    res = str(input('Quer continuar? [S/N]: '))

media = somaDosNumeros / count

print('Você digitou {} números e a média foi {:.1f}'.format(count, media))
print('O maior valor foi {} e o menor foi {:.1f}!'.format(maior, menor))
