tempc = float(input('\033[97mInforme a temperatura em °C: '))
tempf = (( 9 * tempc) / 5) + 32
print('A temperatura de \033[31m{}°C \033[97mcorresponde a \033[31m{}°F !'.format(tempc, tempf))
