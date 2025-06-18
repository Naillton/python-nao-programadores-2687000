# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input("Digite seu nome: ")
ano_cadastro_linkedin = int(input("Digite o ano que conheceu o LinkedIn: "))
ano_atual = int(input("Digite o ano atual: "))
cursos_realizados = input("Digite os cursos realizados no linkedin separados por virgula: ")
# 2. Armazene esses dados em um dicionário
estudante = {
  'nome': nome,
  'cadastro_linkedin': ano_cadastro_linkedin,
  'ano_atual': ano_atual,
  'cursos_realizados': cursos_realizados.split(', ')
}
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print(f"Ola {estudante['nome']}, voce entrou no linkedin em {estudante['cadastro_linkedin']}, o ano de hoje e {estudante['ano_atual']} e ja se passaram {estudante['ano_atual'] - estudante['cadastro_linkedin']} anos, voce ja fez {len(estudante['cursos_realizados'])} cursos, sendo o primeiro {estudante['cursos_realizados'][0]} e o ultimo {estudante['cursos_realizados'][-1]}.")