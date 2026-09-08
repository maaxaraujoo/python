# 10.while_break_maior_menor.py

cont = 1
aux = 0
while cont >= 1:
    maiornum = int(input("Digite um número:"))
    if maiornum > aux:
        aux = maiornum
    if maiornum == 0:
        break
    cont += 1
print(f"Maior número digitado até agora: {aux}")

# QUESTÃO 10 — BREAK + MAIOR VALOR
#
# Crie um programa que peça números inteiros ao usuário
# repetidamente utilizando while.
#
# Requisitos:
#
# - Solicite um número inteiro a cada repetição.
# - Utilize uma variável para armazenar o maior número informado.
# - O primeiro número informado deve ser utilizado como referência
#   inicial para o maior valor.
# - Compare os próximos números informados com o maior valor atual.
# - Atualize o maior valor quando encontrar um número maior.
# - Quando o usuário informar 0, utilize break para encerrar o laço.
# - Ao final, mostre qual foi o maior número informado.
#
# Objetivo:
# - Combinar while, break, if e comparação.
# - Trabalhar com uma variável que é atualizada durante as repetições.