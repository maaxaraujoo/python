# 09.while_break_soma.py

cont = 1
soma = 0
while cont >= 1:
    numeros = int(input("Digite um número:"))
    soma += numeros

    if numeros == 0:
        break
print(f"Os valores dos números digitados somados é: {soma}")
# QUESTÃO 9 — BREAK + ACUMULADOR
#
# Crie um programa que peça números inteiros ao usuário
# repetidamente utilizando while.
#
# Requisitos:
#
# - Crie uma variável chamada soma começando em 0.
# - Solicite um número inteiro ao usuário a cada repetição.
# - Enquanto o usuário não informar 0, some o número informado
#   à variável soma.
# - Utilize if dentro do while.
# - Quando o usuário informar 0, utilize break para interromper
#   o laço.
# - Após o encerramento do while, mostre o valor final da soma.
#
# Objetivo:
# - Combinar while, break e acumulador.
# - Entender que o break pode determinar o momento de encerramento
#   do laço, enquanto o acumulador mantém um resultado durante
#   as repetições.