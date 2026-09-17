# 17.string_isdigit_isalpha.py
numeros = "145743"
numeroscLetras = "8,6,4,a,b,y"
print("----------Verificando se temos somente NÚMEROS na PRIMEIRA variável----------")
print(f"Primeira variável:{numeros}")
print(numeros.isdigit())#verifica se todos os caracteres da string são dígitos.
print("----------Verificando se temos somente LETRAS na SEGUNDA variável----------")
print(f"Segunda variável:{numeroscLetras}")
print(numeroscLetras.isalpha()) #verifica se todos os caracteres são letras.


# QUESTÃO 17 — Verificando caracteres com isdigit() e isalpha()
#
# Crie duas variáveis:
#
# 1. Uma variável chamada numero contendo:
#    "12345"
#
# 2. Uma variável chamada palavra contendo:
#    "Python"
#
# O programa deve:
#
# 1. Mostrar o conteúdo da variável numero.
#
# 2. Utilizar isdigit() para verificar se numero contém
#    somente números.
#
# 3. Mostrar o resultado da verificação.
#
# 4. Mostrar o conteúdo da variável palavra.
#
# 5. Utilizar isalpha() para verificar se palavra contém
#    somente letras.
#
# 6. Mostrar o resultado da verificação.
#
# OBJETIVO:
# Praticar isdigit() e isalpha() para verificar se uma
# string contém somente números ou somente letras.