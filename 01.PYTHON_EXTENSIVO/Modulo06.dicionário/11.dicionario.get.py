# 11.dicionario.get.py
print("------------------------INFORMAÇÃO DO ALUNO-----------------------")
aluno = {}
aluno['nome'] = input("Digite seu nome:")
aluno['turma'] = input("Digite sua turma:")
aluno['turno'] = input("Digite seu turno:")
aluno['local_sala'] = input("Digite o local da sua sala:")
print("")
print("-------------------------DADOS CADASTRADOS-------------------------")
print(aluno)
print("")
print("-------------------------CONSULTAR CHAVES-------------------------")
chave_consulta = input("Digite a chave que você deseja consultar:")
print("")
print("------------------------RESULTADO DA BUSCA------------------------")
print(f"Resultado da procura: {aluno.get(chave_consulta, 'Informação não cadastrada.')}")
print("")
print("------------------------------------------------------------------")
# QUESTÃO 11 — Consulta segura de informações
#
# Uma plataforma de cursos possui um cadastro com algumas
# informações de um aluno.
#
# 1. Crie um dicionário chamado aluno.
# 2. Cadastre pelo menos 4 informações diferentes.
# 3. Peça ao usuário o nome de uma chave que deseja consultar.
# 4. Utilize .get() para realizar a consulta.
# 5. Caso a chave não exista, mostre uma mensagem informando
#    que a informação não foi cadastrada.
#
# OBJETIVO:
# Praticar o método get() para consultar valores de um
# dicionário sem gerar KeyError quando a chave não existir.