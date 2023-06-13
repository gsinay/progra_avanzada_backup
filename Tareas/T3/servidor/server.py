import socket
from threading import Thread, Lock
import sys
import json

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    nombres = parametros["NOMBRES"]

class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientes = list()
        self.nombre_clientes = list()
        self.armar_servidor()

    def armar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_servidor.bind((self.host, self.port))
        except OSError:
            print("No se pudo levantar el servidor")
            sys.exit()
        self.socket_servidor.listen()
        self.escuchar_clientes()
    
    def escuchar_clientes(self):
        while True:
            try:
                print("Esperando clientes")
                socket_cliente, direccion_cliente = self.socket_servidor.accept()
                print(f"Se conecto un cliente desde {direccion_cliente}")

                #nombre cliente encaja con socket cliente, se saca de la lista de nombres
                self.clientes.append(socket_cliente)
                self.nombre_clientes.append(nombres.pop(0))
                print(self.nombre_clientes)
                thread_cliente = Thread(target=self.manejar_clientes, args=(socket_cliente, direccion_cliente))
                thread_cliente.start()
            except ConnectionError:
                print("Error al aceptar cliente")

    def manejar_clientes(self, socket_cliente, direccion_cliente):
        pass
    
        