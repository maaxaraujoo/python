lista_inteiros = []
lista_pares = []
soma = 0
for cont in range (1, 9):
    entrada = int(input(f"Digite o {cont}º número inteiro:"))
    lista_inteiros.append(entrada)

    if entrada %2 == 0:
        lista_pares.append(entrada)
        soma = soma + entrada

print("---------------------------------------")
print(f"Lista de números cadastrados:{lista_inteiros}")
print(f"Lista de números cadastrados pares:{lista_pares}")
print(f"Soma dos numeros pares cadastrados:{soma}")
print(f"Quantidade de números pares cadastrados:{len(lista_pares)}")
print("---------------------------------------")# 11.lista_input_for_if_pares.py
# 11.lista_input_for_if_pares.py
# QUESTÃO 11 — CADASTRO, FILTRO, CONTAGEM E SOMA
#
# Crie um programa que permita cadastrar 8 números inteiros.
#
# Requisitos:
#
# - Crie uma lista para armazenar todos os números digitados.
# - Crie uma segunda lista para armazenar somente os números pares.
# - Utilize um for com range() para controlar as 8 entradas.
# - A cada entrada, adicione o número à primeira lista utilizando append().
# - Verifique se o número digitado é par utilizando %.
# - Se for par, adicione-o à segunda lista.
# - Calcule a soma dos números pares.
# - Ao final, mostre:
#   - a lista com todos os números cadastrados;
#   - a lista contendo somente os números pares;
#   - a soma dos números pares;
#   - a quantidade de números pares.
#
# Objetivo:
# - Integrar input, for, range(), listas, append(), if, %, len()
#   e acumulador em um único programa.