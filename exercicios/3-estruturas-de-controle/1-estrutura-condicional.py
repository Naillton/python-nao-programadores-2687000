# Declare 4 variáveis do tipo numérica
numero1 = 10
numero2 = 20
numero3 = 30
numero4 = 40

# Crie uma estrutura condicional para comparar dois números
if (numero1 >= numero2):
  print("A condição é verdadeira")
else:
  print("A condição é falsa")

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if (numero2 > numero1):
  print("A condição é verdadeira, o maior valor é:", numero2)
else:
  print("A condição é falsa, o maior valor é:", numero1)

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor


# Insira outras condições na estrutura condicional usando o elif
if (numero1 > numero2):
  print("A condição é verdadeira, o maior valor é:", numero1)
elif (numero3 > numero2):
  print("A condição é verdadeira, o maior valor é:", numero3)
else:
  print("So testa duas condicoes")

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (numero1 > numero2 or numero3 > numero2):
  print("A condição é verdadeira, pelo menos um número é maior que o segundo")
else:
  print("Nenhum número é maior que o segundo")

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if (numero1 < numero2 and numero3 < numero4):
  print("Ambas as condições são verdadeiras: numero1 é menor que numero2 e numero3 é menor que numero4")