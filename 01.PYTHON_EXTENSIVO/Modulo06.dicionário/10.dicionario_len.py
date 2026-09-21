# 27.funcao_dicionario_len.py
print("-----------------------FICHA CADASTRAL-----------------------")
participante = {}
participante['nome'] = input("Digite seu nome:")
participante['sobrenome'] = input("Digite seu sobrenome:")
participante['rua'] = input("Digite o nome da sua rua:")
participante['nacionalidade'] = input("Digite sua nacionalidade:")
participante['bairro'] = input("Digite seu bairro:")
print("")
print(len(participante))
print("-------------------------------------------------------------")
# QUESTÃO 27 — Quantidade de informações em um cadastro
#
# Uma plataforma de eventos precisa registrar algumas informações
# de um participante.
#
# 1. Crie um dicionário chamado participante.
# 2. Cadastre pelo menos 5 informações diferentes.
# 3. Utilize len() para descobrir quantas informações foram
#    cadastradas no dicionário.
# 4. Mostre o dicionário completo.
# 5. Mostre a quantidade de informações cadastradas.
#
# OBJETIVO:
# Praticar len() aplicado a dicionários.