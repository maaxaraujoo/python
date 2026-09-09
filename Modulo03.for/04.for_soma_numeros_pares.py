
soma = 0
for cont in range(1, 21):
    if cont %2 == 0:
        soma = soma + cont

print(f"A soma dos numeros pares de 1 a 20 e:{soma}")

# 1 2 3 4 5 ---> 2 + 4 = 6
# 04.for_soma_numeros_pares.py
#
# QUESTÃO 4 — FOR + ACUMULADOR + NÚMEROS PARES
#
# Crie um programa que percorra os números de 1 até 20
# utilizando for.
#
# Requisitos:
#
# - Crie uma variável chamada soma começando em 0.
# - Utilize for para percorrer os números de 1 até 20.
# - Utilize if para identificar os números pares.
# - Utilize o operador % para realizar essa verificação.
# - Some cada número par encontrado à variável soma.
# - Ao final, mostre a soma de todos os números pares de 1 até 20.
#
# Objetivo:
# - Combinar for, range(), if, operador % e acumulador.
# - Aprender a acumular valores selecionados durante as repetições.