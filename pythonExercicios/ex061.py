# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
count = 1

while count <= 10:
    print('{}'.format(termo), end=" -> ")
    termo += razao
    count += 1

print('Acabou!')
