# 15.string_immutabilidade.py
palavra = "Python"
print("----------------Impressões----------------")
print(f"Palavra completa:{palavra}")
palavranova = palavra.replace("P", "J")
print(f"Palavra alterada:{palavranova}")
print(f"Lembrando que essa é a nossa original:{palavra}")
print("------------------------------------------")
# QUESTÃO 15 — Entendendo a imutabilidade das Strings
#
# Crie uma variável chamada palavra contendo exatamente:
#
# "Python"
#
# O programa deve:
#
# 1. Mostrar a palavra original.
#
# 2. Criar uma nova variável utilizando replace() para trocar
#    a letra "P" pela letra "J".
#
# 3. Mostrar a nova string criada.
#
# 4. Mostrar novamente a string original.
#
# 5. Observar que a string original continua inalterada.
#
# OBJETIVO:
# Praticar a imutabilidade das strings e entender que,
# ao utilizar replace(), uma nova string é criada enquanto
# a string original permanece inalterada.