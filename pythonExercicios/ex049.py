# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número: '))
for c in range(1, 10+1):
    print('{} x {} = {}'.format(num, c, num*c))
