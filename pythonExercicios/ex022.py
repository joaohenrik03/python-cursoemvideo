# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras no total, sem considerar espaços.
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo: '))
nomeDividido = nome.split()
print('Em maiúsculo: {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Quantidade total de letras: {}'.format(len(nome.strip()) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(nomeDividido[0])))
