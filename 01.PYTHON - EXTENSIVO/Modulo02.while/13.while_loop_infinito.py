# 13.while_loop_infinito.py
contador = 1
while True:
    print(contador)
    contador += 1

    if contador > 10:
        break

# QUESTÃO 13 — EVITANDO LOOP INFINITO
#
# Crie um programa que utilize while para contar de 1 até 10.
#
# Requisitos:
#
# - Crie uma variável chamada contador começando em 1.
# - Utilize while para controlar a repetição.
# - Mostre o valor de contador a cada repetição.
# - Atualize o contador dentro do while para que ele avance.
# - O programa deve terminar normalmente quando contador
#   ultrapassar 10.
#
# Objetivo:
# - Entender o que pode causar um loop infinito.
# - Aprender a importância de atualizar a variável de controle.
# - Garantir que um while tenha uma condição capaz de chegar
#   ao seu encerramento.
#
# Atenção:
# - O programa não pode ficar repetindo para sempre.
# - Pense no que aconteceria se contador nunca fosse atualizado.