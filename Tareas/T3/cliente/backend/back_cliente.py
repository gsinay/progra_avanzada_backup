from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import os
import sys
import json
import socket
import threading
import time
from Scripts.cripto import encriptar_y_codificar, decodificar_y_desencriptar

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    N_PONDERADOR = int(parametros["N_PONDERADOR"])


class LogicaCliente(QObject):
    senal_actualizar_waiting_room = pyqtSignal(list)
    def __init__(self, host, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = host
        self.port = port
        self.nombre = None
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Conectado al servidor")
            #generar thread del cliente
            thread_cliente = threading.Thread(target=self.recibir_datos)
            thread_cliente.start()

        except ConnectionRefusedError:
            print("No se pudo conectar al servidor, intente nuevamente")
        
    def recibir_datos(self):
        while True:
            try:
                mensaje = self.recibir_mensaje()
                mensaje_decodificado = decodificar_y_desencriptar(mensaje, N_PONDERADOR)
                if self.nombre == None:  #es el primer mensaje que recibimos automaticamente con nuestro nombre
                    self.nombre = mensaje_decodificado
                    print(f"Mi nombre es {self.nombre}")
                else:
                    if mensaje_decodificado[0].lower() == "jugadores:": #si recibimos jugador nuevo actualizamos el waiting room
                        self.actualizar_waiting_room(mensaje_decodificado[1])
            except ConnectionResetError:
                print("Se desconectó el servidor.")
                break
    
    def recibir_mensaje(self):
        largo_mensaje = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_mensaje, byteorder="big")
        mensaje = self.socket_cliente.recv(largo_mensaje)
        return mensaje
        
    def actualizar_waiting_room(self, nombres):
        time.sleep(1)
        self.senal_actualizar_waiting_room.emit(nombres)
            

if __name__ == "__main__":
    cliente_prueba = LogicaCliente("localhost", 9999)

