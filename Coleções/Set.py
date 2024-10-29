# Declaração de sets
set_a = {"laranja", "batata", "vinho"}
set_b = set(["cadeira", "mesa", "armário"])
set_c = set("abracadabra")
set_d = set("alakazan")

# Imprimindo sets
print(set_a)
# {'batata', 'laranja', 'vinho'}
print(set_b)
# {'armário', 'mesa', 'cadeira'}
print(set_c)
# {'b', 'd', 'r', 'a', 'c'}
print(set_d)
# {'l', 'k', 'n', 'a', 'z'}

# letras em set_c, mas não em set_d
print(set_c - set_d)
# {'d', 'b', 'c', 'r'}
# letras em set_c ou em set_d ou ambos
print(set_c | set_d)
# {'b', 'n', 'a', 'l', 'z', 'c', 'r', 'd', 'k'}
# letras em ambos set_c e set_d
print(set_c & set_d)
# {'a'}
# letras em set_c ou set_d, mas não em ambos
print(set_c ^ set_d)
# {'b', 'k', 'n', 'l', 'z', 'c', 'r', 'd'}