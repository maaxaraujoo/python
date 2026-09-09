quant = 0
for cont in range(1, 51):
    if cont %5==0:
        quant = quant + 1

print(f"Quantidade de múltiplos de 5: {quant}")
# 03.for_contagem_multiplos.py
#
# QUESTÃO 3 — FOR + CONTAGEM DE MÚLTIPLOS
#
# Crie um programa que percorra os números de 1 até 50
# utilizando for.
#
# Requisitos:
#
# - Crie uma variável chamada quant começando em 0.
# - Utilize for para percorrer os números de 1 até 50.
# - Utilize if para verificar quais números são múltiplos de 5.
# - Utilize o operador % para realizar essa verificação.
# - A cada múltiplo de 5 encontrado, aumente a variável quant
#   em 1.
# - Ao final, mostre a quantidade de múltiplos de 5 encontrados.
#
# Objetivo:
# - Aprender a utilizar um acumulador de quantidade dentro
#   de um for.
# - Combinar for, range(), if e o operador %.


