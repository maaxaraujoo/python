# 12.funcao_retorno_entre_funcoes.py

valor_produto = float(input("Qual o valor da sua compra?"))

#função 01
def obter_desconto():
    calculo_desconto = valor_produto * 0.1
    return calculo_desconto

#função 02
def calcular_pagamento():
    valor_de_obter_desconto = obter_desconto()
    valor_final = valor_produto - valor_de_obter_desconto
    return valor_final
print(f"Valor que você vai pagar:{calcular_pagamento()}")

# QUESTÃO 12 — Retorno entre funções
#
# Crie duas funções:
#
# 1. Uma função chamada obter_desconto().
#    Ela deve receber o valor de uma compra e retornar o valor
#    correspondente a 10% desse valor.
#
# 2. Uma função chamada calcular_pagamento().
#    Ela deve receber o valor da compra.
#
# O programa deve:
#
# 3. Pedir ao usuário o valor de uma compra.
#
# 4. Fazer calcular_pagamento() chamar obter_desconto().
#
# 5. Armazenar dentro de calcular_pagamento() o valor retornado
#    por obter_desconto().
#
# 6. Calcular o valor final da compra após o desconto.
#
# 7. Retornar o valor final através de calcular_pagamento().
#
# 8. No programa principal, armazenar o retorno em uma variável
#    chamada valor_final.
#
# 9. Mostrar o valor final na tela.
#
# OBJETIVO:
# Praticar uma função chamando outra função, recebendo o valor
# retornado por ela e utilizando esse valor em um novo cálculo.