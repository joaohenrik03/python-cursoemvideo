obj = input('\033[97mDigite algo: ')
print(type(obj))
print('\033[31mÉ numérico? \033[97m{}'.format(obj.isnumeric()))
print('\033[32mÉ um alfanúmero? \033[97m{}'.format(obj.isalnum()))
print('\033[33mÉ alfabético? \033[97m{}'.format(obj.isalpha()))
print('\033[34mEsta em minúsculas? \033[97m{}'.format(obj.islower()))
print('\033[35mSó tem espaços? \033[97m{}'.format(obj.isspace()))
print('\033[36mEsta capitalizada? \033[97m{}'.format(obj.istitle()))
print('\033[37mEsta em maiúsculas? \033[97m{}'.format(obj.isupper()))


