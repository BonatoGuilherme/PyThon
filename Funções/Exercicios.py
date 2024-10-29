#Primeira
def par_impar(nrm):
    if nrm % 2== 0:
        print(f"O {nrm} é par")
    else:
        print(f"{nrm} é impar")
num = int(input("Digite um numero inteiro maior que 0: "))
par_impar(num)

#Segunda
def parametros (*num):
    num = nro + nro1 + nro2
    print(i)
nro = int(input("Digite um numero: "))
nro1 = int(input("Digite um numero: "))
nro2 = int(input("Digite um numero: "))
parametros(nro, nro1, nro2)

#Terceiro
def converter_moeda(BRL):
    taxa = 5
    BRL = USD * taxa
    return BRL
USD = float(input("Digite o valor em dolar: "))
print(f"O Valor em reais é {converter_moeda(USD)}")

#Quarto
def qtd(num):
    print(len(num))
num = input("Digite um numero: ")
qtd(num)

#Quinto
def posi_ou_nega(num):
    if nro > 0:
        return "P, ou seja, positivo"
    else:
        return "N, ou seja, nagativo"

nro = int(input("Digite um numero: "))
print(f"O {nro} é {posi_ou_nega(nro)}")

