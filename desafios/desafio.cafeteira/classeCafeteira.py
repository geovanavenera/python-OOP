from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print ('---- iniciando preparo------')
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print ('Fervendo agua por 180 graus Celsius')


    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass



class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('Passando agua pressurizada pelo pó de cafe moído')

    def servir(self):
        print ('Servindo em xícara pequena')
        print('------Café pronto------')

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print ('Mergulhar o sache de ervas na agúa')

    def servir(self):
        print ('Servir em uma caneca de porcelana media')
        print ('-----Chá esta pronto-------')

