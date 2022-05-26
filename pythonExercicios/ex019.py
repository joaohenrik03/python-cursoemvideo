from random import choice
aln1 = str(input('Primeiro aluno: '))
aln2 = str(input('Segundo aluno: '))
aln3 = str(input('Terceiro aluno: '))
aln4 = str(input('Quarto aluno: '))
lista = [aln1, aln2, aln3, aln4]
sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))

