frase = "A vida é tão boa que esqueço as horas passarem"

palavra = frase.split()

for letra in palavra:
    if len(letra) > 4:
        print(f"{letra}")
# 08.string_split_for_if_len.py
#
# QUESTÃO 08 — Filtrando palavras pelo tamanho
#
# Crie uma variável chamada frase contendo uma frase com
# várias palavras.
#
# O programa deve:
#
# 1. Utilizar split() para transformar a frase em uma lista
#    de palavras.
#
# 2. Percorrer essa lista utilizando for.
#
# 3. Utilizar len() para verificar a quantidade de caracteres
#    de cada palavra.
#
# 4. Utilizar if para identificar somente as palavras que
#    possuem mais de 4 caracteres.
#
# 5. Mostrar na tela apenas as palavras que possuem mais
#    de 4 caracteres.
#
# OBJETIVO:
# Praticar a combinação de split(), for, if e len() para
# filtrar palavras de uma string de acordo com seu tamanho.
