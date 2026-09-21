#18.funcao_dicionario_criacao_estrutura.py
# QUESTÃO 18 — Criando e preenchendo um dicionário
funcionario = {}
funcionario["nome"] = str(input("Digite seu nome:"))
funcionario["idade"] = int(input("Digite sua idade:"))
funcionario["cargo"] = str(input("Digite seu cargo:"))

print(f"Informações recebidas: {funcionario}")
# Uma empresa precisa registrar informações básicas de um
# funcionário recém-contratado.
#
# Crie um dicionário chamado funcionario.
#
# O programa deve:
#
# 1. Criar o dicionário inicialmente vazio.
#
# 2. Pedir ao usuário:
#    - nome do funcionário;
#    - idade;
#    - cargo.
#
# 3. Adicionar cada informação ao dicionário utilizando uma
#    chave diferente para cada dado.
#
# 4. Ao final, mostrar o dicionário completo na tela.
#
# OBJETIVO:
# Praticar a criação de um dicionário vazio e a adição de
# informações utilizando pares de chave e valor.
