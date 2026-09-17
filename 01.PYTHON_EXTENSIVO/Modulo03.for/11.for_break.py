# 11.for_break.py
for cont in range(1,11):
    print(f"Número {cont}º")
    
    if cont == 6:
        break
# QUESTÃO 11 — BREAK NO FOR
#
# Crie um programa que utilize for para percorrer os números
# de 1 até 10.
#
# Requisitos:
#
# - Utilize for.
# - Utilize range() para criar a sequência de 1 até 10.
# - Mostre cada número durante a repetição.
# - Utilize if dentro do for.
# - Quando o contador chegar ao número 6, utilize break
#   para interromper o for.
# - A sequência deve parar no número 6, mesmo que o range()
#   permita continuar até 10.
#
# Objetivo:
# - Aprender a utilizar break dentro de um for.
# - Entender que o break interrompe completamente o for,
#   mesmo que ainda existam valores na sequência.