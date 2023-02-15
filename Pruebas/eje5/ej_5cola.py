from typeguard import typechecked


class Cola:

    @typechecked
    def __init__(self, elementos: list = []):
        self.elementos = []
        self.elementos = elementos

    @property
    def elementos(self):
        return self.__elementos

    @elementos.setter
    def elementos(self, value):
        self.__elementos = value

    def num_elementos(self):
        return len(self.elementos)

    def cola_vacia(self):
        return self.num_elementos() == 0

    def clear_cola(self):
        self.elementos = []

    def encolar(self, valor):
        self.elementos.append(valor)

    def desencolar(self):
        if self.cola_vacia():
            raise RuntimeError("ERROR: La cola esta vacía")
        else:
            print("sacando el valor:", self.leerFrontal())
            self.elementos.pop(0)

    def leerFrontal(self):
        if self.cola_vacia():
            raise RuntimeError("ERROR: La cola esta vacia")
        else:
            return self.elementos[0]

