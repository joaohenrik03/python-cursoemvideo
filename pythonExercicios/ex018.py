import math
ang = float(input('Digite o ângulo que você deseja: '))
sn = math.sin(math.radians(ang))
cs = math.cos(math.radians(ang))
tt = math.tan(math.radians(ang))
print('O ângulo de {0} tem o SENO de {1:.2f} \n'
      'O ângulo de {0} tem o COSSENO de {2:.2f} \n'
      'O ângulo de {0} tem o TANGENTE de {3:.2f}'.format(ang, sn, cs, tt))
