# 07.argumentos_nomeados.py

print("------------------------------------------IMPRESSÕES------------------------------------------")
def registrarPedido(cliente,produto,quanti):   
    print(f"Quantidade de produtos:{quanti}")
    print(f"Nome do cliente:{cliente}")
    print(f"Nome do produto:{produto}")
registrarPedido(cliente="Maxwell",produto="Videogame",quanti=4)
print("----------------------------------------------------------------------------------------------")
# QUESTÃO 07 — Argumentos nomeados
#
# Crie uma função chamada registrar_pedido().
#
# A função deve receber três parâmetros:
# cliente, produto e quantidade.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do cliente.
#
# 2. Pedir ao usuário o nome do produto.
#
# 3. Pedir ao usuário a quantidade desejada.
#
# 4. Chamar a função utilizando argumentos nomeados.
#
# 5. Na chamada da função, altere a ordem dos argumentos em
#    relação à ordem dos parâmetros.
#
# 6. Dentro da função, mostrar os três dados recebidos.
#
# OBJETIVO:
# Praticar argumentos nomeados e perceber como eles permitem
# enviar os valores aos parâmetros independentemente da ordem
# em que aparecem na chamada.