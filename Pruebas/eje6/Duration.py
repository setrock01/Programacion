from typeguard import typechecked


class Durarion:

    @typechecked
    def __init__(self, t1: list = [], t2: list = [], t3: list = []):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t1_seg = 0
        self.t2_seg = 0
        self.t3_seg = 0


    @property
    def t1(self):
        return self.__t1

    @t1.setter
    def t1(self, value):
        self.__t1 = value

    @property
    def t2(self):
        return self.__t2

    @t2.setter
    def t2(self, value):
        self.__t2 = value

    @property
    def t3(self):
        return self.__t3

    @t3.setter
    def t3(self, value):
        self.__t3 = value

    def seg_total(self):
        valor = 3600
        for i in range(len(self.t1)):
            if valor == 1:
                self.t1_seg += self.t1[i]
                valor = 3600
            else:
                self.t1_seg += self.t1[i] * valor
                valor /= 60
        for i in range(len(self.t2)):
            if valor == 1:
                self.t2_seg += self.t2[i]
                valor = 3600
            else:
                self.t2_seg += self.t2[i] * valor
                valor /= 60
        for i in range(len(self.t3)):
            if valor == 1:
                self.t3_seg += self.t3[i]
                valor = 3600
            else:
                self.t3_seg += self.t3[i] * valor
                valor /= 60
        return print(self.t2_seg)

    def remplazar_tiempo(self):
        self.t1 = self.t1_seg
        self.t2 = self.t2_seg
        self.t3 = self.t3_seg

    def tiempo_t1(self):
        horas = self.t1_seg // 3600
        self.t1_seg -= horas * 3600
        minutos = self.t1_seg // 60
        self.t1_seg -= minutos * 60
        segundos = self.t1_seg

        print(f"t1 = {self.t1}seg son: {horas}h {minutos}min {segundos}seg")

    def tiempo_t2(self):
        horas = self.t2_seg // 3600
        self.t2_seg -= horas * 3600
        minutos = self.t2_seg // 60
        self.t2_seg -= minutos * 60
        segundos = self.t2_seg

        print(f"t2 = {self.t2}seg son: {horas}h {minutos}min {segundos}seg")

    def tiempo_t3(self):
        horas = self.t3_seg // 3600
        self.t3_seg -= horas * 3600
        minutos = self.t3_seg // 60
        self.t3_seg -= minutos * 60
        segundos = self.t3_seg

        print(f"t3 = {self.t3}seg son: {horas}h {minutos}min {segundos}seg")
