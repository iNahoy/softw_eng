class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome=nome

    def set_ender(self, ender):
        self.ender=ender
    
    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

pessoaA = Pessoa("Jorge","Rua Barao de Frexeiras")
pessoaB = Pessoa("Yohan","Sunset Strip")
print("Primeira pessoa cadastrada: " ,pessoaA.get_nome(), "\nMoradia: " ,pessoaA.get_ender())
print("Segunda pessoa cadastrada: " ,pessoaB.get_nome(),"\nMoradia: " ,pessoaB.get_ender())