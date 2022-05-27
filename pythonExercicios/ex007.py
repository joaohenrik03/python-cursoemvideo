# Desenvolva um programa que leia as duas notas de um aluno(a), calcule e mostre sua média.

nota1 = float(input('\033[33mQual foi sua primeira nota? '))
nota2 = float(input('\033[33mQual foi sua segunda nota? '))

media = (nota1 + nota2) / 2
print('\033[34mSua média é: \033[32m{:.1f}'.format(media))


