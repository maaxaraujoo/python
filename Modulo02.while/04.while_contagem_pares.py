numeroPar = int(input("Digite um numero inteiro positivo:"))

cont = 1
quantidade = 0
while cont <= numeroPar:
    if cont % 2 == 0: #se for positivo
        quantidade = quantidade + 1 #aqui conta +1
    cont = cont + 1 #esse contador é o nosso rotativo, para o while funcionar

print(f"A quantidade de numeros pares é {quantidade}")
# 04.while_contagem_pares.py
#
# QUESTÃO 4 — WHILE E CONTAGEM DE NÚMEROS PARES
#
# Crie um programa que solicite ao usuário um número inteiro positivo
# e conte quantos números pares existem entre 1 e o número informado.
#
# O programa deve:
#
# 1. Solicitar um número inteiro positivo ao usuário;
# 2. Criar uma variável de controle começando em 1;
# 3. Criar uma variável chamada "quantidade" começando em 0;
# 4. Utilizar while para percorrer os números de 1 até o número
#    informado;
# 5. Verificar quais números são pares utilizando o operador %;
# 6. A cada número par encontrado, aumentar a variável "quantidade"
#    em 1;
# 7. Atualizar