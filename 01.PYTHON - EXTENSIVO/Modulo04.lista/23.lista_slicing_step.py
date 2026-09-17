# 23.lista_slicing_step.py
lista = ["4","5","6","7","2","3","5","6"]
print(f"Lista original: {lista}")
print(f"Lista com slicing:{lista[::2]}")
# QUESTÃO 23 — SLICING COM STEP
#
# Crie uma lista contendo 8 números inteiros.
#
# Requisitos:
#
# - Mostre a lista completa.
# - Utilize slicing com step 2 para pegar os elementos
#   começando pelo primeiro elemento e avançando de 2 em 2.
# - Mostre o resultado.
#
# Objetivo:
# - Entender o terceiro parâmetro do slicing.
# - Praticar lista[inicio:fim:passo].
# - Entender como utilizar [::2].


# MÓDULO 4 — LISTAS
#
# BLOCO — SLICING COM STEP (PASSO)
#
# Já vimos:
#
# lista[inicio:fim]
#
# Agora podemos adicionar um terceiro valor:
#
# lista[inicio:fim:passo]
#
# O terceiro valor determina de quanto em quanto
# vamos avançar pelos elementos.
#
# Exemplo:
#
# lista = [10, 20, 30, 40, 50, 60]
#
# lista[0:6:2]
#
# Começa no índice 0.
# Para antes do índice 6.
# Avança de 2 em 2.
#
# Resultado:
# [10, 30, 50]
#
# Índices utilizados:
# 0 → 10
# 2 → 30
# 4 → 50
#
# ----------------------------------------------------------
#
# Outro exemplo:
#
# lista[1:6:2]
#
# Índices:
# 1 → 20
# 3 → 40
# 5 → 60
#
# Resultado:
# [20, 40, 60]
#
# ----------------------------------------------------------
#
# Também podemos utilizar step sem informar início e fim:
#
# lista[::2]
#
# Isso significa:
# - começar do início;
# - ir até o final;
# - avançar de 2 em 2.
#
# Exemplo:
#
# lista[::2]
# → [10, 30, 50]
#
# ----------------------------------------------------------
#
# IMPORTANTE:
#
# lista[inicio:fim:passo]
#
# inicio → onde começa
# fim    → onde para (não inclui)
# passo  → de quanto em quanto avança