from classxestatico import Pessoa

pessoa1 = Pessoa('Yohan', 18)
pessoa2 = Pessoa.apartirAnoNascimento('Joao', 1975)

print(pessoa1.idade)
print(pessoa1.nome)
print(pessoa2.idade)
print(Pessoa.ehmaiordeidade(18))