from rich import inspect

class Pessoa:
    def __init__ (self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__ (self, nome, idade, curso, turma):
        super ().__init__(nome , idade)
        self.curso= curso
        self.turma= turma

    def fazer_matricula(self):
        pass

class Professor(Pessoa):
    def __init__ (self, nome ,idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass

a1= Aluno ("Maria", 19, "Engenharia de Software", "N02")
a1.fazer_aniversario()
inspect (a1, methods= True)

p1= Professor ("Carlos", 37,"Arquitetura de Sistemas", "Mestrado")
inspect (p1, methods= True)