trilha = []

# Crie uma função para selecionar o curso desejado em uma trilha profissional
def adicionar_curso(curso):
  trilha.append(curso)
  print(f"Curso '{curso}' adicionado à trilha.")
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
dicionario = {}
def adicionar_nivel():
  try:
    nivel = int(input("Digite o nível do curso: "))
    dicionario[trilha[0]] = nivel
  except ValueError as e:
    print(f"Erro: {e}")

def imprimir_funcoes():
  print("Funções disponíveis:")
  print("1. adicionar_curso(curso): Adiciona um curso à trilha.")
  print("2. adicionar_nivel(): Adiciona um nível ao curso atual.")

# Execute as funções
imprimir_funcoes()
adicionar_curso("Python Básico")
adicionar_nivel()

print(dicionario)

        