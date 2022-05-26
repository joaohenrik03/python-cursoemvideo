sexo = 's'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é o seu sexo?: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('[ERRO] Digite novamente.')

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'

print('Sexo {} detectado, fim.'.format(sexo))
