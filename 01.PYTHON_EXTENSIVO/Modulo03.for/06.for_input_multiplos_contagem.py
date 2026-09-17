quantidade = 0
numero = int(input("Digite um numero inteiro positivo:"))
print("-------------------------------------------")
print("Múltiplos de 3:")
for cont in range(1, numero + 1):
    if cont %3 == 0:
        quantidade = quantidade + 1
        print(cont)
print("-------------------------------------------")
print(f"Número digitado:{numero}")
print(f"Quantidade de Múltiplos de 3:{quantidade}")
print("-------------------------------------------")
# 06.for_input_multiplos_contagem.py
#
# QUESTÃO 6 — FOR + INPUT + MÚLTIPLOS + CONTAGEM
#
# Crie um programa que peça ao usuário um número inteiro e positivo.
#
# Requisitos:
#
# - Crie uma variável chamada quantidade começando em 0.
# - Solicite ao usuário um número inteiro e positivo.
# - Utilize for para percorrer os números de 1 até o número informado.
# - Utilize range() para controlar a sequência.
# - Utilize if para identificar os números múltiplos de 3.
# - Utilize o operador % para realizar essa verificação.
# - Mostre cada múltiplo de 3 encontrado.
# - A cada múltiplo encontrado, aumente a variável quantidade em 1.
# - Ao final, mostre a quantidade de múltiplos de 3 encontrados.
#
# Objetivo:
# - Combinar input(), for, range(), if, %, print() e acumulador.
# - Praticar simultaneamente a identificação e a contagem de valores
#   que atendem a uma determinada condição.
