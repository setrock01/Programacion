class Menu:
    def __init__(self, opciones=[], opcion_elegida=0):
        self.opciones = []
        self.opcion = opcion_elegida

    def addOpciones(self, opcion):
        self.opciones.append(opcion)

    def __str__(self):#Recorre el array opciones
        str_opciones = ""
        for i in range(len(self.opciones)):
            str_opciones += f"{i+1} - {self.opciones[i]} \n"
        return str_opciones
