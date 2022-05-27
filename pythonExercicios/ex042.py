# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('=-=-=-=' * 7)
print('Analisador de Triângulos V2.0')
print('=-=-=-=' * 7)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Será formado um triângulo Equilátero!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Será formado um triângulo Isósceles!')
    else:
        print('Será formado um triângulo Escaleno!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
