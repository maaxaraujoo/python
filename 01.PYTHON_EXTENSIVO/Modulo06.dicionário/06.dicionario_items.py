# 23.funcao_dicionario_items.py
print("-----------------------FICHA CADASTRAL-----------------------")
agendamento = {}
agendamento['nome'] = str(input("Digite seu nome:"))
agendamento['especialidade'] = str(input("Qual especialidade você agendou?:"))
agendamento['hora'] = float(input("Digite a hora do seu atendimento:"))
print("-----------------------DADOS RECEBIDOS-----------------------")
for cont, valor in agendamento.items():
    print(cont, valor)


# QUESTÃO 23 — Percorrendo chave e valor com .items()
#
# Uma clínica possui informações sobre um agendamento.
#
# Crie um dicionário chamado agendamento contendo:
# paciente, especialidade e horario.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do paciente.
# 2. Pedir a especialidade desejada.
# 3. Pedir o horário do atendimento.
# 4. Armazenar as três informações no dicionário.
# 5. Utilizar .items() para percorrer o dicionário.
# 6. Mostrar a chave e o valor de cada informação.
#
# OBJETIVO:
# Praticar .items() e entender como percorrer simultaneamente
# as chaves e os valores de um dicionário.