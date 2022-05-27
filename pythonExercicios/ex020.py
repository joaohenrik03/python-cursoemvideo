# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aln1 = str(input('Primeiro aluno: '))
aln2 = str(input('Segundo aluno: '))
aln3 = str(input('Terceiro aluno: '))
aln4 = str(input('Quarto aluno: '))

lista = [aln1, aln2, aln3, aln4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
