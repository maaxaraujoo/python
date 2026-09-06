idadepessoa = int(input("Qual a sua idade?"))

if idadepessoa < 12 :
    print("Idade de uma criança")
elif idadepessoa >= 12 and idadepessoa <= 17 :
    print("Idade de um adolescente")
else :
    print("Idade de um adulto")
# 04.introducao_condicional_elif.py

# QUESTÃO 4
#
# Peça ao usuário para informar sua idade.
#
# Classifique a pessoa de acordo com a idade:
# - menor de 12 anos: criança;
# - de 12 a 17 anos: adolescente;
# - 18 anos ou mais: adulto.
#
# Utilize:
# - input()
# - int()
# - if
# - elif
# - else
# - operadores de comparação
# - operador and
# - print()