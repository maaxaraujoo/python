# 08.while_break_condicao.py

cont = 1

while cont >= 1:
    numeros = int(input("Digite um número:"))
    print(f"Número digitado: {numeros}")
    if numeros == 0:
        break
# QUESTÃO 8 — BREAK COM CONDIÇÃO
#
# Crie um programa que peça números inteiros ao usuário
# repetidamente utilizando while.
#
# Requisitos:
#
# - Solicite um número inteiro ao usuário a cada repetição.
# - Utilize uma variável para armazenar o número informado.
# - O programa deve continuar pedindo números enquanto o laço
#   estiver sendo executado.
# - Utilize if dentro do while.
# - Quando o usuário informar o número 0, utilize break
#   para interromper o laço.
# - Enquanto o número informado não for 0, mostre o número
#   digitado.
#
# Objetivo:
# - Aprender a utilizar o break para criar uma condição de
#   saída dentro de um while.
# - Entender que o break pode interromper o laço a qualquer
#   momento quando uma condição específica for atingida.