class Salario:
    def __init__(self,base,bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base*12)+self.bonus

class empregado:
    def __init__(self,nome,idade,salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()

salario = Salario(10000, 700)
emp = empregado('Yohan', 46, salario)
print (emp.salario_total())