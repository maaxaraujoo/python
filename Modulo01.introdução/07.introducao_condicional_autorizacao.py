idade = int(input("Qual sua idade?"))
if idade >= 18 :
    print("Entrada Permitida")
elif idade == 16 or idade == 17:
    autori = str(input("Voce possui autorizacao?"))
    if autori == "Sim":
        print("ENTRA")
    else:
        print("NAO ENTRA")  
else:
    print("Entrada Negada")
# 07.introducao_condicional_autorizacao.py

# QUESTÃO 7
#
# Peça ao usuário para informar sua idade.
#
# Verifique as seguintes condições:
# - 18 anos ou mais: entrada permitida;
# - 16 ou 17 anos: pergunte se possui autorização;
#   - se tiver autorização: entrada permitida;
#   - caso contrário: entrada negada;
# - menor de 16 anos: entrada negada.
#
# Utilize:
# - input()
# - int()
# - str()
# - if
# - elif
# - else
# - operador or
# - operadores de comparação
# - condicionais aninhadas
# - print()