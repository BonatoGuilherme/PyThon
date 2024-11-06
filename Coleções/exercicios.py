#Primeira
numeros = []

for i in range(10):
    num = float(input("Digite um número: "))
    numeros.append(num)

numeros.reverse()
print(numeros)

#Segunda
nro = []
for i in range(5):
    num = int(input("Digite um numero: "))
    nro.append(num)
soma = 0
multi=1
for i in range(5):
    soma = nro[i] + soma
    multi = nro[i] * multi
print(soma)
print(multi)
print(nro)

#Terceira
def contatenar_tuplas(tupla1, tupla2):
    tupla3 = tupla1 + tupla2
    return tupla3
tupla1 = 3,4,5,6
tupla2 = 'oi',
tupla_contatenada = contatenar_tuplas(tupla1, tupla2)
print(tupla_contatenada)

#Quarta
def contar_elementos(tupla1, elemento):
    vezes = tupla1.count(elemento)
    return vezes
tupla1 = 1, 3, 5, 6, 5, 7, 9
elemento = 5
resul = contar_elementos(tupla1, elemento)
print(resul)

#Quinta
dupli = [1,1,2,3,4,4,5,6,6,1]
conjunt = set(dupli)
print(conjunt)

#Sexta
lista1 = ['a', 'b', 'a','c', 'b', 'd']
conjunt = set(lista1)
print(len(conjunt))

#Setima
def num_x(conjunto):
    x = conjunto.count(3)
    return x
conjunto = [1, 2, 3, 4, 5]
x = num_x(conjunto)
if x == True:
    print("Esta na lista")
else:
    print("Não esta na lista.")

#Oitava
def lista_palavra(lista):
    lista1 = lista.count('oi') and lista.count('ola')
    return dict(lista1)
lista = ['oi', 'ola', 'oi', 'ola', 'oi', 'ola']
dicionario = lista_palavra(lista)
print(dicionario)
