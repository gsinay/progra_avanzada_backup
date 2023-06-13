from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import os
import sys
import json
import socket
from threading import Thread

class LogicaCliente(QObject):
    def __init__(self, host, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Conectado al servidor")
        except ConnectionRefusedError:
            print("No se pudo conectar al servidor, intente nuevamente")
            

if __name__ == "__main__":
    cliente_prueba = LogicaCliente("localhost", 9999)

