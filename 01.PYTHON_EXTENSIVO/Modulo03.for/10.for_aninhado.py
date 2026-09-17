# 10.for_aninhado.py
for externo in range(1,4):
    print(f"-----Externo:{externo}")
    for interno in range(1,4):
        print(f"Interno:{interno}")
# QUESTÃO 10 — FOR ANINHADO
#
# Crie um programa que utilize dois for, sendo um dentro do outro.
#
# Requisitos:
#
# - Utilize um for externo para percorrer os números de 1 até 3.
# - Dentro do for externo, utilize um segundo for para percorrer
#   os números de 1 até 3.
# - Mostre os valores do for externo e do for interno a cada
#   repetição.
# - Observe que, para cada valor do for externo, o for interno
#   deve percorrer toda a sua sequência.
#
# Objetivo:
# - Aprender o funcionamento de um for dentro de outro for.
# - Entender a relação entre o laço externo e o laço interno.
# - Compreender que o for interno é executado completamente
#   a cada repetição do for externo.