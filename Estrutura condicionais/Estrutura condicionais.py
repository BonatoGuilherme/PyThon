#Atividades sobre estrutura condicionais
#Primeiro
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


#Outras atividades
#Primeira
ano = int(input("DIgite um ano: "))
if ano % 4== 0 and not(ano % 100) or ano % 400 == 0:
    print("Esse ano é bissexto")
else:
    print("Não é bissexto")

#Segunda
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacional = input("Escolha entre(+, -, * ou /): ")

if operacional == "+":
    print(f"Escolheu soma, o resultado da soma dos dois números digitados é {numero1 + numero2}")
    print("Fim do programa")
elif operacional == "-":
    print(f"Escolheu subtração, o resultado da subtração dos dois números digitados é {numero1 - numero2}")
    print("Fim do programa")
elif operacional == "*":
    print(f"Escolheu multiplicação, o resultado da multiplicação é {numero1 * numero2}")
    print("Fim do programa")
elif operacional == "/":
    print(f"Escolheu divisão, o resultado da divisão é {numero1/numero2}")
    print("Fim do programa")

#terceiro
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior")
    print("Fim do programa")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior")
elif num3 > num1 and num3 > num2:
    print(f"{num3} é o maior")
elif num1 == num2 and num1 == num3 and num2 == num3:
    print("São iguais")
    print("Fim do programa")

#Quarto
nro1 = float(input("Digite um número: "))
nro2 = float(input("Digite o segundo número: "))
multiplo = nro1 % nro2
if multiplo == 0:
    print(f"{nro1} é multiplo de {nmr2}")
else:
    print("Não é multiplo")
print("Fim do programa")

#Quinto
nro = int(input("Digite um número: "))
if nro > 0:
    print("É positivo")
elif nro < 0:
    print("È negativo")
else:
    print("É zero")
print("Fim do programa")

#Sexta
temperatura = float(input("Digite a temperatura: "))
if temperatura < 14.9:
    print("Frio")
elif temperatura > 15 and temperatura < 24.9:
    print("Agradavel")
elif temperatura > 25:
    print("Quente")
print("Fim do programa")

#setima
nro = int(input("Digite um número: "))
if nro % 3==0:
    print("É divisivel por 3")
else:
    print("Não é divisivel por 3")
if nro % 5==0:
    print("É divisivel por 5")
else:
    print("Não é divisivel por 5")
print("Fim do programa")

#oitava
letra = input("Digite uma letra: ")
if letra == (letra.upper()):
    print(f"{letra} é maiuscula")
else:
    print(f"{letra} não é maiuscula")
print("Fim do programa")