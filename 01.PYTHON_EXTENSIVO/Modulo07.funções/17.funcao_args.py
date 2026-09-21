# 17.funcao_args.py
print("----------------------INFORMAÇÕES DE USUÁRIOS----------------------")

lista_nomes = []
for cont in range(1,5):
  nome_user = str(input(f"DIgite o {cont}º nome:"))
  lista_nomes.append(nome_user)
print("")
print("----------------------NOMES EM ARGS----------------------")
def registrar_participantes(*args):
  for cont in args:
    print(cont)
    
registrar_participantes(*lista_nomes)
print("----------------------FIM----------------------")

# QUESTÃO 17 — Função com quantidade variável de argumentos
#
# Uma empresa quer registrar os nomes dos participantes de uma
# reunião. A quantidade de participantes pode variar.
#
# Crie uma função chamada registrar_participantes() utilizando
# *args.
#
# O programa deve:
#
# 1. Fazer a função receber uma quantidade variável de nomes.
#
# 2. Dentro da função, percorrer os valores recebidos utilizando
#    um for.
#
# 3. Mostrar cada participante separadamente.
#
# 4. Chamar a função passando pelo menos 4 participantes.
#
# 5. Não criar parâmetros individuais para cada participante.
#
# OBJETIVO:
# Praticar *args e entender que os argumentos posicionais recebidos
# pela função são armazenados em uma tupla.
