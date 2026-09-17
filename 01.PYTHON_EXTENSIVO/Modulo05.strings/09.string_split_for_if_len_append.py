frase = "Eu estudo linguagem de programação por amar a cadeira"
frase_lista = frase.split()
frase_lista_4letras = []

for x in frase_lista:
    if len(x) > 4:
        frase_lista_4letras.append(x)

print(f"Lista com 4 palavras formada: {frase_lista_4letras}")
# 09.string_split_for_if_len_append.py
#
# QUESTÃO 09 — Filtrando palavras pelo tamanho
#
# Crie uma variável chamada frase contendo uma frase com
# várias palavras.
#
# O programa deve:
#
# 1. Utilizar split() para transformar a frase em uma lista
#    de palavras.
#
# 2. Criar uma nova lista para armazenar somente as palavras
#    que possuem mais de 4 caracteres.
#
# 3. Percorrer a lista de palavras utilizando for.
#
# 4. Utilizar len() e if para verificar quais palavras possuem
#    mais de 4 caracteres.
#
# 5. Utilizar append() para adicionar as palavras encontradas
#    na nova lista.
#
# 6. Mostrar a nova lista ao final.
#
# OBJETIVO:
# Praticar a combinação de split(), for, if, len() e append()
# para filtrar palavras de uma string e armazená-las em
# uma nova lista.