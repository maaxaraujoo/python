print("---------------------------------------------------------------------")
list_frutas =["Maça","Uva","Melancia","Laranja","Limão","Mamão","Morango"]
print(f"Lista original:{list_frutas}")
print("---------------------------------------------------------------------")
para_remover = "Melancia" #temos que epecificar onde a fruta removida vai ficar
fruta_remov = list_frutas.remove(para_remover) #fruta_remov recebe None
print(f"Fruta removida:{para_remover}")
print(f"Lista alterada:{list_frutas}")
print("---------------------------------------------------------------------")
# 14.lista_remove.py
#
# QUESTÃO 14 — REMOVENDO ELEMENTOS COM remove()
#
# Crie uma lista contendo 7 frutas.
#
# Requisitos:
#
# - Mostre a lista original.
# - Escolha uma fruta que será removida.
# - Utilize remove() para remover essa fruta pelo seu valor.
# - Mostre qual fruta foi removida.
# - Mostre a lista novamente após a remoção.
#
# Objetivo:
# - Aprender a utilizar remove().
# - Entender que remove() procura e remove um elemento pelo seu valor.
# - Diferenciar remove() de pop(), que trabalha com índices.
