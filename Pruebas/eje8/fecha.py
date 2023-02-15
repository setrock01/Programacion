from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")


class Fecha:

    def __init__(self):
        self.fecha = ""

    def comprobar_fecha(self, otra_fecha = ""):
        flag = True
        while flag:
            try:
                fecha_introducida = input("introduce una fecha con el formato dd/mm/YYY: ")
                self.fecha = datetime.strftime(fecha_introducida, "%d/%m/%Y").date()
                flag = False
            except Exception as e:
                print("Se ha producifo un error al introducir una fecha: ", str(e))

    def __str__(self):
        return self.fecha.strftime("%d/%m/%Y")

    def addDias(self):
        # opcion 2
        dias = int(input("Indica los dias a sumar a la fecha previa: "))
        self.fecha += timedelta(days=dias)

    def addMes(self):
        # opcion 3
        mes = int(input("Indica los meses a sumar a la fecha previa: "))
        self.fecha += relativedeal(months=mes)

    def addAge(self):
        # opcion 4
        age = int(input("indica los años a sumar a la fecha previa: "))
        self.fecha += relativedeal(years=age)

    def compararFechas(self, otra_fecha):
        # opcion 5
        if self.fecha > otra_fecha.fecha:
            diferencia = (self.fecha - otra_fecha).days
            print(f"La fecha {otra_fecha} es anterior a {self.fecha} por {diferencia} dias")
        elif self.fecha < otra_fecha.fecha:
            diferencia = (otra_fecha - self.fecha).days
            print(f"La fecha {otra_fecha} es posterior a {self.fecha} por {diferencia} dias")
        else:
            print("Las fechas son iguales")

    def mostrarFecha(self):
        # opcion 6
        return self.fecha.strftime("%A, %d de %B de %Y").title()
