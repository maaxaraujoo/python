print("---------------NÚMERO MAIOR---------------")
a = int(input("Digite o 1º número:"))
b = int(input("Digite o 2º número:"))
c = int(input("Digite o 3º número:"))

aux = a #10

if aux < b: # 10 < 5 - falso
  aux = b
if aux < c: # 15 < 20 - verdadeiro
  aux = c

print(f"O maior número entre os três é:{aux}")
print("------------------------------------------")


