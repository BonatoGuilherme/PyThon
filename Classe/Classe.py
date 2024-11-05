class Produto: #Classe com nome sempre em maiusculo
    preco = 0.0 #Atributos
    nome = ""   #Atributos

    def __init__(self, nome, preco): #Construtor sempre sera __init__
        self.nome = nome #como é construido
        self.preco = preco 
        
    def exibir_info(self): # Oque ira fazer
        print(f"Produto: {self.nome}, Preço: R${self.preco: 2F}")

produto1 = Produto("Caneta", 1.50)
produto2 = Produto("Caderno", 5.00)
produto1.exibir_info()
produto2.exibir_info()