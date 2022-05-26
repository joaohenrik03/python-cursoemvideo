idade = int(input('Olá atleta, nos diga sua idade: '))
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('Com {} anos, você se encaixa na categoria {}.'.format(idade, categoria))