peso = float(input('Peso em KG: '))
altura = float(input('Altura em M: '))
imc = peso / (altura ** 2) #índice de massa corporal
if imc < 18.5:
    status = 'abaixo do peso'
elif 18.5 <= imc < 25:
    status = 'no peso ideal'
elif 25 <= imc < 30:
    status = 'com sobrepeso'
elif 30 <= imc <= 40:
    status = 'com obesidade'
else:
    status = 'com obesidade mórbida'
print('Seu IMC é {:.2f}, e você está {}!'.format(imc, status))
