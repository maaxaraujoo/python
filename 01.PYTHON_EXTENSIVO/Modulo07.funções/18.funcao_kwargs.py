# 18.funcao_kwargs.py
dicionario = {}

dicionario["nome"] = str(input("Digite seu nome:"))
dicionario["idade"] = int(input("Digite sua idade:"))
dicionario["cargo"] = str(input("Digite seu cargo:"))

def cadastrar_atendimento(**kwargs):
    for cont, valor in kwargs.items():
        print(f"'{cont}': {valor}")

cadastrar_atendimento(**dicionario)
    
    


    
# QUESTÃO 18 — Cadastro de atendimento
#
# Uma empresa precisa registrar informações de um atendimento.
#
# 1. Crie uma função chamada cadastrar_atendimento() que receba
#    uma quantidade variável de argumentos nomeados usando **kwargs.
#
# 2. Dentro da função, percorra os dados recebidos.
#
# 3. Mostre cada chave e seu respectivo valor.
#
# 4. Faça uma chamada da função passando pelo menos 4 informações
#    nomeadas diferentes.
#
# OBJETIVO:
# Praticar **kwargs e entender que os argumentos nomeados recebidos
# pela função ficam armazenados em um dicionário.
