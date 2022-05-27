# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).upper()
print('Tem SILVA no seu nome: {}'.format('SILVA' in nome))
