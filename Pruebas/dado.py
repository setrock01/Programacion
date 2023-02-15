import random


class Dado:

    def __int__(self):
        self.caras = [1, 2, 3, 4, 5, 6]

    def lanzar(self):
        return self.caras[random.randint(0, 5)]
