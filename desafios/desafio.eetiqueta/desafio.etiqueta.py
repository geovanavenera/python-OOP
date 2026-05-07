from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"


    def etiqueta (self):
        conteudo= f"{self.nome.center (75,' ')}"
        conteudo += f"{'-' * 75}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center (77, '-')}"
        etiqueta= Panel(conteudo , title="Produto")
        print (etiqueta)

p1= Produto ("Iphone 15 Pro Max",6000 )

p1.etiqueta()
p2= Produto ("Notebook Dell Inspiron", 5800)
p2.etiqueta()