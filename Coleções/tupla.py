# Declaração de tuplas
x = 12345, 54321, "olá!", "mundo"
y = "abc", 123.456
z = 123,

# Imprimindo conjuntos
print(x)
# (12345, 54321, 'olá!', 'mundo')
print(y)
# ('abc', 123.456)
print(z)
# (123,)

# Imprimindo posições das tuplas
print(x[2])
# olá
print(y[1])
# 123.456
print(z[0])
# 123

# Aninhamento de tuplas
u = z, "Aninhada", y
print(u)
# ((123,), 'Aninhada', ('abc', 123.456))

# Tuplas são imutáveis
u[0]="Outro valor"
"""
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
"""
