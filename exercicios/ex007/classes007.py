from abc import ABC, abstractmethod   # Abstract Base Classes

class Pessoa(ABC):
    def __init__ (self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar (self):
        pass


class Aluno(Pessoa):
    def __init__ (self, nome, idade, curso, turma):

        self.curso= curso
        self.turma= turma

    def fazer_matricula(self):
        pass

    def estudar (self):
        print (f"{self.nome} esta estudando {self.curso} na turma {self.turma}")

class Professor(Pessoa):
    def __init__ (self, nome ,idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass

    def estudar (self):
        print (f"{self.nome} tem {self.nivel} em {self.especialidade} ")

