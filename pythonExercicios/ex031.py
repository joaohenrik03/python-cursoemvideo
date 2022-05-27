# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da sua viagem (em km/h)? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem irá custar R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem irá custar R${:.2f}'.format(passagem))
