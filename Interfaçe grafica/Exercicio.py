from tkinter import *
class Produto:
    nome = ""
    descricao = ""
    preco = 0
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    def info(self):
        return(f"Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}")
produto1 = Produto("Água", "Tomavel", 154)
produto1.info()

from tkinter import *
class Application:
    def __init__(self, master=None):
        for i in lista:
            print(i)
            self.widget1 =  Frame(master)
            self.widget1.pack()
            self.msg = Label(self.widget1, text=i.info())
            self.msg["font"] = ("Verdana", "10", "italic", "bold")
            self.msg.pack ()
lista = [1, 2, 3, 4, 5, 6]        
root = Tk()
Application(root)
root.mainloop()

