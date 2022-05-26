print('===RADAR V1.0===')
vel = float(input('Qual a velocidade do veículo em km/h? '))
velmax = 80.0
if vel > velmax:
    multa = (vel - velmax) * 7
    print('=-=-=-= MULTADO! =-=-=-=\n'
          'Você foi multado em R${:.2f}, por estar acima da velocidade permitida! Sua velocidade: {:.1f}Km/h'.format(multa, vel))
else:
    print('=-=-=-= TUDO CERTO, BOA VIAGEM!=-=-=-=')
