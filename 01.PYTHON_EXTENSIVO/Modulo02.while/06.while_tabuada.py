tabuada = int(input("De qual numero voce quer saber a tabuada?"))

contador = 1
while 10>= contador:
    print(f"{contador} x {tabuada} = {contador*tabuada} ")
    contador = contador + 1 
# 06.while_tabuada.py
#
# QUESTÃO 6 — WHILE E TABUADA
#
# Crie um programa que solicite ao usuário um número inteiro e mostre
# a tabuada desse número de 1 até 10.
#
# O programa deve:
#
# 1. Solicitar um número inteiro ao usuário;
# 2. Criar uma variável chamada "contador" começando com o valor 1;
# 3. Utilizar while para repetir enquanto o contador for menor ou igual
#    a 10;
# 4. Realizar a multiplicação entre o número informado e o contador;
# 5. Mostrar cada operação da tabuada no formato:
#    contador x número = resultado;
# 6. Atualizar o contador a cada repetição;
# 7. Encerrar a repetição após mostrar a multiplicação por 10.
#
# Utilize:
# - input()
# - int()
# - variáveis
# - while
# - comparação
# - print()
# - multiplicação
# - operador de adição
#
# Objetivo:
# Praticar o while utilizando uma variável de controle e realizar uma
# operação matemática diferente a cada repetição.