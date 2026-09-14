primeira_frase = "A vida é bela"

print(f"-----------------------------------------")
print(f"Frase sem modificação: {primeira_frase}")
print(f"-----------------------------------------")
nova_frase = primeira_frase.replace("bela", "longa")
print(f"Frase sem modificação: {nova_frase}")
print(f"-----------------------------------------")
print(f"Frase sem modificação: {primeira_frase}")
print(f"-----------------------------------------")
# 05.string_replace.py
#
# QUESTÃO 05 — Substituindo partes de uma string com replace()
#
# Crie uma variável contendo uma frase.
#
# O programa deve:
#
# 1. Mostrar a frase original.
#
# 2. Escolher uma palavra presente na frase para ser substituída.
#
# 3. Utilizar replace() para substituir essa palavra por outra.
#
# 4. Armazenar o resultado em uma nova variável.
#
# 5. Mostrar a frase depois da substituição.
#
# 6. Mostrar novamente a frase original para verificar que ela
#    não foi modificada.
#
# OBJETIVO:
# Praticar replace() e entender que ele retorna uma nova string,
# mantendo a string original sem alteração.
