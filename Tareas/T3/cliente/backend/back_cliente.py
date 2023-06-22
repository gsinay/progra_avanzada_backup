from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
import os
import sys
import json
import socket
import threading
import time
from Scripts.cripto import encriptar_y_codificar, decodificar_y_desencriptar
import pickle

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    N_PONDERADOR = int(parametros["N_PONDERADOR"])


class LogicaCliente(QObject):
    senal_actualizar_waiting_room = pyqtSignal(list)
    senal_servidor_caido = pyqtSignal()
    senal_server_lleno = pyqtSignal()
    senal_jugador_desconectado = pyqtSignal(list)
    senal_error_partir_juego = pyqtSignal(str)
    senal_condiciones_ok = pyqtSignal(str, list)
    senal_repaint = pyqtSignal(list, bool, bool)
    senal_turno = pyqtSignal(bool, list)
    senal_paint_dados = pyqtSignal(list)
    senal_error_turno = pyqtSignal(str)
    senal_actualizar_vidas = pyqtSignal(list)
    senal_ganador = pyqtSignal(str)
    senal_jugador_desconectado_en_juego = pyqtSignal(str)
    senal_error_cambiar_dados = pyqtSignal()

    def __init__(self, host, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = host
        self.port = port
        self.nombre = None
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.standby = False
        self.estuvo_en_standby = False
        self.jugando = False
        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Conectado al servidor")
            #generar thread del cliente
            thread_cliente = threading.Thread(target=self.recibir_datos)
            thread_cliente.start()

        except ConnectionRefusedError:
            print("No se pudo conectar al servidor, intente nuevamente")
        
    def recibir_datos(self):
        funcionando = True
        while funcionando:
            try:
                mensaje = self.recibir_mensaje()
                mensaje_decodificado = decodificar_y_desencriptar(mensaje, N_PONDERADOR)
                #es el primer mensaje que recibimos automaticamente con nuestro nombre en caso que hayan espacios de jugadores
                if self.nombre == None and mensaje_decodificado[0].lower() == "nombre:" :  
                    self.nombre = mensaje_decodificado[1]
                    print(f"Mi nombre es {self.nombre}")
                    self.standby = False
                else:
                    if mensaje_decodificado[0].lower() == "jugadores:": #si recibimos jugador nuevo actualizamos el waiting room
                        self.actualizar_waiting_room(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "servidor lleno": #si el jugador llega a una sala llena. 
                        self.actualizar_waiting_room(mensaje_decodificado[1], error = "server lleno")
                        self.standby = True
                        self.estuvo_en_standby = True
                    elif "desconectado:" in mensaje_decodificado[0].lower(): #si se desconecta un jugador
                        print(f"client disconnected")
                        self.actualizar_waiting_room(mensaje_decodificado[1], error = "disconnected")
                    elif mensaje_decodificado[0].lower() == "faltan jugadores":
                        self.senal_error_partir_juego.emit("faltan jugadores")
                    elif mensaje_decodificado[0].lower() == "partir juego":
                        self.partir_juego(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "dados:":
                        print(f"recibi los dados {mensaje_decodificado[1]}")
                        self.senal_paint_dados.emit(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "turno de:":
                        self.jugador_jugando = mensaje_decodificado[1]
                        print(f"turno de {self.jugador_jugando}")
                    elif mensaje_decodificado[0].lower() == "valor actual:":
                        self.valor_actual = mensaje_decodificado[1]
                    elif mensaje_decodificado[0].lower() == "turno actual:":
                        self.turno_actual = mensaje_decodificado[1]
                        self.jugar_turno([self.jugador_jugando, self.valor_actual, self.turno_actual])
                    elif mensaje_decodificado[0].lower() == "error_jugada:":
                        self.senal_error_turno.emit(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "pierde_vida:":
                        print(f"recibi pierde vida {mensaje_decodificado[1]}")
                        self.actualizar_vidas_front(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "ganador:":
                        self.senal_ganador.emit(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "desconectado_en_juego:":
                        if self.standby == False:
                            self.senal_jugador_desconectado_en_juego.emit(mensaje_decodificado[1])
                    elif mensaje_decodificado[0].lower() == "error_jugada:" and mensaje_decodificado[1] == "ya cambiaste los dados":
                        self.senal_error_cambiar_dados.emit()
                    if mensaje_decodificado[0].lower() == "repaint:":
                        self.actualizar_waiting_room(mensaje_decodificado[1], error = "repaint")
                        print("repainting window")

            except ConnectionResetError:
                print("Se desconectó el servidor.")
                funcionando = False
            except ConnectionAbortedError:
                print("Se desconectó el servidor.")
                funcionando = False
            except ZeroDivisionError:
                print("Se desconectó el servidor.")
                funcionando = False
            except ConnectionError:
                print("Se desconectó el servidor.")
                funcionando = False
        
        self.senal_servidor_caido.emit()
        self.socket_cliente.close()
        
    
    def recibir_mensaje(self):
        largo_mensaje = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_mensaje, byteorder="big")
        mensaje = self.socket_cliente.recv(largo_mensaje)
        return mensaje
        
    def actualizar_waiting_room(self, nombres, error = False):
        if not self.jugando:
            time.sleep(1)
            self.senal_actualizar_waiting_room.emit(nombres)
            if error == "server lleno":
                self.senal_server_lleno.emit()
            elif error == "disconnected":
                self.senal_jugador_desconectado.emit(nombres)
            elif error == "repaint":
                if self.standby == True:
                    self.standby = False
                    self.senal_repaint.emit(nombres, True, self.estuvo_en_standby)
                else:
                    self.senal_repaint.emit(nombres, False, self.estuvo_en_standby)

    def enviar_mensaje(self, mensaje):
        bytes_mensaje = encriptar_y_codificar(mensaje, N_PONDERADOR)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="big")
        self.socket_cliente.send(largo_mensaje)
        self.socket_cliente.send(bytes_mensaje)
    
    def check_partir_juego(self):
        mensaje = "partir juego"
        self.enviar_mensaje(mensaje)

    def partir_juego(self, nombres):
        #reordenamos los nombres para que el jugador propio sea el primero en la lista 
        # (de forma de mantener integridad del circulo en la ventana de juego)
        indice_nombre = nombres.index(self.nombre)
        nombres = nombres[indice_nombre:] + nombres[:indice_nombre]
        self.senal_condiciones_ok.emit(self.nombre, nombres)
        self.jugando = True

    def jugar_turno(self, info_de_turno):
        if info_de_turno[0] == self.nombre:
            self.senal_turno.emit(True, info_de_turno)
        else:
           self.senal_turno.emit(False, info_de_turno)

    def anunciar_valor(self, valor):
        print(f"en mi turno anuncie este valor: {valor}")
        self.enviar_mensaje(("valor", valor))

    def pasar_turno(self):
        self.enviar_mensaje(("pasar turno", self.nombre))

    def dudar(self):
        self.enviar_mensaje(("dudar", self.nombre))

    def actualizar_vidas_front(self, info_vidas):
        self.senal_actualizar_vidas.emit(info_vidas)

    def disconnect(self): #el disconnect se considera como un "error", causa crash en el cliente y el servidor lo atrapa
        raise ConnectionError
    
    def cambiar_dados(self):
        self.enviar_mensaje(("cambiar dados", self.nombre))
            

if __name__ == "__main__":
    cliente_prueba = LogicaCliente("localhost", 9999)

