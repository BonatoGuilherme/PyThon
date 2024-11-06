# Declaração de dicionários
pc_1 = {'SSD': 250, 'CPU': 'Intel', 'RAM': '8gb'}
pc_2 = {'SSD': 1000, 'CPU': 'AMD', 'RAM': '16gb'}

print(pc_1)
print(pc_2)

#Print dicionarios
print(pc_1['CPU'])
print(pc_2['RAM'])

# Adicionando novos itens em dicionários
pc_1["water_cooler"] = False
pc_2["water_cooler"] = True
print(pc_1)
# {'SSD': 250, 'CPU': 'Intel', 'RAM': '8gb', 'water_cooler': False}
print(pc_2)
# {'SSD': 1000, 'CPU': 'AMD', 'RAM': '16gb', 'water_cooler': True}""