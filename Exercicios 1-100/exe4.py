obj = input("Digite algo: ")

print("O tipo primitivo desse valor é: %s!" %type(obj))# type(): Indentifica o tipo do objeto
print("Só tem espaços? %s!" %(obj.isspace())) # .isspace: Indentifica espaços no objeto
print("É um número? %s!" %(obj.isnumeric())) # .isnumeric: Indentifica se o objeto é um numero
print("É alfabético? %s!" %(obj.isalpha())) # .isalpha: Indentifica se o objeto possui letras
print("É alfanumérico %s!" %(obj.isalnum())) # .isalnum: Indentifica se o objeto possui letras e numeros
print("Está em maiúsculas? %s!" %(obj.isupper())) # .isupper: Indentifica se o objeto esta em Maiusculas
print("Está em minúsculas? %s!" %(obj.islower())) # .islower: Indentifica se o objeto esta em Minusculas
print("Está capitalizada? %s!" %(obj.istitle())) # .istitle: Indentifica se o objeto esta em maiusculas ou minusculas






