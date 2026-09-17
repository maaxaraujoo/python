
frasenova = "Eu venho todos os dias para a faculdade."

esta = frasenova.startswith("Eu")
print(f"Status da palavra 'Eu':{esta} ")

naoesta = frasenova.endswith(".")
print(f"Status da palavra '.':{naoesta} ")

# 11.string_startswith_endswith.py
#
# QUESTÃO 11 — Verificando o início e o final de uma string
#
# Crie uma variável chamada frase contendo uma frase.
#
# O programa deve:
#
# 1. Mostrar a frase original.
#
# 2. Utilizar startswith() para verificar se a frase começa
#    com uma determinada palavra.
#
# 3. Mostrar o resultado dessa verificação.
#
# 4. Utilizar endswith() para verificar se a frase termina
#    com determinado caractere ou trecho de texto.
#
# 5. Mostrar o resultado dessa verificação.
#
# OBJETIVO:
# Praticar startswith() e endswith() para verificar,
# respectivamente, como uma string começa e como ela termina.