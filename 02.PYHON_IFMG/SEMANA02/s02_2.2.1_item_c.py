print("-------------------CÁLCULO DE IMPOSTOS-------------------")
salario = float(input("Digite seu salário:"))

if salario <= 1903.98:
  print("Você está isento de imposto!")
# 7,5% a taxa
elif salario <= 2826.65:
  print(f"Opa, vai ter que pagar imposto de 7,5%! Seu salário ficou: {salario * 0.925}")
# 15% a taxa
elif salario <= 3751.05:
  print(f"Opa, vai ter que pagar imposto 15%! Seu salário ficou: {salario * 0.85}")
# 22,5% a taxa
elif salario <=4664.68:
  print(f"Opa, vai ter que pagar  22,5%! Seu salário ficou: {salario * 0.775}")
# 27,5% a taxa
else:
#salario > 4664.68
  print(f"Opa, vai ter que pagar imposto de 27,5%! Seu salário ficou: {salario * 0.725}") 
print("------------------------ FIM! ------------------------")
