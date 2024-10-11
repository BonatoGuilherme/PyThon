#conversão de inteiro para float
numero_inteiro = 42
numero_float = float(numero_inteiro)
print(f"Conversão de {numero_inteiro} para float: {numero_float}")

#Ao contrario

nro_float = 42.9
nro_inteiro = int(nro_float)
print(f"A conversão de {nro_float} para inteiro é {nro_inteiro}")
print(f"O Tipo de variavel nro_inteiro é: {type(nro_inteiro)}")

#Conversão de string para inteiro

nro_string = "100"
nro_int = int(nro_string)
print(f"A conversão de {nro_string} para inteiro é {nro_int}")
print(f"O Tipo de variavel nro_int é: {type(nro_int)}")

#Conversão de string para float

nmr_string_float = "123.456"
nmr_float = float(nmr_string_float)
print(f"A conversão de {nmr_string_float} para float é {nmr_float}")
print(f"O Tipo de variavel nmr_float é: {type(nmr_float)}")

#Conversão de inteiro para string

nmr_inteiro = 12321
nmr_string = str(nmr_inteiro)
print(f"A conversão de {nmr_inteiro} para string é {nmr_string}")
print(f"O Tipo de variavel nmr_string é: {type(nmr_string)}")

#Conta

numero = int(input("digite um numero"))
print(f"Número vale {numero} e seu tipo é: {type(numero)}")

print(f"O calculo é {numero + 3}")