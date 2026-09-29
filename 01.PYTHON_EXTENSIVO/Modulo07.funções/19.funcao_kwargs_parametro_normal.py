# 19.funcao_kwargs_parametro_normal.py

dicionario = {}
patrimonio = 5017
dicionario["modelo"] = str(input("Qual o modelo do computador?"))
dicionario["setor"] = str(input("Qual o setor do computador?"))
dicionario["problema"] = str(input("Qual o problema do computador?"))

def registrar_manutencao(patrimonio, **kwargs):
for cont, valor in kwargs.items():
print(f"'{patrimonio}  - {cont}:{valor}'")

registrar_manutencao(patrimonio, **dicionario)

# QUESTÃO 19 — Registro de equipamento para manutenção
#
# O setor de TI de uma empresa recebe equipamentos para manutenção.
# Cada equipamento possui obrigatoriamente um número de patrimônio.
# Além disso, o técnico pode receber outras informações sobre o
# equipamento, como modelo, setor de origem e problema apresentado.
#
# 1. Crie uma função chamada registrar_manutencao().
#
# 2. A função deve receber um parâmetro normal chamado patrimonio
#    e também informações adicionais usando **kwargs.
#
# 3. Mostre o número de patrimônio recebido.
#
# 4. Percorra as informações adicionais recebidas em **kwargs
#    utilizando .items().
#
# 5. Mostre cada chave e seu respectivo valor.
#
# 6. Faça uma chamada da função passando um número de patrimônio
#    e pelo menos 3 informações nomeadas adicionais.
#
# OBJETIVO:
# Praticar uma função que possui uma informação obrigatória
# específica e aceita informações adicionais através de **kwargs.


