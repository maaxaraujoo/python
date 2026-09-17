# 08.parametro_valor_padrao.py
print("------------------------------------------DIGITE AQUI------------------------------------------")
nome = str(input("Qual o seu nome?"))
print("------------------------------------------IMPRESSÕES------------------------------------------")
def configurar_perfil(nome, nivelUser = "iniciante"):
    print(f"Usuário:{nome} | Nível do usuário:{nivelUser}")
configurar_perfil(nome) #1 chamada, feita pela função
configurar_perfil("Adriano Paz", nivelUser = "Senior")
print("---------------------------------------------FIM-----------------------------------------------")
# QUESTÃO 08 — Parâmetro com valor padrão
#
# Crie uma função chamada configurar_perfil().
#
# A função deve receber dois parâmetros:
# usuario e nivel.
#
# O parâmetro nivel deve possuir um valor padrão.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do usuário.
#
# 2. Chamar a função informando apenas o usuário.
#
# 3. Fazer com que a função utilize o valor padrão de nivel.
#
# 4. Fazer uma segunda chamada informando o usuário e um nível
#    diferente do valor padrão.
#
# 5. Dentro da função, mostrar o usuário e o nível recebido.
#
# OBJETIVO:
# Praticar parâmetros com valor padrão e entender a diferença
# entre utilizar o valor definido na função e substituí-lo por
# um valor enviado durante a chamada.