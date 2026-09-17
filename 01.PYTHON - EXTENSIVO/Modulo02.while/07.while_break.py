contador = 1 
while contador <= 10: 
    print(contador) 
    if contador == 5: 
        break 
    contador = contador + 1
# 07.while_break.py
#
# QUESTÃO 7 — BREAK
#
# Crie um programa que utilize while para contar de 1 até 10.
#
# Requisitos:
#
# - Crie uma variável de controle chamada contador começando em 1.
# - Utilize while para realizar a contagem.
# - Mostre o valor do contador a cada repetição.
# - Utilize if dentro do while.
# - Quando o contador chegar ao número 5, utilize break
#   para interromper o laço.
# - A contagem deve ser interrompida no 5, mesmo que a condição
#   do while ainda permita que o laço continue.
#
# Objetivo:
# - Aprender a utilizar o break para interromper um laço
#   antes que sua condição principal se torne falsa.