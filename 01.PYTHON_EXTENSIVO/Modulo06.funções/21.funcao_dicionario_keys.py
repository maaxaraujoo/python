# 21.funcao_dicionario_keys.py
inscricao = {}
inscricao['nome'] = str(input("Digite o nome do seu curso:"))
inscricao['modal'] = str(input("Digite a modalidade do seu curso:"))
inscricao['tuno'] = str(input("Digite o turno do seu curso:"))

for cont in inscricao.keys():
    print(f"{cont}")

# QUESTÃO 21 — Percorrendo as chaves de um dicionário
#
# Uma plataforma de cursos possui uma lista de informações
# sobre uma inscrição.
#
# Crie um dicionário chamado inscricao contendo:
# curso, modalidade e turno.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do curso.
# 2. Pedir a modalidade do curso.
# 3. Pedir o turno escolhido.
# 4. Armazenar as informações no dicionário.
# 5. Utilizar .keys() para percorrer as chaves do dicionário.
# 6. Mostrar cada chave separadamente.
#
# OBJETIVO:
# Praticar o uso de .keys() para acessar e percorrer as
# chaves de um dicionário.