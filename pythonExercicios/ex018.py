# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite o ângulo que você deseja: '))
sn = math.sin(math.radians(ang))
cs = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo de {0} tem o SENO de {1:.2f} \n'
      'O ângulo de {0} tem o COSSENO de {2:.2f} \n'
      'O ângulo de {0} tem o TANGENTE de {3:.2f}'.format(ang, sn, cs, tg))
