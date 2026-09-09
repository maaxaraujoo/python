# 12.for_continue.py
for cont in range(1,11):
        if cont %2 == 0:
            continue
        print(f"Números ímpares:{cont}")
# QUESTÃO 12 — CONTINUE NO FOR
#
# Crie um programa que percorra os números de 1 até 10
# utilizando for.
#
# Requisitos:
#
# - Utilize for.
# - Utilize range() para percorrer os números de 1 até 10.
# - Utilize if dentro do for.
# - Identifique os números pares utilizando o operador %.
# - Quando encontrar um número par, utilize continue para
#   pular o restante daquela repetição.
# - Mostre somente os números ímpares.
# - Não utilize break.
#
# Objetivo:
# - Praticar o uso do continue dentro de um for.
# - Entender que o continue pula apenas a repetição atual,
#   permitindo que o for continue percorrendo a sequência.