class Carro: 
    marca = ""
    modelo = ""
    amo = ""

    def __init__(self, marca, modelo, ano): #Construtor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def exibir_info(self): 
        print(f"Carro: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")