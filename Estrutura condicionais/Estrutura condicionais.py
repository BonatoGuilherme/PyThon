#Atividades sobre estrutura condicionais
'''#Primeiro
nmr = int(input("Digite um número: "))
resu = nmr % 2
if resu == 0:
    print("Número é par!")
else:
    print("Número é impar!")
print("Fim do programa: ")

#Segundo
nmr1 = float(input("Digite um número: "))
nmr2 = float(input("Digite outro número: "))

if nmr1 > nmr2:
    print(f"{nmr1} é maior")
else:
    print(f"{nmr2} é maior")
print("Fim do programa: ")

#Terceiro
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade")
print("Fim do programa!")
#Quarto
nota = float(input("Digite sua nota: "))
if nota == 10:
    print("A")
elif nota >= 9 and nota <= 9.9:
    print("B")
elif nota >= 8 and nota <= 8.9:
    print("C")
elif nota >= 7 and nota <= 7.9:
    print("D")
elif nota < 7:
    print("F")
print("Fim do programa!")

#Quinta
nro = float(input("Digite um número: "))
if nro > 10 and nro < 20:
    print("Esta entre 10 e 20")
else:
    print("Não esta entre 10 e 20")
print("Fim do programa")
'''

#Outras atividades

ano = int(input("DIgite um ano: "))
if ano % 4== 0 and not(ano % 100) or ano % 400 == 0:
    print("Esse ano é bissexto")
else:
    print("Não é bissexto")