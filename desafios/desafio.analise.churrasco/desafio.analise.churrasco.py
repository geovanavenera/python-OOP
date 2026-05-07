from rich import print

class Churrasco:
    # Analise para calcular quantidade total de Kg, custo total do churrasco
    # e calcular quantidade de cada pessoa individual ira pagar


    def __init__(self, titulo, quant, kg_pessoa=0.4, valor_kg=84):
        self.titulo = titulo
        self.quant = quant
        self.kg_pessoa = kg_pessoa
        self.valor_kg = valor_kg

    def __str__(self):
        return (
            f"Analisando {self.titulo} com {self.quant} convidados\n"
            f"Cada participante comerá {self.kg_pessoa} kg e cada kg custa R${self.valor_kg:.2f}"
        )

    def analisar(self):
        kg_total = self.kg_pessoa * self.quant
        valor_total = kg_total * self.valor_kg
        valor_pessoa = valor_total / self.quant

        return (
            f"Recomendo comprar {kg_total:.2f} Kg de carne\n"
            f"O custo total será de R${valor_total:.2f}\n"
            f"Cada pessoa pagará R${valor_pessoa:.2f}"
        )


c1 = Churrasco("Churras da  Luiza", 15)
print(c1)
print(c1.analisar())