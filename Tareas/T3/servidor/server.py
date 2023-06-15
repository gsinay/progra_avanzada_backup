import socket
from threading import Thread, Lock
import sys
import json
from Scripts.cripto import encriptar_y_codificar, decodificar_y_desencriptar

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    NOMBRES = parametros["NOMBRES"]
    N_PONDERADOR = int(parametros["N_PONDERADOR"])
    NUMERO_JUGADORES = int(parametros["NUMERO_JUGADORES"])



class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientes = list()
        self.nombre_clientes = list()
        self.clientes_standby = list()
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

                #si la sala esta llena se le avisa al cliente y se deja en standby
                if len(self.nombre_clientes) >= NUMERO_JUGADORES:
                    self.broadcast_mensaje_especifico(socket_cliente, ("Servidor lleno", self.nombre_clientes))
                    self.clientes_standby.append(socket_cliente)
                    continue
                else:
                    #nombre cliente encaja con socket cliente, se saca de la lista de nombres si es que hay espacio
                    self.clientes.append(socket_cliente)
                    self.nombre_clientes.append(NOMBRES.pop(0))
                    print(f"Se conecto {self.nombre_clientes[-1]}")

                    #creamos un thread para manejar al cliente
                    thread_cliente = Thread(target=self.manejar_clientes, args=(socket_cliente, direccion_cliente), daemon=True)
                    thread_cliente.start()
            except ConnectionError:
                print("Error al aceptar cliente")

   
    def manejar_clientes(self, socket_cliente, direccion_cliente):
        #le enviamos al cliente su nombre:
        self.broadcast_mensaje_especifico(socket_cliente, ("Nombre:", self.nombre_clientes[-1]))
        self.broadcast_mensaje_general(("Jugadores:", self.nombre_clientes))
    
        while True:
            try:
                message = socket_cliente.recv(1024).decode()
                if message:
                    print(f"Recibimos el mensaje: {message}")
                    self.broadcast(message, socket_cliente)
            except ConnectionResetError:
                self.clientes.remove(socket_cliente)
                nombre_cliente = self.nombre_clientes[self.clientes.index(socket_cliente)]
                self.nombre_clientes.remove(nombre_cliente)
                print(f"Se desconectó el cliente {nombre_cliente}.")
                self.broadcast_mensaje_general(f"El cliente {nombre_cliente} se ha desconectado.")
                break


    def broadcast_mensaje_especifico(self, socket_cliente, mensaje):
        bytes_mensaje = encriptar_y_codificar(mensaje, N_PONDERADOR)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="big")
        socket_cliente.send(largo_mensaje)
        socket_cliente.send(bytes_mensaje)


    
    def broadcast_mensaje_general(self, mensaje):
        bytes_mensaje = encriptar_y_codificar(mensaje, N_PONDERADOR)
        largo_mensaje = bytes_mensaje[:4]
        for cliente in self.clientes:
            cliente.send(largo_mensaje)
            cliente.send(bytes_mensaje)
        
        
        

        