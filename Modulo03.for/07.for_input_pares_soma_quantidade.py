numero = int(input("Digite um numero inteiro positivo:"))

soma = 0
quant = 0
print("----Números pares encontrados:----")
for cont in range(1, numero + 1):
    if cont %2==0:
        print(cont)
        quant = quant + 1
        soma = soma + cont
print("--------------------------------------")
print(f"Soma dos numeros pares:{soma}")
print(f"Quantidade dos numeros pares:{quant}")
print("--------------------------------------")
# 07.for_input_pares_soma_quantidade.py
#
# QUESTÃO 7 — FOR + INPUT + PARES + SOMA + CONTAGEM
#
# Crie um programa que peça ao usuário um número inteiro e positivo.
#
# Requisitos:
#
# - Crie uma variável chamada soma começando em 0.
# - Crie uma variável chamada quant começando em 0.
# - Solicite ao usuário um número inteiro e positivo.
# - Utilize for para percorrer os números de 1 até o número informado.
# - Utilize range() para controlar a sequência.
# - Utilize if para identificar os números pares.
# - Utilize o operador % para realizar essa verificação.
# - Mostre cada número par encontrado.
# - Some cada número par encontrado à variável soma.
# - Aumente a variável quant em 1 a cada número par encontrado.
# - Ao final, mostre a soma dos números pares.
# - Ao final, mostre a quantidade de números pares encontrados.
#
# Objetivo:
# - Combinar for, range(), input(), if, %, acumulador e contador.
# - Trabalhar simultaneamente com a soma e a quantidade de valores
#   que atendem a uma determinada condição.


