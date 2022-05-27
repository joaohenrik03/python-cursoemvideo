# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('\033[34mPrimeiro número: '))
num2 = int(input('Segundo número: '))

print('\033[97m-=-=-=' * 5)
if num1 > num2:
    print('\033[32mO primeiro número é maior!')
elif num2 > num1:
    print('\033[32mO segundo número é maior!')
else:
    print('\033[32mOs dois números são iguais!')
print('\033[97m-=-=-=' * 5)