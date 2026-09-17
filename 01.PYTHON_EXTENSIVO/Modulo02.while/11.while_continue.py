# 11.while_continue.py
cont = 1
while cont <=10:
    if cont %2 == 0:
        cont += 1 
        continue
    else:
        print(cont)
        cont += 1 
        
    
        
        
    
       

# QUESTÃO 11 — CONTINUE
#
# Crie um programa que percorra os números de 1 até 10
# utilizando while.
#
# Requisitos:
#
# - Crie uma variável de controle chamada contador começando em 1.
# - Utilize while para percorrer os números de 1 até 10.
# - Utilize if para identificar os números pares.
# - Quando encontrar um número par, utilize continue para
#   pular o restante daquela repetição.
# - Os números ímpares devem ser mostrados na tela.
# - A variável de controle deve continuar sendo atualizada
#   corretamente para que o while termine.
#
# Objetivo:
# - Aprender a utilizar continue para pular uma repetição
#   específica sem encerrar o while.
# - Entender a diferença entre continue e break.