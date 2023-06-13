from PyQt5.QtWidgets import QApplication
from frontend.front_inicio import WaitingRoom
from backend.back_cliente import LogicaCliente
from socket import socket
import sys
import os
import json


if __name__ == '__main__':
    app = QApplication([])
    if len(sys.argv) < 2:
        print("Falta ingresar host del servidor")
        sys.exit()
    puerto = sys.argv[1]
    print(puerto)

    #poner puerto en el json:
    with open("parametros.json", "r") as file:
        parametros = json.load(file)
        parametros["port"] = puerto
        host = parametros["host"]
    with open("parametros.json", "w") as file:
        json.dump(parametros, file)

    ventana_inicio = WaitingRoom()
    logica_cliente = LogicaCliente(host, int(puerto))
    sys.exit(app.exec())