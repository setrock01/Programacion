from ejercicio_1dani import Utilidades
#Utilidades.crear_fichero("fichero.xml")
#Utilidades.editar_fichero("fichero.xml")


juegos = Utilidades.obtener_datos("fichero.xml")

for i in juegos:
    print(i)

