# 33.lista_matriz.py

matriz = [
     [10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
 ]

print(f"Matriz completa:{matriz}")
print(f"Número:{matriz[1][1]}") #50
print(f"Número:{matriz[2][2]}") #90

#alterando o número 20 para 200;
matriz[0][1] = 200
print(f"Matriz com alteração:{matriz}")

# QUESTÃO 33 — Criando e manipulando uma matriz
#
# Crie a seguinte matriz:
#
# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
#
# Faça o programa:
#
# 1. Mostre a matriz completa.
#
# 2. Mostre o número 50 acessando-o diretamente
#    pelos índices.
#
# 3. Mostre o número 90 acessando-o diretamente
#    pelos índices.
#
# 4. Altere o número 20 para 200 usando seus índices.
#
# 5. Mostre a matriz novamente depois da alteração.
#
# OBJETIVO:
# Praticar listas dentro de listas, índices de matriz
# e alteração de elementos.