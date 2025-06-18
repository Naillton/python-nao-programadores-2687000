# Crie uma lista apenas com elementos numéricos
numeric = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_variada = [1, 23.5, "testando", True, [1, 2, 3, 4], {"chave": 20}]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_variada[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
for i in range(len(numeric)):
  if (i % 2 != 0):
    print(numeric[i])

# Remova da lista o último item
numeric.pop()

# Insira na lista um novo item
numeric.append(10)

# Remova da lista um item específico
numeric.remove(10)
print(numeric)