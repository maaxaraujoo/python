cont = 1
quant = 0

numero = int(input("Digite um numero inteiro e positivo:"))

while cont <= numero :
    if cont % 3 == 0:
        quant = quant + 1
    cont = cont + 1
print("-----------------------------------------------------")
print(f"Numero digitado:{numero}")
print(f"A quantidade de numeros multiplos de 3, de 1 até {numero} são: {quant}")
print("-----------------------------------------------------")
# 05.while_contagem_multiplos.py
#
# QUESTÃO 5 — WHILE E CONTAGEM DE MÚLTIPLOS
#
# Crie um programa que solicite ao usuário um número inteiro positivo
# e conte quantos números múltiplos de 3 existem entre 1 e o número
# informado.
#
# O programa deve:
#
# 1. Solicitar um número inteiro positivo ao usuário;
# 2. Criar uma variável de controle começando em 1;
# 3. Criar uma variável chamada "quant" começando em 0;
# 4. Utilizar while para percorrer os números de 1 até o número
#    informado;
# 5. Verificar quais números são múltiplos de 3 utilizando o operador %;
# 6. A cada múltiplo de 3 encontrado, aumentar a variável "quant" em 1;
# 7. Atualizar o contador a cada repetição;
# 8. Mostrar a quantidade total de múltiplos de 3 encontrados.
#
# Utilize:
# - input()
# - int()
# - variáveis
# - while
# - if
# - operador %
# - comparação
# - operador de adição
# - print()
#
# Objetivo:
# Praticar o while combinado com if e o operador %, utilizando uma
# variável acumuladora para contar quantas vezes uma condição é atendida.