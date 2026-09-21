# 22.funcao_dicionario_values.py
viagem = {}
viagem['destino'] = str(input("Pra onde você quer viajar?"))
viagem['km'] = float(input("Quantos Km são?"))
viagem['cat'] = str(input("Qual a categoria da viagem?"))

for cont in viagem.values():
    print(cont)
# QUESTÃO 22 — Percorrendo os valores de um dicionário
#
# Um aplicativo de transporte precisa analisar os dados de uma
# viagem realizada por um motorista.
#
# Crie um dicionário chamado viagem contendo:
# destino, distancia e categoria.
#
# O programa deve:
#
# 1. Pedir ao usuário o destino da viagem.
# 2. Pedir a distância percorrida em quilômetros.
# 3. Pedir a categoria da viagem.
# 4. Armazenar as três informações no dicionário.
# 5. Utilizar .values() para percorrer os valores do dicionário.
# 6. Mostrar cada valor separadamente.
#
# OBJETIVO:
# Praticar o uso de .values() para percorrer diretamente os
# valores armazenados em um dicionário.