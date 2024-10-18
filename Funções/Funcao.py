#Função
def bem_vindo():
    print("Bem-vindo ao Python")
#Chama a função
bem_vindo()

#Usando parâmetros
def bem_vindo(nome):
    print("Bem-vindo ao Python " + nome + "!")

bem_vindo("Joaquim")
bem_vindo("Henrique")

#Multiplos parâmetros
def bem_vindo(nome, sobrenome):
    print(f"Bem-vindo ao python {nome} {sobrenome}!")

bem_vindo("Pedro", "Silva") #Posicional
#Saida: Bem-vindo ao python Pedro silva!

bem_vindo(sobrenome="Vagas", nome="Dion") #Nomeado
#Saida: Bem-vindo ao python Dion Vargas!

#Argumento padrão
def bem_vindo(nome, linguagem="Python"):
    print(f"Bem-vindo ao {linguagem} {nome}")
bem_vindo("pedro")
#Saida:bem-vindo ao python pedro!
bem_vindo("Dion", "Java")
#Saida: bem-vindo ao java dion!

#multiplos parametros
def cumprimento (*nomes):
    for nome in nomes:
        print(f"Oi{nome}")
cumprimento ("paulo", "dion", "antan")
#Saida: oi paulo, oi dion e oi antan