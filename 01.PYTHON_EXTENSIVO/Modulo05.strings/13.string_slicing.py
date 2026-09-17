# 13.string_slicing.py

palavra = "Viralizei"

print(f"Palavra: {palavra}")
print(f"Indice 0 até o índice 3 da palavra {palavra}:{palavra[0:3]}")
print(f"Indice 1 até o índice 5 da palavra com passo 2 {palavra}:{palavra[1:5:2]}")
print(f"{palavra} no modo inverso:{palavra[::-1]}")

# QUESTÃO 13 — Fatiando uma string com slicing
#
# Crie uma variável chamada palavra contendo:
#
# "Python"
#
# O programa deve:
#
# 1. Mostrar a palavra completa.
#
# 2. Utilizar slicing para mostrar os caracteres do índice 0
#    até o índice 3, lembrando que o índice final não é incluído.
#
# 3. Utilizar slicing com início no índice 1, final no índice 5
#    e passo 2.
#
# 4. Utilizar slicing com passo -1 para mostrar a palavra
#    completamente na ordem inversa.
#
# OBJETIVO:
# Praticar slicing em strings utilizando início, fim e passo,
# incluindo o uso de passo negativo.