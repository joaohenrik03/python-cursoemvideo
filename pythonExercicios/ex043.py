# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Peso em KG: '))
altura = float(input('Altura em M: '))
imc = peso / (altura ** 2)
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
