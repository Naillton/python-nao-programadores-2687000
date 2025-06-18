# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 2. Crie um for loop para percorrer todos os elementos da lista
for i in range(len(numeros)):
  print(numeros[i])
# 3. Crie uma estrutura condicional para verificar cada número da lista:
for i in range(len(numeros)):
  if (numeros[i] % 2 == 0):
    print(f"{numeros[i]} é par")
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"

#for i in range(len(numeros)):
#  if (numeros[i] % 3 == 0):
#    numeros[i] = "Fizz"
#print(numeros)

# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"

#for i in range(len(numeros)):
#  if (numeros[i] % 5 == 0):
#    numeros[i] = "Buzz"
#print(numeros)

# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
for i in range(len(numeros)):
  if (numeros[i] % 3 == 0 and numeros[i] % 5 == 0):
    numeros[i] = "FizzBuzz"
print(numeros)