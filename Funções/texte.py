def posi_ou_nega(num):
    if nro > 0:
        return "P, ou seja, positivo"
    else:
        return "N, ou seja, nagativo"

nro = int(input("Digite um numero: "))
print(f"O {nro} é {posi_ou_nega(nro)}")