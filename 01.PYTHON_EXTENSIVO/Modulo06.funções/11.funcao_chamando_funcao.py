# 11.funcao_chamando_funcao.py
nomeProduto = str(input("Qual produto você procura?"))
def verificar_estoque(nomeProduto):
    print("Estoque sendo verificado...")

def iniciar_venda(nomeProduto):
    verificar_estoque(nomeProduto)
    print("Verificamos o estoque!A venda pode ser iniciada.")
iniciar_venda(nomeProduto)
# QUESTÃO 11 — Uma função chamando outra função
#
# Crie duas funções:
#
# 1. Uma função chamada verificar_estoque().
#    Ela deve mostrar uma mensagem informando que o estoque
#    está sendo verificado.
#
# 2. Uma função chamada iniciar_venda().
#    Dentro dela, chame a função verificar_estoque().
#    Depois que a verificação for realizada, mostre uma mensagem
#    informando que a venda pode ser iniciada.
#
# O programa deve:
#
# 3. Pedir ao usuário o nome de um produto.
#
# 4. Fazer a função verificar_estoque() receber o nome do produto.
#
# 5. Fazer a função iniciar_venda() receber o mesmo nome do produto
#    e utilizá-lo ao chamar verificar_estoque().
#
# 6. Chamar apenas a função iniciar_venda() no programa principal.
#
# OBJETIVO:
# Praticar uma função chamando outra função e entender como
# informações podem ser passadas entre essas funções.