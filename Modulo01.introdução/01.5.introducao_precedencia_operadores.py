# 01.5.introducao_precedencia_operadores.py

# QUESTÃO 1.5 — PRECEDÊNCIA DE OPERADORES
#
# Crie um programa que demonstre a pr1cedência de operadores em Python.
#
# O programa deve:
#
# 1. Criar uma variável chamada "resultado1" contendo uma expressão
#    que misture soma e multiplicação;
resultado1 = 2 + 2 + 1 * 10
# 2. Criar uma variável chamada "resultado2" contendo uma expressão
#    com parênteses, soma e multiplicação;
resultado2 = 1 * 2 * (1 + 2)
# 3. Mostrar os dois resultados;
print(f"Resultado 1:{resultado1}")
print(f"Resultado 2:{resultado2}")
# 4. Criar uma variável chamada "idade" com um valor numérico;
idade = 10
# 5. Criar uma variável chamada "resultado3" contendo uma expressão
#    que misture duas comparações com o operador "and";
resultado3 = (idade)>=18 and 20 < 10

# 6. Mostrar o resultado de "resultado3";
print(f"Resultado 3:{resultado3}")
# 7. Criar uma variável chamada "resultado4" contendo uma expressão
#    que utilize "or" e "and" na mesma expressão;
resultado4 = 10 > 3 or 10 > 11 and 20>2

# 8. Mostrar o resultado de "resultado4";
print(f"Resultado 4:{resultado4}")
# Atenção:
# - Observe a ordem de execução dos operadores;
# - Utilize parênteses em uma das expressões para alterar a ordem
#   de execução;
# - Não utilize if/elif/else nesta questão;
#
# Utilize:
# - variáveis
# - =
# - + 
# - *
# - ()
# - comparações
# - and
# - or
# - print()
#
# Objetivo:
# Entender como o Python determina a ordem de execução dos operadores
# quando diferentes tipos de operadores aparecem na mesma expressão.