# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

soma = 0
impar = 0
for c in range(0, 501):
    if c % 2 != 0 and c % 3 == 0:
        impar += 1
        soma += c
print('A soma entre os {} números ímpares que são múltiplos de três é: {}'.format(impar, soma))
