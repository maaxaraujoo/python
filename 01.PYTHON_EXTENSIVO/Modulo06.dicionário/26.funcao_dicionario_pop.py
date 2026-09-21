# 26.funcao_dicionario_pop.py
print("-----------------------FICHA CADASTRAL-----------------------")
inscricao = {}
inscricao['nome'] = input("Digite seu nome:")
inscricao['curso'] = input("Digite seu curso:")
inscricao['modal'] = input("Digite sua modalidade:")
inscricao['turno'] = input("Digite seu turno:")
print('')
print("-----------------------DADOS RECEBIDOS-----------------------")
print(inscricao)
print('')
remove_chave = input("Digite a chave que deseja remover:")
valor_removido = inscricao.pop(remove_chave) #devolve somente o valor que está na chave
print('')
print("-----------------------DADOS ALTERADOS-----------------------")
print(inscricao)
print(f"O valor'{valor_removido}' foi removido da chave '{remove_chave}'!")
print('')
print("-------------------------------------------------------------")
# QUESTÃO 26 — Removendo e recuperando um valor com pop()
#
# Uma plataforma de cursos possui informações sobre uma
# inscrição realizada por um aluno.
#
# Crie um dicionário chamado inscricao contendo:
# aluno, curso, modalidade e turno.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do aluno.
# 2. Pedir o curso escolhido.
# 3. Pedir a modalidade do curso.
# 4. Pedir o turno.
# 5. Armazenar todas as informações no dicionário.
# 6. Perguntar ao usuário qual chave deseja remover.
# 7. Utilizar pop() para remover a chave escolhida.
# 8. Armazenar o valor removido em uma variável.
# 9. Mostrar o valor que foi removido.
# 10. Mostrar o dicionário depois da remoção.
#
# OBJETIVO:
# Praticar o uso de pop() para remover uma chave de um
# dicionário e armazenar o valor removido em uma variável.