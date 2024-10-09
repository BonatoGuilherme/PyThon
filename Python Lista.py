#Primeira
nota1 = float(input("Digite sua primeira Nota:"))
nota2 = float(input("Digite sua segunda Nota:"))
nota3 = float(input("Digite sua terceira Nota:"))
resul = (nota1 + nota2 + nota3)/3
print(f"Sua media final é: {resul}")

#Segunda
tempoMinutos = float(input("Digite um tempo em minutos: "))
tempoSegundo = tempoMinutos * 60
print(f"Seu tempo em segundos é: {tempoSegundo}")

#Terceiro
distancia = float(input("Digite sua distancia percorrida em KM/h:"))
tempo = float(input("O tempo em que percorreu: "))
velMedia = distancia/tempo * 60
print(f"A velocidade media é {velMedia} durante seu percurso")

#Quarto
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto do produto: "))
precoFinal = preco *(1 - (desconto/100))
print(f"O preco apos o desconto é {precoFinal}")

#Quinto
Kg = float(input("Digite o seu peso: "))
Altura = float(input("Digite sua altura: "))
Imc = Kg/(Altura * Altura)
print(f"O imc é {Imc}")