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

#Sexta
def media_final(nota, total_notas):
    mediafinal = nota / total_notas
    return mediafinal
nota = 0
total_notas = 0
notas = int(input("Digite quantas notas tem para fazer a media final: "))
while notas != 0:
    nro = int(input("Digite suas notas"))
    nota = nro + nota
    notas-= 1
    total_notas+=1
print(f"A media das notas é {media_final(nota, total_notas)}")

#Setima
def reverso_numero(numero):
    numero_reverso = str(numero)[::-1]
    return numero_reverso
numero = input("Digite um número: ")
print(reverso_numero(numero))

#Oitava
def m(mes):
    if mes == 1:
        return("Janeiro")
    elif mes == 2:
        return("Fevereiro")
    elif mes == 3:
        return("Março")
    elif mes == 4:
        return("Abril")
    elif mes == 5:
        return("Maio")
    elif mes == 6:
        return("Junho")
    elif mes == 7:
        return("Julho")
    elif mes == 8:
        return("Agosto")
    elif mes == 9:
        return("Setembro")
    elif mes == 10:
        return("Outubro")
    elif mes == 11:
        return("Novembro")
    elif mes == 12:
        return("Dezembro")
dia = int(input("Digite seu dia de aniversario: "))
mes = int(input("Digite seu mes de aniversario: "))
ano = int(input("Digite seu ano de nacimento: "))

print(f"Seu aniversario é {dia} de {m(mes)} de {ano}")