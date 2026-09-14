# 28.lista_index.py
listanomes = ["Max", "Gabi", "Pedro", "Gustavo","Miguel"]

loc = listanomes.index("Pedro")

print(f"O Pedro está na posição: {loc}")
# QUESTÃO 28 — Encontrando a posição de um elemento com index()
#
# CONCEITO:
# O método index() serve para descobrir em qual índice
# determinado elemento está dentro de uma lista.
#
# Exemplo:
# lista = ["A", "B", "C"]
# lista.index("B") → 1
#
# QUESTÃO:
# Crie uma lista com 5 nomes.
#
# 1. Mostre a lista.
# 2. Peça ao usuário um nome que esteja na lista.
# 3. Use index() para descobrir a posição desse nome.
# 4. Mostre o nome e sua posição.
#
# Exemplo de saída:
# Nome procurado: Carlos
# Posição do nome: 2