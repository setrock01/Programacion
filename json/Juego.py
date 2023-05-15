from typeguard import typechecked


class Juego:
    @typechecked
    def __init__(self, nombre: str, creador: str, personajes: list, calificacion: float):
        self.nombre = nombre
        self.creador = creador
        self.personajes = personajes
        self.calificacion = calificacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def creador(self):
        return self.__creador

    @creador.setter
    def creador(self, value):
        self.__creador = value

    @property
    def personajes(self):
        return self.__personajes

    @personajes.setter
    def personajes(self, value: list):
        self.__personajes = value

    @property
    def calificacion(self):
        return self.__calificacion

    @calificacion.setter
    def calificacion(self, value):
        self.__calificacion = value

    def __str__(self):
        s = "Personajes Jugables:\n"
        for i in self.personajes:
            s += f"- {i}\n"
        return "Nombre: {}\n" \
               "Creador: {}\n" \
               "{}" \
               "CalificaciÃ³n: {}".format(self.nombre, self.creador, s, self.calificacion)