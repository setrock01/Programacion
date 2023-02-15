import random
from typeguard import typechecked

class dado_final:

    @typechecked
    def __int__(self, cara_superior=0, n_caras=6):
        self.caras = n_caras
        self.superior = cara_superior

    @property
    def caras(self):
        return self.__caras

    @property
    def superior(self):
        return self.__superior

    @caras.setter
    def caras(self, value):
        if value > 0:
            self.__caras = value
        else:
            raise ValueError("No se puede introducir numeros menores que 0")

    @superior.setter
    def superior(self, value):
        if value > 0:
            self.__superior = value
        else:
            raise ValueError("No se puede introducir numeros menores que 0")

    def cara_sup(self, cara_sup):
        self.__caras = [] * self.caras
        for i in range(0, self.caras):
            self.__caras[i] = random.randint(1, cara_sup)

    def cara_sup_n_caras(self, cara_sup, n_caras):
        self.__superior = cara_sup
        self.__caras[0] = cara_sup
        for i in range(1, n_caras):
            self.__caras[i] = random.randint(1, self.superior)

    def roll(self):
        numero = random.randint(0, self.__superior)
        return self.__caras[numero]
