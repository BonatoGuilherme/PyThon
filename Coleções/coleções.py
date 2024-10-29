lista = ["Maçã", "Uva", "Morango", "Abacate", "Graviola"]
tupla = "abc", 123.456
set = {"cadeira", "mesa", "armário"}
dicionario = {'SSD': 1000, 'CPU': 'AMD', 'RAM': '16gb'}

print(type(lista))
# <class 'list'>
print(type(tupla))
# <class 'tuple'>
print(type(set))
# <class 'set'>
print(type(dicionario))
# <class 'dict'>

# Função len
print(len(lista))
# 5
print(len(tupla))
# 2
print(len(set))
# 3
print(len(dicionario))
# 3

# Clausula in
print("Pera" in lista)
# False
print("abc" in tupla)
# True
print("monitor" in set)
# False
print("SSD" in dicionario)
# True

# Método count
print(lista.count("Uva"))
# 1
print(tupla.count(123))
# 0

#Interação com for
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
#Saida maçã, banana, laranja

#interação com a função "Enumerate()"
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

#Iteração com a função "zip()"
nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(f"Nome: {nome}, Idade: {idade}")