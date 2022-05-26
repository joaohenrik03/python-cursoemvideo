from random import shuffle
aln1 = str(input('Primeiro aluno: '))
aln2 = str(input('Segundo aluno: '))
aln3 = str(input('Terceiro aluno: '))
aln4 = str(input('Quarto aluno: '))
lista = [aln1, aln2, aln3, aln4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)