# Declaração de Classe
# Exercicio melhorando codigo anterior

class Aluno:
    """
    Essa clase cria um Aluno, que é uma pessoa que tem nome e idade
    para criar um novo aluno
    variavel = Aluno ( nome, idade)
    """
    def __init__(self, nome ='', idade = 0):
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    #Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__ (self):
        return f'{self.nome} é aluno(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
     return f'estado: nome= {self.idade}; idade {self.idade}'

# Declaração do objetos
g1 = Aluno('Geovana', 24)
g1.aniversario()
print (g1.mensagem())

print (g1.__doc__)
print (g1.__dict__) #Attrubute
print (g1.__getstate__) #Method