nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome...")
nomeup = nome.upper()
nomelow = nome.lower()
print(f"Seu nome em maiúsculas é: {nomeup}")
print(f"Seu nome em minusculas é: {nomelow}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
separado = nome.split(' ')
print(f"Seu primeiro nome tem {len(separado[0])} letras")


# print(f"Seu primeiro nome tem {nome.find(' ')} letras")



# .strip(): Retira os espaços do inicio e do final das strings
# .lower(): Deixa todas as letras minúsculas
# .upper(): Deixa todas as letras MAIÚSCULAS
# len(): Mostra o comprimento do objeto
# .split(): Separa o conjunto de um determinado objeto colocado entre ()
# .count(): Mostra a quantidade de um determinado objeto no meio do conjunto/Array
# .find(): Mostra a posição de um determinado objeto no conjunto/Array
 
