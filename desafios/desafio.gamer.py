from rich import print
from rich.panel import Panel

class Gamer:
    def __init__ (self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos (self, game):
        self.favoritos.append(game)

    def ficha(self):
        conteudo = f"Nome real: [blue]{self.nome}\n [/]"
        conteudo += f"\n Jogos favoritos:\n"
        for game in self.favoritos:
            conteudo += f"\n🎮 {game}"
        painel= Panel(conteudo, title= f" jogador(a) {self.nick}", width = 50)
        print(painel)

j1= Gamer("Geovana Venera", "DETONADORAdemundos")
j1.add_favoritos("God of War")
j1.add_favoritos("The Last of Us")
j1.ficha()