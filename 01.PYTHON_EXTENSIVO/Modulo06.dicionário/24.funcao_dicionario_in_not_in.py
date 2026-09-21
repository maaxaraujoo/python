# 24.funcao_dicionario_in_not_in.py
print("-----------------------FICHA CADASTRAL-----------------------")
chamado = {}
chamado['nome'] = input("Digite seu nome:")
chamado['assunto'] = input("Qual assunto você quer tratar?")
chamado['prioridade'] = input("Qual sua prioridade?")
verifica_chave = input("Me diga um nome de uma chave que deseja verificar:")
verifica_chave_not = input("Me diga um nome de uma chave que não está no nosso dicionário:")
print(f"--------VERIFICANDO SE A CHAVE {verifica_chave} ESTÁ AQUI!--------")
if verifica_chave in chamado:
    print("Essa chave está aqui!")
else:
    print("Não está aqui!")
print(f"------VERIFICANDO SE A CHAVE {verifica_chave_not} NÃO ESTÁ AQUI!------")
if verifica_chave_not  not in chamado:
    print("Realmente, não está aqui.")
else:
    print("Essa chave se encontra aqui!")



# QUESTÃO 24 — Verificando a existência de chaves
#
# Um sistema de atendimento possui informações básicas de um
# chamado aberto por um cliente.
#
# Crie um dicionário chamado chamado contendo:
# cliente, assunto e prioridade.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do cliente.
# 2. Pedir o assunto do chamado.
# 3. Pedir a prioridade.
# 4. Armazenar as três informações no dicionário.
# 5. Perguntar ao usuário o nome de uma chave que deseja verificar.
# 6. Utilizar in para verificar se essa chave existe no dicionário.
# 7. Utilizar not in para verificar se uma chave diferente não existe.
# 8. Mostrar na tela o resultado das duas verificações.
#
# OBJETIVO:
# Praticar in e not in para verificar a existência de chaves
# em um dicionário.