lista = [2,4,50,32,20,21,22,24,19,1]
lista2 = []
quantidade = 0
for numero in lista:
    if numero > 20:
        quantidade = quantidade + 1
        lista2.append(numero)


print(f"Numeros encontrados maiores que 20:{quantidade}")
print(f"Os numeros são:{lista2}")
# 10.lista_for_if_contador_nova_lista.py
#
# QUESTÃO 10 — FILTRANDO, CONTANDO E ARMAZENANDO ELEMENTOS
#
# Crie uma lista contendo números inteiros.
#
# Requisitos:
#
# - Crie uma segunda lista vazia.
# - Crie uma variável para contar quantos números atendem à condição.
# - Utilize um for para percorrer diretamente os elementos da primeira lista.
# - Verifique quais números são maiores que 20.
# - Para cada número maior que 20:
#   - aumente o contador em 1;
#   - adicione o número à segunda lista utilizando append().
# - Ao final, mostre a quantidade de números encontrados.
# - Mostre a segunda lista contendo somente os números maiores que 20.
#
# Objetivo:
# - Combinar lista, for, if, contador e append().
# - Aprender a filtrar elementos de uma lista.
# - Aprender a armazenar os elementos filtrados em uma nova lista.
