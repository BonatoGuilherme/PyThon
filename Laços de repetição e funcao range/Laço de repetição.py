'''
for: usado quando sabemos o número de iterações.
while: usado quando nãosabemos o número de iterações, mas temos uma condição.
'''
for i in range(1,7):
 if i%2 == 0:
  print(f"{i} é par")
 else:
  print(f"{i} é impar")

soma = 0
numero = 1
limite = 10
while numero <= limite:
 soma += numero
 numero += 1
print(f"A soma de 1 até {limite}:", soma)
