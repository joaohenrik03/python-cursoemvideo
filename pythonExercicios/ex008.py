metros = int(input('\033[35mQuantos metros deseja converter? '))
cent = metros * 100
mil = metros * 1000
print('\033[97m{} \033[35mmetros em centímetros é: \033[97m{}cm \n'
      '\033[97m{} \033[35mmetros em miliímetros é: \033[97m{}mm'.format(metros, cent, metros, mil))
