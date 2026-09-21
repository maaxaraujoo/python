# 10.escopo_variavel_local.py
nome = str(input("Qual o nome do seu produto?"))
def exibir_produto():
    produto = nome
    print(f"Nome:{produto}")
exibir_produto()
#(Não imprime poque - produto - está dentro da função) print(f"Nome:{produto}")

# QUESTÃO 10 — Escopo de variáveis
#
# Crie uma função chamada exibir_produto().
#
# O programa deve:
#
# 1. Pedir ao usuário o nome de um produto.
#
# 2. Criar uma variável chamada produto dentro da função,
#    utilizando o nome recebido como valor.
#
# 3. Dentro da função, mostrar o valor de produto.
#
# 4. Depois da chamada da função, tente mostrar produto fora
#    da função.
#
# 5. Observe o que acontece ao executar o programa.
#
# OBJETIVO:
# Praticar o conceito de variável local e perceber em qual
# escopo uma variável criada dentro de uma função pode ser
# acessada.