with open("consumibles.csv", "r") as archivo: #haciendo lista de listas de los consumibles
    lineas = archivo.readlines()[1:]
    consumibles = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        consumibles.append(linea_limpia.split(","))
with open("tesoros.csv", "r") as archivo: #haciendo lista de listas de los tesoros
    lineas = archivo.readlines()[1:]
    tesoros = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        tesoros.append(linea_limpia.split(","))