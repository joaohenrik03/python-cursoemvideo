# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('===RADAR V1.0===')

vel = float(input('Qual a velocidade do veículo em km/h? '))
velMax = 80.0

if vel > velMax:
    multa = (vel - velMax) * 7
    print('=-=-=-= MULTADO! =-=-=-=\n'
          'Você foi multado em R${:.2f}, por estar acima da velocidade permitida! Sua velocidade: {:.1f}Km/h'
          .format(multa, vel))
else:
    print('=-=-=-= TUDO CERTO, BOA VIAGEM!=-=-=-=')
