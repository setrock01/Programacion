class Automovil:

    def __init__(self, motor, potencia, marca, modelo):
        self.motor = motor
        self.marca = marca
        self.set_potencia(potencia)
        self.modelo = modelo
        self.arrancando = False

    def set_potencia(self, potencia):
        if potencia < 0:
            self.__potencia = 0
        else:
            self.__potencia = self.__potencia

    def get_potencia(self):
        return self.__potencia

    def arrancar(self):
        if not self.arrancando:
            print("Estoy arrancando")
            self.arrancando = True
        elif self.arrancando:
            print("El veiculo ya está arrancado")

    def parar(self):
        if not self.arrancando:
            print("Ya esta parado")
        elif self.arrancando:
            print("El veiculo esta parando")
            self.arrancando = False

    def __str__(self):
        return f"Marca {self.marca} modelo {self.modelo}"
