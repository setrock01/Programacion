SEGUNDOS_MINUTO=60


class Duration:
    def __init__(self,horas_duracion=0,minutos=0,segundos=0):
        if isinstance(horas_duracion,Duration):
            self.horas=horas_duracion.horas
            self.minutos = horas_duracion.minutos
            self.segundos = horas_duracion.segundos
        else:
            self.horas = horas_duracion
            self.minutos = minutos
            self.segundos = segundos


    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self,value):
        self.__horas=value

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, value):
        if (value < 0 and value > -60):
            value = 60 + value
            self.horas=(self.horas - 1)

        elif (value <= -60):
            horas_sub = abs(value) // 60
            value = abs(value) % 60
            self.horas = (self.horas - horas_sub)
        elif (value >= 60):
            horas_ad = value // 60
            value = value % 60
            self.horas = (self.horas + horas_ad)
        self.__minutos = value

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, value):
        if (value<0 and value>-60):
            value = SEGUNDOS_MINUTO + value
            self.minutos=(self.minutos - 1)
        elif(value<=-60):
           minutos_sub=abs(value)//60
           value=abs(value) % 60
           self.minutos=(self.minutos - minutos_sub)
        elif (value>=60):
            minutos_ad=value//60
            value= value % 60
            self.minutos=(self.minutos + minutos_ad)
        self.__segundos=value

    def __str__(self):
        return f"{self.horas}h {self.minutos}m {self.segundos}s"

    def __add__(self, other):
        return Duration (self.horas+other.horas,self.minutos+other.minutos,self.segundos+other.segundos)

    def __sub__(self, other):
        return Duration (abs(self.horas-other.horas),abs(self.minutos-other.minutos),abs(self.segundos-other.segundos))


    def add_sub_time(self,segundos_add=0,minutos_add=0,horas_add=0):
        if segundos_add != 0:
            self.segundos=(self.segundos + segundos_add)
        if minutos_add != 0:
            self.minutos=(self.minutos + minutos_add)
        if horas_add != 0:
            self.horas=(self.horas + horas_add)
