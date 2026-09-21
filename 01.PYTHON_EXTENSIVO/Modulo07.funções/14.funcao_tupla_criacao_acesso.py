# 14.tupla_criacao_acesso.py
nome_doProduto = str(input(f"Qual o nome do seu produto?"))
categoria_doProduto = str(input(f"Qual a categoria desse produto?"))
preco_doProduto = int(input(f"Qual o valor do produto?"))

tuplaProduto0 = (nome_doProduto,categoria_doProduto,preco_doProduto)
print(f"Nome:{tuplaProduto0[0]}")
print(f"Categoria:{tuplaProduto0[1]}")
print(f"Valor:{tuplaProduto0[2]}")
print(f"Quantidade de valores na tupla:{len(tuplaProduto0)}")
# QUESTÃO 14 — Criando e acessando uma tupla
#
# Crie uma tupla chamada dados_produto.
#
# A tupla deve armazenar três informações sobre um produto:
# nome, categoria e preço.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do produto.
#
# 2. Pedir ao usuário a categoria do produto.
#
# 3. Pedir ao usuário o preço do produto.
#
# 4. Armazenar as três informações dentro da tupla.
#
# 5. Mostrar o nome do produto utilizando seu índice.
#
# 6. Mostrar a categoria utilizando seu índice.
#
# 7. Mostrar o preço utilizando seu índice.
#
# 8. Mostrar a quantidade de elementos existentes na tupla.
#
# OBJETIVO:
# Praticar a criação de tuplas, o acesso aos seus elementos
# através de índices e a utilização de len().