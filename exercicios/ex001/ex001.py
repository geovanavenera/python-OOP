# Declaração de Classe

class Aluno:
    def __init__(self):
        # Atributos de instancia
        self.nome = ''
        self.idade = 0

    #Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é aluno(a) e tem {self.idade} anos de idade.'


# Declaração do objetos
g1 = Aluno()
g1.nome = 'Geovana'
g1.idade = 24
g1.aniversario()
g1.mensagem()

print (g1.mensagem())
