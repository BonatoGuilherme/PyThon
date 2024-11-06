#Primeira
class Produto: #Classe com nome sempre em maiusculo
    preco = 0.0 #Atributos
    nome = ""   #Atributos
    perc_de_desconto = 0.0
    quantidade = 0
    venda = 0

    def __init__(self, nome, preco, perc_de_desconto, quantidade, venda): #Construtor sempre sera __init__
        self.nome = nome #como é construido
        self.preco = preco 
        self.perc_de_desconto = perc_de_desconto
        self.quantidade = quantidade
        self.venda = venda

    def exibir_info(self): # Oque ira fazer
        if self.quantidade > 0 and self.quantidade - self.venda >= 0:
            print(f"Produto: {self.nome}, Preço com desconto: RS{self.preco * (1 - self.perc_de_desconto):.2f}, Estoque: {self.quantidade}")
        else:
            print(f"Poduto: {self.nome}, Preço: R${self.preco * (1 - self.perc_de_desconto):.2f}, Estoque: Fora de estoque")
produto1 = Produto("Caneta", 1.50, 0.10, 16, 1)
produto2 = Produto("Caderno", 5.00, 0.15, 1, 1)
produto1.exibir_info()
produto2.exibir_info()