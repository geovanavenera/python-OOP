from rich import inspect
from pessoa import Pessoa
from professor import Professor
from aluno import Aluno

a1= Aluno ("Maria", 19, "Engenharia de Software", "N02")
a1.fazer_aniversario()
inspect (a1, methods= True)

p1= Professor ("Carlos", 37,"Arquitetura de Sistemas", "Mestrado")
inspect (p1, methods= True)