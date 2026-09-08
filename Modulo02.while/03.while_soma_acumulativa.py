
numero = int(input("Digite o numero para nossa soma acumulativa:"))
soma = 0
contador = 1

while contador <= numero:
    print(contador)
    soma = contador + soma
    contador = contador + 1

print(f"Valor da soma: {soma}")
# 03.while_soma_acumulativa.py
#
# QUESTÃO 3 — WHILE E SOMA ACUMULATIVA
#
# Crie um programa que solicite um número inteiro ao usuário e calcule
# a soma de todos os números inteiros de 1 até o número informado.
#
# O programa deve:
#
# 1. Solicitar um número inteiro ao usuário;
# 2. Criar uma variável chamada "soma" começando com o valor 0;
# 3. Criar uma variável chamada "contador" começando com o valor 1;
# 4. Utilizar while para repetir enquanto o contador for menor ou igual
#    ao número informado;
# 5. Adicionar o valor atual do contador à variável "soma" a cada
#    repetição;
# 6. Fazer o contador avançar a cada repetição;
# 7. Mostrar o valor final da soma depois que o while terminar.
#
# Utilize:
# - input()
# - int()
# - variáveis
# - while
# - comparação
# - print()
# - operador de adição
#
# Objetivo:
# Praticar o while utilizando uma variável acumuladora e compreender
# como acumular valores durante as repetições.