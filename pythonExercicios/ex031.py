distancia = float(input('Qual a distância da sua viagem (em km/h)? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem irá custar R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem irá custar R${:.2f}'.format(passagem))
