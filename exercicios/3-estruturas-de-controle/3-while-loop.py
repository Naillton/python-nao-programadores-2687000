# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
inicial = 1
final = 5

# Crie um while loop que imprima na tela o nível atual
#while inicial <= final:
  #print(f"Nível atual: {inicial}")
  #inicial += 1

# Insira "else" no while loop anterior.
while inicial <= final:
  if (inicial % 2 == 0):
    print(f"Nível atual: {inicial} - Par")
  else:
    print(f"Nível atual: {inicial} - Ímpar")
  inicial += 1
