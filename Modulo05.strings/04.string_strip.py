nome = "    Maxwell     "

print(f"---------------------------------------------")
print(f"Nome dentro da variável:{nome}")
print(f"Quantidade de caracteres dentro da variável: {len(nome)}")
print(f"---------------------------------------------")
print(f"Nome dentro da variável com strip:{nome.strip()}")
print(f"Quantidade de caracteres dentro da variável depois do strip: {len(nome.strip())}")
print(f"---------------------------------------------")
# 04.string_strip.py
#
# QUESTÃO 04 — Removendo espaços desnecessários com strip()
#
# Crie uma variável chamada nome contendo um nome com
# espaços antes e depois do texto.
#
# Exemplo de situação:
#
# "   Maxwell   "
#
# O programa deve:
#
# 1. Mostrar o nome exatamente como foi armazenado.
#
# 2. Mostrar a quantidade de caracteres da string original
#    utilizando len().
#
# 3. Utilizar strip() para remover os espaços do início
#    e do final.
#
# 4. Mostrar o nome depois do strip().
#
# 5. Mostrar novamente a quantidade de caracteres depois
#    do strip().
#
# OBJETIVO:
# Praticar strip() e perceber, através do len(), a diferença
# entre a string original e a string sem os espaços externos.