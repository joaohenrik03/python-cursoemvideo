# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

total = maisDeMil = valorProdutoMaisBarato = valorProduto = 0
nomeProdutoMaisBarato = nomeProduto = ''
while True:
    nomeProduto = str(input('Nome do produto: ')).upper()

    valorProduto = int(input('Preço: R$'))

    if total == 0:
        valorProdutoMaisBarato = valorProduto

    if valorProduto < valorProdutoMaisBarato:
        valorProdutoMaisBarato = valorProduto
        nomeProdutoMaisBarato = nomeProduto
    if valorProduto > 1000:
        maisDeMil += 1

    total += valorProduto

    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-' * 5 + 'FIM DO PROGRAMA' + '-' * 5)
print(f'O total de compra foi {total}!')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeProdutoMaisBarato} que custa {valorProdutoMaisBarato}')
