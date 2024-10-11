#Primeira
inicio = 10
fim = 21
sequencia = range(inicio, fim)
print(list(sequencia))

#Segunda
for hello in range(5):
    print("Ola, mundo!")

#terceira
for i in range(11):
    if i%2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é impar")

#Quarto
nro = 10
while nro >=0:
    print(nro)
    nro -= 1

#Quinto
soma = 0
nro = 1
limite = 100
while nro <= limite:
    soma = nro + soma
    print(soma)
    nro+=1

#Sexta
for i in range(1, 11):
    print(i ** 2)

#Setima
nro = 0
for i in range(1, 21):
    if i % 2==0:
        nro = i + nro
        print(nro)

#oitava
media_final = 0
for i in range(0, 5):
    nota = int(input(f"Digite suas nota: "))
    media_final = nota + media_final
media_final = media_final/5
print(media_final)

#nona
nro = int(input("Digite um número para que seja feita a tabuada: "))
for i in range(0, 11):
    tabu = nro * i
    print(tabu)

#Decima
fatorial = 1
nro = int(input("Digite um número: "))
while nro > 0:
    fatorial = fatorial * nro
    nro-=1
    
print(fatorial)

