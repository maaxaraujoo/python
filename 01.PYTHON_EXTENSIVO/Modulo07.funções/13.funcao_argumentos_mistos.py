# 13.funcao_argumentos_mistos.py
alunoNome = str(input("Digite seu nome:"))
cursoAluno = str(input("Qual seu curso?"))
semestre = int(input("Qual seu semestre?(Digite o número)"))

def ficha_aluno(alunoNome, cursoAluno, semestreAlnuo):
    print(f"Nome digitado:{alunoNome}")
    print(f"Curso digitado:{cursoAluno}")
    print(f"Semestre encontrado:{semestreAlnuo}")

ficha_aluno(alunoNome, cursoAluno, semestreAlnuo = semestre)
# QUESTÃO 13 — Argumentos posicionais e nomeados
#
# Crie uma função chamada ficha_aluno().
#
# A função deve receber três parâmetros, nesta ordem:
# nome, curso e semestre.
#
# O programa deve:
#
# 1. Pedir ao usuário o nome do aluno.
#
# 2. Pedir ao usuário o curso do aluno.
#
# 3. Pedir ao usuário o semestre atual.
#
# 4. Chamar a função utilizando uma combinação de argumentos
#    posicionais e nomeados.
#
# 5. Os argumentos posicionais devem aparecer primeiro na chamada.
#
# 6. Pelo menos um dos argumentos deve ser enviado utilizando
#    o nome do parâmetro.
#
# 7. Dentro da função, mostrar os três dados recebidos.
#
# OBJETIVO:
# Praticar a utilização de argumentos posicionais e nomeados
# na mesma chamada, respeitando a ordem exigida pelo Python.