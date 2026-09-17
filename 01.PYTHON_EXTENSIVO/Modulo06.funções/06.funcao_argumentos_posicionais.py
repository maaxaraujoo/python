# 06.argumentos_posicionais.py
print("-----------DIGITE----------")
prod = str(input("Nome do produto:"))
quant = int(input("Quantidade desse produto:"))
prec = float(input("Valor do produto:"))
def cadatrar_produto(prod, quant, prec):
    print(f"Nome do produto:{prod}")
    print(f"Quantidade do produto:{quant}")
    print(f"Preço do produto:{prec}")
cadatrar_produto(prod, quant, prec)
# QUESTÃO 06 — Argumentos posicionais
#
# Crie uma função chamada cadastrar_produto().
#
# A função deve receber três parâmetros, nesta ordem:
# produto, quantidade e preco.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do produto.
#
# 2. Pedir ao usuário a quantidade disponível.
#
# 3. Pedir ao usuário o preço do produto.
#
# 4. Chamar a função passando os três valores na ordem
#    correta dos parâmetros.
#
# 5. Dentro da função, mostrar:
#    - nome do produto
#    - quantidade disponível
#    - preço do produto
#
# OBJETIVO:
# Praticar argumentos posicionais, entendendo que cada valor
# enviado na chamada da função é associado ao parâmetro de
# acordo com sua posição.