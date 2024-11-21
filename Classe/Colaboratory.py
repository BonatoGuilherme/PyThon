'''
class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def exibir_info(self):
        print(f"Carro: {self.__marca} {self.__modelo}")

    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

carro = Carro("Toyota", "Supra")
carro.exibir_info()
carro.set_marca("Donda")
carro.exibir_info()

class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    def info(self):
        print(f"Marca: {self.marca}")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    def info(self):
        super().info
        print(f"Modelo: {self.modelo}")

from abc import ABC, abstractmethod
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * (self.raio ** 2)
class Quadrado(Forma):
    def __init__ (self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

#Uso de classes
circulo = Circulo(5)
quadrado = Quadrado(4)

print(f"Área do circulo: {circulo.area()}")
print(f"Área do quadrado: {quadrado.area()}")

class Animal:
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        print("O cachorro faz: Au Au")

class Gato(Animal):
    def som(self):
        print("O gato faz: Miau")

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.som()

class Banco():
    def __init__(self, saldo):
        self.__saldo = saldo  # saldo inicial
    def exibir_info(self):
        print(f"Seu saldo: {self.__saldo}")
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor}!")
        else:
            print("Valor inválido para depósito.")
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor}!")
        else:
            print("Saldo insuficiente para saque.")

dinheiro = Banco(155)
dinheiro.exibir_info()
dinheiro.depositar(50)
dinheiro.exibir_info()
dinheiro.sacar(100)
dinheiro.exibir_info()
'''
class Funcionario():
    def __init__(self, nome, salario, departamento):
        self.__nome = nome
        self.__salario = salario
    def exibir_info(self):
        print(f"Nome: {self.__nome}, Sálario: {self.__salario}")
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.__departamento = departamento
    def info(self):
        super().info()
        print(f"Departamento: {self.__departamento}")
Gerente = ("Gustavo", 1.700, 'got')
Gerente.info()

