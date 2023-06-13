from server import Servidor
import socket
from threading import Thread
import sys
import json

if __name__ == "__main__":
    #verificamos el puerto a ocupar y lo guardamos en el json
    if len(sys.argv) < 2:
        print("Falta ingresar host del servidor")
        sys.exit()
    puerto = sys.argv[1]
    #poner puerto en el json:
    with open("parametros.json", "r") as file:
        parametros = json.load(file)
        parametros["port"] = puerto
        host = parametros["host"]
    with open("parametros.json", "w") as file:
        json.dump(parametros, file)
    print(f"El serividor esta en el host {host} y puerto {puerto}")

    servidor = Servidor(host, int(puerto))






