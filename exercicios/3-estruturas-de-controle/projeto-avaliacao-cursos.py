# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ["Python para Iniciantes", "Data Science com Python", "Desenvolvimento Web com Django", "Machine Learning com R", "JavaScript Avançado"]

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
python = cursos[0]
data_science = cursos[1]
django = cursos[2]
r = cursos[3]
javascript = cursos[4]

# 3. Crie um dicionário vazio para armazenar a nota do curso
cursos_notas = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if python in cursos:
  print(f"O curso '{python}' está na lista de cursos disponíveis.")
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
if python in cursos:
  nota_python = input(f"Por favor, avalie o curso '{python}' de 0 a 10: ")
  cursos_notas[python] = nota_python

print(f"A nota para o curso '{python}' foi armazenada: {cursos_notas[python]}")
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
if data_science in cursos:
  print(f"O curso '{data_science}' está na lista de cursos disponíveis.")
  nota_data_science = input(f"Por favor, avalie o curso '{data_science}' de 0 a 10: ")
  cursos_notas[data_science] = nota_data_science
  print(f"A nota para o curso '{data_science}' foi armazenada: {cursos_notas[data_science]}")