# 05.funcao_calculo.py
print("-----------------------------CÁLCULO DE VALOR-----------------------------")
quantidade = int(input("Qual a quantidade de produtos existentes?"))
valor_produto = int(input("Quanto deu o valor dos produtos?"))
#print("----------------------FUNÇÃO----------------------")
def caulcular_valor(quantidade, valor_produto):
    totaldacompra = quantidade * valor_produto
    return totaldacompra
#print("----------------------FUNÇÃO----------------------")
totaldacompra = caulcular_valor(quantidade,valor_produto)
print(f"Total da compra:{totaldacompra}")
print("--------------------------------------------------------------------------")

# QUESTÃO 05 — Função com retorno
#
# Crie uma função chamada calcular_valor().
#
# A função deve receber dois parâmetros:
# quantidade e preco.
#
# O programa deve:
#
# 1. Pedir ao usuário a quantidade de produtos.
#
# 2. Pedir ao usuário o preço de cada produto.
#
# 3. Enviar esses dois valores para a função.
#
# 4. Dentro da função, calcular o valor total da compra.
#
# 5. Utilizar return para devolver o valor calculado.
#
# 6. Armazenar o valor retornado em uma variável chamada total.
#
# 7. Mostrar na tela o valor armazenado em total.
#
# OBJETIVO:
# Praticar o uso de return para devolver um valor calculado
# por uma função, utilizando dados fornecidos pelo usuário.