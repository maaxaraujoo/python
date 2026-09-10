# 26.lista_copia_referencia.py
lista_a =  [1,2,3]
lista_b =  [4,5,6]
print("--------------------------------------")
print(f"Lista A antes da cópia:{lista_a}")
print(f"Lista B antes da cópia:{lista_b}")
print("--------------------------------------")
#lista_b = lista_a.copy()
lista_a = lista_b.copy()

print(f"Lista B com a cópia de A:{lista_a}")


# QUESTÃO 26 — REFERÊNCIA E CÓPIA DE LISTAS
#
# Crie uma lista chamada lista_a contendo alguns números.
#
# Requisitos:
#
# - Crie uma segunda variável chamada lista_b recebendo lista_a
#   diretamente.
# - Altere um elemento através de lista_b.
# - Mostre lista_a e lista_b e observe o resultado.
#
# Depois:
#
# - Crie uma terceira variável chamada lista_c utilizando
#   lista_a.copy().
# - Altere um elemento através de lista_c.
# - Mostre lista_a e lista_c.
#
# Objetivo:
# - Entender a diferença entre referência e cópia.
# - Perceber na prática que lista_b = lista_a aponta para
#   a mesma lista.
# - Entender que lista_a.copy() cria uma lista independente.