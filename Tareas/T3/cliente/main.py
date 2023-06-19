from PyQt5.QtWidgets import QApplication
from frontend.front_inicio import WaitingRoom
from frontend.front_juego import GameRoom
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
    ventana_juego = GameRoom()
    logica_cliente = LogicaCliente(host, int(puerto))
    

    logica_cliente.senal_actualizar_waiting_room.connect(ventana_inicio.actualizar_waiting_room)
    logica_cliente.senal_servidor_caido.connect(ventana_inicio.servidor_caido)
    logica_cliente.senal_server_lleno.connect(ventana_inicio.server_lleno)
    logica_cliente.senal_jugador_desconectado.connect(ventana_inicio.jugador_desconectado)
    ventana_inicio.senal_partir_juego.connect(logica_cliente.check_partir_juego)
    logica_cliente.senal_error_partir_juego.connect(ventana_inicio.error_partir_juego)
    logica_cliente.senal_condiciones_ok.connect(ventana_inicio.partir_juego)
    ventana_inicio.senal_armar_ventana_juego.connect(ventana_juego.init_gui)
    logica_cliente.senal_repaint.connect(ventana_inicio.repaint)

    #ahora conectamos señales de back con front del juego

    logica_cliente.senal_turno.connect(ventana_juego.turno)
    ventana_juego.senal_anunciar_accion.connect(logica_cliente.anunciar_valor)


    sys.exit(app.exec())