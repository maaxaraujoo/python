# 04.funcao_return.py
def compraloja(quant, precouni):
      multi = quant * precouni
      return multi
total = compraloja(4,27.50)
print(f"Total da compra:{total}")

# QUESTÃO 04 — Função com retorno de valor
# Uma loja precisa calcular o valor total de uma compra.
#
# Crie uma função chamada calcular_total().
#
# A função deve receber dois parâmetros:
# quantidade e preco.
#
# O programa deve:
#
# 1. Multiplicar a quantidade pelo preço dentro da função.
#
# 2. Utilizar return para devolver o valor total.
#
# 3. Fora da função, armazenar o valor retornado em uma variável
#    chamada total.
#
# 4. Mostrar na tela o valor armazenado em total.
#
# 5. Testar a função utilizando:
#    quantidade = 4
#    preco = 27.50
#
# OBJETIVO:
# Praticar o uso de return para devolver um valor calculado
# por uma função e utilizar esse valor fora dela.
