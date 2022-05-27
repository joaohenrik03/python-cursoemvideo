# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Qual é o seu nome? ')
print('\033[97mÉ um prazer te conhecer, \033[36m{}\033[97m!'.format(nome))
