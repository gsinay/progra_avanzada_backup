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

    logica_cliente.senal_actualizar_waiting_room.connect(ventana_inicio.actualizar_waiting_room)
    logica_cliente.senal_servidor_caido.connect(ventana_inicio.servidor_caido)
    logica_cliente.senal_server_lleno.connect(ventana_inicio.server_lleno)

    sys.exit(app.exec())