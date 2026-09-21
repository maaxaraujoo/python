# 20.funcao_dicionario_alteracao.py
reserva = {}
reserva['cidade'] = str(input("Digite a cidade que pretende se hospedar:"))
reserva['quarto'] = str(input("Digite seu tipo de quarto:"))
reserva['q_noites'] = int(input("Digite quantas noites quer passar:"))
reserva['cidade'] = str(input("Tivemos um conflito na última cidade que você escolheu, por favor digite uma nova cidade::"))



print(f"Cidade escolhida:{reserva['cidade']}")
print(f"Tipo do quarto:{reserva['quarto']}")
print(f"Noites escolhidas:{reserva['q_noites']}")

# QUESTÃO 20 — Alterando informações de uma reserva
#
# Um sistema de reservas de um hotel possui informações sobre
# uma hospedagem. O hóspede decidiu alterar a cidade da reserva.
#
# Crie um dicionário chamado reserva contendo inicialmente:
# cidade, quarto e noites.
#
# O programa deve:
#
# 1. Receber do usuário a cidade da reserva.
# 2. Receber o tipo do quarto.
# 3. Receber a quantidade de noites.
# 4. Armazenar essas informações no dicionário.
# 5. Perguntar ao usuário qual será a nova cidade da reserva.
# 6. Alterar o valor da chave "cidade" utilizando a nova cidade.
# 7. Mostrar o dicionário atualizado.
#
# OBJETIVO:
# Praticar a alteração do valor de uma chave que já existe
# em um dicionário.
