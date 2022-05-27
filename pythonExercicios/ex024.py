# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da sua cidade? ')).upper().strip().split()
primeiroNome = cidade[0]
print('SANTO' in primeiroNome)
