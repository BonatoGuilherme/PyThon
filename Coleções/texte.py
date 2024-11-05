#Oitava
def lista_palavra(lista):
    dicionario = {}
    for lista in lista:
        if lista in dicionario:
            dicionario[lista] += 1
        else:
            dicionario[lista] = 1
    return dicionario
lista = ['oi', 'ola', 'oi', 'ola', 'oi', 'ola']
dicionario = lista_palavra(lista)
print(dicionario)
