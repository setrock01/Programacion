from typeguard import typechecked


class Pila:

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

    def pila_vacia(self):
        return self.num_elementos() == 0

    def clear_pila(self):
        self.elementos = []

    def apilar(self, valor):
        self.elementos.append(valor)

    def desapilar(self):
        if self.pila_vacia():
            raise RuntimeError("La pila esta vacía")
        else:
            print("Se va a eliminar: ", self.leerSuperior())
            self.elementos.pop()

    def leerSuperior(self):
        if self.pila_vacia():
            raise RuntimeError("La pila esta vacía")
        else:
            return self.elementos[len(self.elementos) - 1]

