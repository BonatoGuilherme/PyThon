# Exemplo de uso de variáveis booleanas
x = True # Declara x valendo verdadeiro
y = False # Declara y valendo falso
print(f"x é do tipo {type(x)} e seu valor é {x}.")
print(f"y é do tipo {type(y)} e seu valor é {y}.")

x = 10
y = 10 
z = 11

print(x==y) #true
print(y==z) #false

print(x!=y) #false
print(x!=z) #true

print(x>=y) #true
print(y<=z)

# Inversor (not)
"""
Retorna False se o resultado
for True e True se o resultado
for False.
"""
a = True
b = False
print(a==b) # False
print(not a==b) # True

# Ou (or)
"""
Retorna True se uma das
afirmações for verdadeira
"""
x = True
y = False
print(x or y) # True

# E (and)
"""
Retorna True se ambas as
afirmações forem verdadeiras
"""
x = True
y = False
print(x and y) # False 