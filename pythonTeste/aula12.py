nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'João':
    print('Esse nome é perfeito!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))