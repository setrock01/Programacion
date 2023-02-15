"""
4. Implementar otra clase Dado. Por defecto el dado tendrá 6 caras.
Tendremos tres formar de construir un dado (uno al que no se le pasa nada e inicializa el dado al azar,
otro al que sólo se le pasa que número tiene el dado en la cara superior y otro con el número
del dado en la cara superior y el número de caras del dado). Implementa los getters, el método roll()
que tirará el dado al azar y el __str__().
Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.
"""
from random import randint
from random import sample

NUMERO_DE_CARAS_POR_DEFECTO=6
CARA_SUPERIOR_POR_DEFECTO=6

class Dado:
    def __init__(self, cara_superior=CARA_SUPERIOR_POR_DEFECTO, nro_caras=NUMERO_DE_CARAS_POR_DEFECTO):
        if (nro_caras>cara_superior):
            raise ValueError("El numero de caras no puede mayor que la cara superior")
        elif (nro_caras<=0 or cara_superior<=0):
            raise ValueError("No se admiten valores iguales o menores que 0.")
        self.cara_superior=cara_superior
        self.nro_caras=nro_caras
        self.caras=self.dame_caras
        self.cara_valor=0



    @property
    def cara_superior(self):
        return self.__cara_superior

    @cara_superior.setter
    def cara_superior(self,value):
        self.__cara_superior=value

    @property
    def nro_caras(self):
        return self.__nro_caras

    @nro_caras.setter
    def nro_caras(self,value):
        self.__nro_caras=value

    @property
    def caras(self):
        return self.__caras

    @caras.setter
    def caras(self,value):
        self.__caras=value

    @property
    def dame_caras(self):
        #caras=sample(range(1,self.cara_superior-1),self.nro_caras-1)
        caras=[self.cara_superior]
        for i in range(self.nro_caras-1):
            while True:
                valor=randint(1,self.cara_superior-1)
                if valor not in caras:
                    caras.append(valor)
                    break
        return caras

    @property
    def cara_valor(self):
        return self.__cara_valor

    @cara_valor.setter
    def cara_valor(self,value):
        self.__cara_valor=value

    @property
    def roll(self):
        self.cara_valor= self.caras[randint(0,self.nro_caras-1)]
        return self.cara_valor

    def __str__(self):
        if self.cara_valor != 0:
            return f"El ultimo valor es {self.cara_valor}"
        else:
            return "Aun no ha tirado el dado"
