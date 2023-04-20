from items import Consumible, Tesoro


with open("consumibles.csv", "r") as archivo: #haciendo lista de listas de los consumibles
    lineas = archivo.readlines()[1:]
    consumibles = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        consumibles.append(linea_limpia.split(","))
with open("excavadores.csv", "r") as archivo: #haciendo lista de listas de los excavadores
    lineas = archivo.readlines()[1:]
    excavadores = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        excavadores.append(linea_limpia.split(","))
with open("tesoros.csv", "r") as archivo: #haciendo lista de listas de los tesoros
    lineas = archivo.readlines()[1:]
    tesoros = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        tesoros.append(linea_limpia.split(","))
with open("arenas.csv", "r") as archivo: #haciendo lista de listas de las arenas
    lineas = archivo.readlines()[1:]
    arenas = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        arenas.append(linea_limpia.split(","))

#vamos a hacer sub-listas con los tipos de arena

arenas_normales = []
arenas_mojadas = []
arenas_rocosas = []
arenas_magneticas = []

for arena in arenas:
    if arena[1] == "normal":
        arenas_normales.append(arena)
    elif arena[1] == "mojada":
        arenas_mojadas.append(arena)
    elif arena[1] == "rocosa":
        arenas_rocosas.append(arena)
    elif arena[1] == "magnetica":
        arenas_magneticas.append(arena)

#vamos a instanciar los Items y apendicarlos a una lista:
lista_consumibles = []
lista_tesoros = []
for item_consumible in consumibles:
    lista_consumibles.append(Consumible(Nombre = item_consumible[0], \
                                  Descripcion = item_consumible[1], \
                                  Tipo = "Consumible", \
                                  Energia = int(item_consumible[2]), \
                                  Fuerza = int(item_consumible[3]), \
                                  Suerte = int(item_consumible[4]), \
                                  Felicidad = int(item_consumible[5])))
for item_tesoro in tesoros:
    lista_tesoros.append(Tesoro(Nombre = item_tesoro[0], \
                              Tipo = "Tesoro", \
                              Descripcion = item_tesoro[1], \
                              Calidad = int(item_tesoro[2]), \
                              Cambio = item_tesoro[3]))

lista_items = [lista_consumibles, lista_tesoros] #lista de lista de items


for tipo_item in lista_items: #recordar que los items estan instanciados en datos.py
    for item in tipo_item:
        print(item.nombre)