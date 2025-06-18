# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Digite seu nome: ")
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input("Digite o total de dias estudados por semana: ")
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input("Digite a média de horas estudadas por dia: ")
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Digite o título do curso: ")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f"Ola {nome}, voce estudou por {total_dias} dia(s) na semana, com uma media de {total_horas} hora(s) por dia")