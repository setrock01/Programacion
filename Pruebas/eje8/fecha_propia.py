class FechaPropia:

    def __init__(self):
        self.fecha = []
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "diciembre"]
        self.mes_30 = [4, 6, 9, 11]
        self.mes_31 = [1, 3, 5, 7, 8, 10, 12]
        self.bisiesto = False
        self.dia_max = 0

    def introducir_fecha(self):
        dia = 0
        flag = True
        while flag:
            try:
                fecha_introducida = input("Introduce una fecha con el formato 'dd/mm/YYYY': ")
                fecha_introducida = fecha_introducida.split(sep="/")
                for i in range(len(fecha_introducida)):
                    fecha_introducida[i] = int(fecha_introducida[i])
                flag = False
                for e in range(0, len(fecha_introducida)):
                    print(fecha_introducida[e])
                self.comprobar_fecha(fecha_introducida)
            except Exception as e:
                print("Se ha producifo un error al introducir una fecha: ", str(e))

    def comprobar_fecha(self, valor: list):
        check = False
        if 0 < valor[1] <= 12:
            if valor[1] in self.mes_30:
                self.dia_max = 30
            elif valor[1] in self.mes_31:
                self.dia_max = 31
            elif valor[1] == 2:
                if (valor[2] % 4 != 0) or (valor[2] % 4 == 0 and valor[2] % 100 == 0 and valor[2] % 400 != 0):
                    self.dia_max = 28
                    self.bisiesto = False
                elif (valor[2] % 4 == 0 and valor[2] % 100 != 0) or (valor[2] % 4 == 0 and valor[2] % 100 == 0 and valor[2] % 400 == 0):
                    self.dia_max = 29
                    self.bisiesto = True
            else:
                raise ValueError("ERROR")
            if 0 < valor[0] <= self.dia_max:
                check = True
            else:
                raise ValueError("ERROR: El dia no concuerda con el mes")
            if check and valor[2] > 0:
                print("fecha introducida correctamente")
                self.fecha = valor
        else:
            raise ValueError("ERROR: Los meses deben de estar entre el 1 y el 12")

    def add_dias(self, valor):
        self.fecha[0] += valor
        if self.fecha[0] >

    def diaMax(self):
        if self.fecha[1] in self.mes_31:
            self.dia_max

f = FechaPropia()
f.introducir_fecha()
