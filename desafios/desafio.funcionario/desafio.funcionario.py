from rich import print
class Funcionario:
    """
    Criar mensagem de apresentação para cada funcionario da empresa
    """
    empresa= "Curso em Video"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao (self):
        return f"Olá, sou [red]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {self.empresa}"

Funcionario.empresa = "Hostnet"

c1= Funcionario ("Luiza", "Financeiro", "Gerente")
print (c1.apresentacao())

c2= Funcionario ("Pedro", "TI", "Programador")
print (c2.apresentacao())