# 09.funcao_com_ou_sem_return.py
nome_usuario = str(input("Digite seu nome:"))
print("-----------------------------------SEM RETURN-----------------------------------")
def mostrar_status(nome_usuario):
    print(f"Seja bem-vindo(a) {nome_usuario}! É uma honra ter você conosco.")
mostrar_status(nome_usuario)
print("-----------------------------------COM RETURN-----------------------------------")
def gerar_status(nome_usuario):
    saudacao = nome_usuario
    return saudacao

mensagem = gerar_status(nome_usuario)
print(f"Boas vindas {mensagem}")
print("-----------------------------------FINISH-----------------------------------")

# QUESTÃO 09 — Função com e sem retorno
#
# Crie duas funções:
#
# 1. Uma função chamada mostrar_status().
#    Ela deve receber o nome de uma pessoa e mostrar uma
#    mensagem informando que o cadastro foi realizado.
#
# 2. Uma função chamada gerar_status().
#    Ela deve receber o nome de uma pessoa e devolver,
#    através de return, uma mensagem de status.
#
# O programa deve:
#
# 3. Pedir ao usuário o nome de uma pessoa.
#
# 4. Chamar mostrar_status() utilizando o nome informado.
#
# 5. Chamar gerar_status() utilizando o mesmo nome e armazenar
#    o valor retornado em uma variável.
#
# 6. Mostrar na tela o valor armazenado nessa variável.
#
# OBJETIVO:
# Praticar a diferença entre uma função que apenas executa
# uma ação e uma função que devolve um valor através de return.