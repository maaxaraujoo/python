# 22.lista_slicing.py
lista = ["Uva","Morango","Limão","Melancia","Abacate","Laranja"]

print(f"Três primeiros elementos: {lista[:3]}")
print(f"Três primeiros elementos: {lista[:3]}")

# QUESTÃO 22 — FATIAMENTO BÁSICO DE LISTAS
#
# Crie uma lista contendo 6 frutas.
#
# Requisitos:
#
# - Mostre os 3 primeiros elementos utilizando slicing.
# - Mostre os elementos do índice 2 até o final utilizando slicing.
# - Mostre os elementos do índice 1 até o índice 4,
#   lembrando que o índice final não é incluído.
#
# Objetivo:
# - Aprender a utilizar lista[inicio:fim].
# - Entender que o índice inicial é incluído.
# - Entender que o índice final não é incluído.
# - Praticar slicing sem utilizar for.


# MÓDULO 4 — LISTAS
#
# BLOCO — FATIAMENTO (SLICING)
#
# O slicing permite pegar uma PARTE de uma lista.
#
# A estrutura básica é:
#
# lista[inicio:fim]
#
# IMPORTANTE:
# - O índice inicial é incluído.
# - O índice final NÃO é incluído.
#
# Exemplo:
#
# lista = ["A", "B", "C", "D", "E"]
#
# lista[1:4]
#
# Resultado:
# ["B", "C", "D"]
#
# Porque:
# índice 1 → entra
# índice 2 → entra
# índice 3 → entra
# índice 4 → não entra
#
# ----------------------------------------------------------
#
# Também podemos omitir o início:
#
# lista[:3]
#
# Pega do começo até o índice 3 (sem incluir o 3).
#
# Exemplo:
#
# lista[:3]
# → ["A", "B", "C"]
#
# ----------------------------------------------------------
#
# Podemos omitir o final:
#
# lista[2:]
#
# Pega do índice 2 até o final.
#
# Exemplo:
#
# lista[2:]
# → ["C", "D", "E"]
#
# ----------------------------------------------------------
#
# Podemos pegar a lista inteira:
#
# lista[:]
#
# Isso percorre todos os elementos da lista.
#
# ----------------------------------------------------------
#
# Também podemos utilizar um PASSO:
#
# lista[inicio:fim:passo]
#
# Exemplo:
#
# lista[0:5:2]
#
# Significa:
# - começar no índice 0;
# - parar antes do índice 5;
# - avançar de 2 em 2.
#
# Resultado:
# ["A", "C", "E"]
#
# ----------------------------------------------------------
#
# RESUMO:
#
# lista[inicio:fim]
# lista[inicio:fim:passo]
# lista[:fim]
# lista[inicio:]
# lista[:]