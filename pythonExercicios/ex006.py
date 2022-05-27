# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('\033[97mDigite um número: '))
x2 = num * 2
x3 = num * 3
xquadrad = num ** (1/2)
print('\033[35mO dobro de \033[32m{} \033[35mé: \033[32m{} \n\033[35mO triplo é: \033[32m{} \n\033[35mA raiz quadrada é: \033[32m{:.1f}'.format(num, x2, x3, xquadrad))

