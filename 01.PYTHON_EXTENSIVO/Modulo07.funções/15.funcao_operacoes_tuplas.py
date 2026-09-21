# 15.funcao_operacoes_tuplas.py
print("-------------------------PAPELARIA-------------------------")
#entrada de dados
produto_principal_user = str(input("Qual produto você deseja procurar?"))
produto_novo_user = str(input("Me diga um produto que você acha que não temos:"))
print("")
#fim da entrada de dados

#atribuições
produtos_principais = ("Lápis","Borracha","Apontador")
produtos_novos = ("Canetinha","Régua")
#fim das atribuições 

#interações
produtos_geral = produtos_principais + produtos_novos

print("-----------------SOBRE O PRODUTO QUE VOCÊ PROCURA-----------------")
verifica_principal = produto_principal_user in produtos_geral
if verifica_principal == True:
    print(f"Oba! Encontramos seu produto em nossa loja! {produto_principal_user} se encontra disponível em nossa papelaria.")
else:
    print(f"Não foi dessa vez! Mas em breve o(a) {produto_principal_user} chegará em nossa loja.")
print("")
print("-----------------SOBRE O PRODUTO QUE VOCÊ ACHA QUE NÃO TEMOS-----------------")
verifica_novo = produto_novo_user not in produtos_geral
if verifica_novo == True:
    print(f"É, realmente não temos {produto_novo_user} em nossa papelaria.")
else:
    print(f"Haha! Quase, por sorte chegou reposição ontem de {produto_novo_user} no estoque!")
print("")
print("-----------------INTERAÇÕES EXTRAS-----------------")
print(f"Produtos principais: {produtos_principais}")
print(f"Produtos novos: {produtos_novos}")
print(f"Todos os produtos: {produtos_geral}")
print(f"Produtos em destaque se repetindo: {produtos_principais[0]*3}")
print("")
print("-----------------FIM DO ATENDIMENTO-----------------")
# fim da etrutura de decisão


# QUESTÃO 15 — Operações com tuplas
#
# Crie duas tuplas relacionadas a uma loja.
#
# O programa deve:
#
# 1. Criar uma tupla chamada produtos_principais contendo
#    três nomes de produtos.
#
# 2. Criar uma tupla chamada produtos_novos contendo
#    dois nomes de produtos.
#
# 3. Criar uma nova tupla juntando as duas tuplas utilizando +.
#
# 4. Verificar se um produto informado pelo usuário existe
#    na nova tupla utilizando in.
#
# 5. Verificar se outro produto informado pelo usuário não
#    existe na nova tupla utilizando not in.
#
# 6. Criar uma tupla contendo uma informação de destaque
#    e utilizar * para repetir essa informação três vezes.
#
# 7. Mostrar os resultados das operações realizadas.
#
# OBJETIVO:
# Praticar as principais operações com tuplas: in, not in,
# concatenação com + e repetição com *.