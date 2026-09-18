# 16.funcao_desempacotamento_tupla.py
print("------------------DESEMPACOTAMENTO------------------")
nome_produto = str(input("Informe o nome do produto:"))
categoria_produto = str(input("Informe a categoria do produto:"))
preco_produto = int(input("Informe o valor do produto:"))
informacoes_produto = (nome_produto,categoria_produto,preco_produto)
nome_produto, categoria_produto, preco_produto = informacoes_produto
print("------------------IMPRESSÕES------------------")
print("")
print(f"Informações do produto em tupla:{informacoes_produto}")
print(f"Nome do produto mencionado: {nome_produto}")
print(f"Categoria do produto mencionado: {categoria_produto}")
print(f"Preço do produto mencionado: R${preco_produto} reais")
print("------------------FIM------------------")
# QUESTÃO 16 — Desempacotamento de tupla
#
# Crie uma tupla chamada informacoes_produto.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome de um produto.
#
# 2. Pedir ao usuário a categoria do produto.
#
# 3. Pedir ao usuário o preço do produto.
#
# 4. Armazenar as três informações dentro da tupla.
#
# 5. Desempacotar a tupla em três variáveis:
#    produto, categoria e preco.
#
# 6. Mostrar cada uma das três variáveis separadamente.
#
# 7. Não utilize índices da tupla para mostrar os valores depois
#    do desempacotamento.
#
# OBJETIVO:
# Praticar o desempacotamento de tuplas, distribuindo seus
# valores diretamente em variáveis de acordo com a posição.