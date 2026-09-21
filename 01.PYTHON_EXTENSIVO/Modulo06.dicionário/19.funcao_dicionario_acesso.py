# 19.funcao_dicionario_acesso.py
funcionario = {}
funcionario["nome"] = str(input("Digite seu Nome:"))
funcionario["departamento"] = str(input("Digite seu Depatamento:"))
funcionario["salario"] = int(input("Digite seu Salário:"))

print(f"Nome:{funcionario["nome"]}")
print(f"Departamento:{funcionario["departamento"]}")
print(f"Salário:{funcionario["salario"]}")

# QUESTÃO 19 — Acessando valores pelas chaves
#
# Uma empresa mantém informações de um funcionário em um
# dicionário.
#
# Crie um dicionário chamado funcionario contendo:
# nome, departamento e salario.
#
# O programa deve:
#
# 1. Receber do usuário o nome do funcionário.
# 2. Receber o departamento.
# 3. Receber o salário.
# 4. Armazenar as três informações no dicionário.
# 5. Acessar cada valor utilizando sua respectiva chave.
# 6. Mostrar cada informação separadamente.
#
# OBJETIVO:
# Praticar o acesso aos valores de um dicionário utilizando
# suas chaves.
