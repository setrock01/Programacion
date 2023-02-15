from menu import Menu
from fecha import Fecha

test = Menu()

while True:
    valor = input("Introduce un valor para el menu:")
    if valor.strip() == "":
        break
    test.addOpciones(valor)

f = Fecha()

while True:
    opcion = int(input("Elige una de las opciones introducidas: "))
    if opcion == 1:
        f.comprobar_fecha()
        print(f)
    elif opcion == 2:
        f.addDias()
        print(f"Fecha actualizada: {f}")
    elif opcion == 3:
        f.addMes()
        print(f"Fecha actualizada: {f}")
    elif opcion == 4:
        f.addAge()
        print(f"Fecha actualizada: {f}")
    elif opcion == 5:
        f2 = Fecha()
        f2.comprobar_fecha()
        f.compararFechas(f2)
    elif opcion == 6:
        print(f.mostrarFecha())
    else:
        print("Cerrando menú")
        break

# "Introducir fecha (dd/mm/aaaa)", "Añadir días", "Añadir meses",
# "Añadir años", "Comparar fechas","Mostrar formato largo", "Salir"