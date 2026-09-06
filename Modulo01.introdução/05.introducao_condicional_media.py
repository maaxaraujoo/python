


nota1 = int(input("Informe a primeira nota do aluno:"))
nota2 = int(input("Informe a segunda nota do aluno:"))

media = 0
media = (nota1 + nota2)/2

print(f"----A media do aluno e:{media}----")

if media >= 7:
    print("Aprovado")
elif media >= 5 and media<7:
    print("Recuperacao")
else:
    print("Reprovado")
# 05.introducao_condicional_media.py

# QUESTÃO 5
#
# Peça ao usuário para informar duas notas de um aluno.
#
# Calcule a média das duas notas e classifique o resultado:
# - média maior ou igual a 7: aprovado;
# - média maior ou igual a 5 e menor que 7: recuperação;
# - média menor que 5: reprovado.
#
# Mostre a média calculada e a situação do aluno.
#
# Utilize:
# - input()
# - int()
# - cálculo de média
# - if
# - elif
# - else
# - operadores de comparação
# - operador and
# - print()