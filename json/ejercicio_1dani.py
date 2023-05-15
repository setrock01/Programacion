from Juego import Juego
import os
import re
import csv
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

extensiones = "\w+.(csv|json|xml)"


class Utilidades:
    @classmethod
    def buscar_fichero(cls, fichero):
        try:
            if re.search(extensiones, fichero):
                if os.path.exists(fichero):
                    return True
                else:
                    return False
            else:
                raise Exception("Extensión no válida")
        except Exception as e:
            print(e)

    @classmethod
    def crear_fichero(cls, fichero):
        if Utilidades.buscar_fichero(fichero):  # esta el fichero en el sistema??
            try:
                respuesta = input("Quieres sobreescribirlo? S/N: ").lower()
                if respuesta == "s":
                    f = open(fichero, "w", encoding="utf-8")
                    f.close()
                else:
                    raise Exception("No se ha modificado el fichero")
            except Exception as e:
                print(e)
        else:  # fichero no esta en el sistema
            if re.search(extensiones, fichero):
                f = open(fichero, "w", encoding="utf-8")  # Crear fichero
                f.close()
            else:
                pass

    @classmethod
    def editar_fichero(cls, fichero):
        if Utilidades.buscar_fichero(fichero):
            if re.search("\w+.csv", fichero):
                Utilidades.export_csv(fichero)
            elif re.search("\w+.json", fichero):
                Utilidades.export_json(fichero)
            elif re.search("\w+.xml", fichero):
                Utilidades.export_xml(fichero)
        else:
            print("Fichero no encontrado")

    @classmethod
    def export_json(cls, fichero):
        class juego_encoder(json.JSONEncoder):
            def default(self, objeto):
                return {
                    "Titulo": objeto.nombre,
                    "Creador": objeto.creador,
                    "Personajes": objeto.personajes,
                    "Calificacion": objeto.calificacion
                }

        juegos = []
        while True:
            juego = Utilidades.crear_juegos()
            juegos.append(juego)
            respuesta = input("¿Quieres añadir otro juego?: ").lower()
            if respuesta == "no" or respuesta == "n":
                break
        with open(fichero, "wt", encoding="UTF-8") as json_file:
            json.dump(juegos, json_file, ensure_ascii=False, indent=4, cls=juego_encoder)

    @classmethod
    def import_json(cls, fichero):
        def juego_decode(j):
            if "Titulo" in j and "Creador" in j and "Personajes" in j and "Calificacion" in j:
                return Juego(j["Titulo"], j["Creador"], j["Personajes"], j["Calificacion"])
            else:
                return j

        with open(fichero, "r", encoding="UTF-8") as json_file:
            juegos = json.load(json_file, object_hook=juego_decode)
            return juegos

    @classmethod
    def export_csv(cls, fichero):
        juegos = []
        while True:
            juego = Utilidades.crear_juegos()
            juegos.append(juego)
            respuesta = input("¿Quieres añadir otro juego?: ").lower()
            if respuesta == "no" or respuesta == "n":
                break
        with open(fichero, "w", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["Titulo", "Creador", "Personajes",
                                                          "Calificacion"])  # Le dice cuales serán las cabeceras
            writer.writeheader()  # Escribe en el csv las cabeceras
            for i in juegos:
                writer.writerow({  # Escribe las filas del csv en forma de diccionario
                    "Titulo": i.nombre,
                    "Creador": i.creador,
                    "Personajes": i.personajes,
                    "Calificacion": i.calificacion
                })

    @classmethod
    def import_csv(cls, fichero):
        juegos = []
        with open(fichero, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for fila in reader:
                cadena = fila["Personajes"].replace("'", "")  # Quita las comillas de los personajes
                lista = cadena.strip("[]").split(", ")  # con strip quita corchetes y con split crea una lista
                juegos.append(Juego(fila["Titulo"], fila["Creador"], lista, float(fila["Calificacion"])))
            return juegos

    @classmethod
    def export_xml(cls, fichero):
        xml_fichero = fichero
        try:
            tree = ET.parse(xml_fichero)
            root = tree.getroot()

        except:
            games = ET.Element("Juegos")
            tree = ET.ElementTree(games)
            root = tree.getroot()

        juegos = []
        while True:
            juego = Utilidades.crear_juegos()
            juegos.append(juego)
            respuesta = input("¿Quieres añadir otro juego?: ").lower()
            if respuesta == "no" or respuesta == "n":
                break

        for i in juegos:
            game = ET.Element("Juego", {"Nombre": i.nombre, "Calificacion": str(i.calificacion)})
            ET.SubElement(game, "Creador").text = i.creador
            personajes = ET.SubElement(game, "Personajes")
            for p in i.personajes:
                ET.SubElement(personajes, "Personaje").text = p
            root.append(game)
        tree.write(xml_fichero, encoding="utf-8")

        #para verlo mejor
        xml_minidom = minidom.parseString(ET.tostring(root))
        xml_str = xml_minidom.toprettyxml()
        with open(xml_fichero, "wt", encoding="utf-8") as archivo:
            archivo.write(xml_str)

    @classmethod
    def import_xml(cls, fichero):
        xml_fichero = fichero
        juegos = []
        tree = ET.parse(xml_fichero)
        root = tree.getroot()
        for juego in root.findall("Juego"):
            personajes = []
            nombre = juego.get("Nombre")
            calificacion = float(juego.get("Calificacion"))
            creador = juego.find("Creador").text
            for personaje in juego.find("Personajes").findall("Personaje"):
                personajes.append(personaje.text)
            juegos.append(Juego(nombre, creador, personajes, calificacion))
        return juegos

    @classmethod
    def obtener_datos(cls, fichero):
        if Utilidades.buscar_fichero(fichero):
            if re.search("\w+.csv", fichero):
                return Utilidades.import_csv(fichero)
            elif re.search("\w+.json", fichero):
                return Utilidades.import_json(fichero)
            elif re.search("\w+.xml", fichero):
                return Utilidades.import_xml(fichero)
        else:
            print("Fichero no encontrado")

    @classmethod
    def crear_juegos(cls):
        personajes = []
        nombre_juego = input("Indica el nombre del juego: ")
        creador = input("Indica el creador del juego: ")
        print("Ahora vamos a guardar los personajes jugables")
        while True:
            personaje = input("Indica el nombre del personaje: ")
            if personaje.strip() == "":
                break
            else:
                personajes.append(personaje)
        calificacion = float(input("Indica la calificación del juego: "))
        return Juego(nombre_juego, creador, personajes, calificacion)
