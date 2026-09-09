# 12.while_true.py
cont = 1
while True:
    numeros = int(input("Digite um número:"))
    print(f"Número digitado:{numeros}")
    cont += 1
    if numeros == 0:
        break
# QUESTÃO 12 — WHILE TRUE
#
# Crie um programa que peça números inteiros ao usuário
# repetidamente.
#
# Requisitos:
#
# - Utilize while True para criar o laço de repetição.
# - Solicite um número inteiro ao usuário a cada repetição.
# - Mostre o número digitado.
# - Utilize if dentro do while.
# - Quando o usuário digitar o número 0, utilize break
#   para encerrar o laço.
# - O programa deve continuar solicitando números enquanto
#   o usuário não digitar 0.
#
# Objetivo:
# - Aprender a estrutura while True.
# - Entender como uma condição interna, junto com break,
#   pode controlar o encerramento do laço.