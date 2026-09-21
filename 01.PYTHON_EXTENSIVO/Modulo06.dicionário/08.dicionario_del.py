# 25.funcao_dicionario_del.py
print("-----------------------FICHA CADASTRAL-----------------------")
dicionario = {}
dicionario['nome'] = input("Nome particular:")
dicionario['tipo'] = input("Tipo do ingresso:")
dicionario['setor'] = input("Setor escolhido:")
print('')
print("-----------------------IMPRESSÕES-----------------------")
print(dicionario)
print('')
remover_chave = input("Chave que deseja remover:")
print('')
del dicionario[remover_chave]
print(dicionario)
# QUESTÃO 25 — Removendo informações com del
#
# Uma plataforma de eventos possui informações sobre uma
# inscrição realizada por um participante.
#
# Crie um dicionário chamado inscricao contendo:
# participante, evento, ingresso e setor.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do participante.
# 2. Pedir o nome do evento.
# 3. Pedir o tipo de ingresso.
# 4. Pedir o setor escolhido.
# 5. Armazenar todas as informações no dicionário.
# 6. Perguntar ao usuário qual informação da inscrição deve ser
#    removida.
# 7. Utilizar del para remover a chave escolhida.
# 8. Mostrar o dicionário depois da remoção.
#
# OBJETIVO:
# Praticar a remoção de uma chave e seu respectivo valor
# utilizando del.
