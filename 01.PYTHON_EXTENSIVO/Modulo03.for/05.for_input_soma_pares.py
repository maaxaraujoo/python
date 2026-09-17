
soma = 0
x = int(input("Digite um numero inteiro e positivo:"))
for cont in range(1, x + 1):
    if cont %2==0:
        soma = soma + cont
print(f"Soma de todos os numeros pares entre 1 e {x}:{soma}")
# 05.for_input_soma_pares.py
#
# QUESTÃO 5 — FOR + INPUT + SOMA DE NÚMEROS PARES
#
# Crie um programa que peça ao usuário um número inteiro e positivo.
#
# Requisitos:
#
# - Crie uma variável chamada soma começando em 0.
# - Solicite ao usuário um número inteiro e positivo.
# - Utilize for para percorrer os números de 1 até o número informado.
# - Utilize range() para controlar a sequência.
# - Utilize if para identificar os números pares.
# - Utilize o operador % para realizar essa verificação.
# - Some cada número par encontrado à variável soma.
# - Ao final, mostre a soma de todos os números pares entre 1
#   e o número informado pelo usuário.
#
# Objetivo:
# - Combinar input(), for, range(), if, %, e acumulador.
# - Entender como utilizar uma entrada do usuário para definir
#   o limite de uma repetição.
