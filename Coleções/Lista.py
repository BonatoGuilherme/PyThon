# Declaração de listas
numeros = [1, 2, 3, 4, 5]
frutas = ["Maçã", "Uva", "Morango", "Abacate", "Graviola"]
mista = [123, "Batata", 9.98] # Não façam isso!

# Imprimindo listas
print("Números:", numeros)
# Números: [1, 2, 3, 4, 5]
print("Frutas:", frutas)
# Frutas: ['Maçã', 'Uva', 'Morango', 'Abacate', 'Graviola']
print("Mista:", mista)
# Mista: [123, 'Batata', 9.98]

# Imprimindo posições das listas
print(numeros[0])
# 1
print(frutas[3])
# Abacate
print(mista[1])
# Batata

numeros.append(1)
print(numeros)
# [1, 2, 3, 4, 5, 1]

frutas.extend(["Laranja", "Cereja", "Amora"])
print(frutas)
# ['Maçã', 'Uva', 'Morango', 'Abacate', 'Graviola', 'Laranja', 'Cereja', 'Amora']

numeros.insert(0,0)
print(numeros)
# [0, 1, 2, 3, 4, 5, 1]

frutas.remove("Abacate")
print(frutas)
# ['Maçã', 'Uva', 'Morango', 'Graviola', 'Laranja', 'Cereja', 'Amora']

frutas.pop(3)
print(frutas)
# ['Maçã', 'Uva', 'Morango', 'Laranja', 'Cereja', 'Amora']

posicao = frutas.index("Uva")
print(posicao)
# 1

quantidade = numeros.count(1)
print(quantidade)
# 2

frutas.sort()
print(frutas)
# ['Amora', 'Cereja', 'Laranja', 'Maçã', 'Morango', 'Uva']
frutas.sort(reverse=True)
print(frutas)
# ['Uva', 'Morango', 'Maçã', 'Laranja', 'Cereja', 'Amora']

numeros.reverse()
print(numeros)
# [1, 5, 4, 3, 2, 1, 0]

nova_lista = numeros.copy()
print(nova_lista)
# [1, 5, 4, 3, 2, 1, 0]
