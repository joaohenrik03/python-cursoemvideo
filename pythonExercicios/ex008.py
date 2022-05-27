# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('\033[35mQuantos metros deseja converter? '))
cm = m * 100
mm = m * 1000
print('\033[97m{} \033[35mmetros em centímetros é: \033[97m{}cm \n'
      '\033[97m{} \033[35mmetros em miliímetros é: \033[97m{}mm'.format(metros, cm, m, mm))
