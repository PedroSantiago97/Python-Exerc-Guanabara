obj = input("Digite algo: ")

print("O tipo primitivo desse valor é: %s!" %type(obj))
print("Só tem espaços? %s!" %(obj.isspace())) # .isspace: Indentifica espaços no objeto
print("É um número? %s!" %(obj.isnumeric())) #
print("É alfabético? %s!" %(obj.isalpha()))
print("É alfanumérico %s!" %(obj.isalnum()))
print("Está em maiúsculas? %s!" %(obj.isupper()))
print("Está em minúsculas? %s!" %(obj.islower()))
print("Está capitalizada? %s!" %(obj.istitle()))





