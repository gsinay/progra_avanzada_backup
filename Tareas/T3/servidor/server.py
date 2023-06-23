import socket
from threading import Thread, Lock
import sys
import json
from Scripts.cripto import encriptar_y_codificar, decodificar_y_desencriptar
from logica_juego import Juego

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    NOMBRE_1 = parametros["id_1"]
    NOMBRE_2 = parametros["id_2"]
    NOMBRE_3 = parametros["id_3"]
    NOMBRE_4 = parametros["id_4"]
    N_PONDERADOR = int(parametros["N_PONDERADOR"])
    NUMERO_JUGADORES = int(parametros["NUMERO_JUGADORES"])

NOMBRES = [NOMBRE_1, NOMBRE_2, NOMBRE_3, NOMBRE_4]



class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientes = list()
        self.nombre_clientes = list()
        self.clientes_standby = list()
        self.jugando = False
        self.lock = Lock()
        self.armar_servidor()

    def armar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_servidor.bind((self.host, self.port))
        except OSError:
            self.log("No se pudo levantar el servidor")
            sys.exit()
        self.socket_servidor.listen()
        self.escuchar_clientes()
    
    def escuchar_clientes(self):
        while True:
            try:
                self.log("Esperando clientes")
                socket_cliente, direccion_cliente = self.socket_servidor.accept()
                self.log(f"Se conecto un cliente desde {direccion_cliente}")

                #si la sala esta llena se le avisa al cliente y se deja en standby
                if len(self.nombre_clientes) == NUMERO_JUGADORES:
                    self.broadcast_mensaje_especifico(socket_cliente, ("Servidor lleno", self.nombre_clientes))
                    self.log("Se le dijo al cliente que la sala esta llena")
                    self.clientes_standby.append(socket_cliente)
                    continue
                else:
                    #nombre cliente encaja con socket cliente, se saca de la lista de nombres si es que hay espacio
                    self.clientes.append(socket_cliente)
                    self.nombre_clientes.append(NOMBRES.pop(0))
                    self.log(f"Se le asigno el nombre {self.nombre_clientes[-1]}")

                    #creamos un thread para manejar al cliente
                    thread_cliente = Thread(target=self.manejar_clientes, args=(socket_cliente, direccion_cliente), daemon=True)
                    thread_cliente.start()
            except ConnectionError:
                self.log("Error al conectar cliente")

   
    def manejar_clientes(self, socket_cliente, direccion_cliente):
        #le enviamos al cliente su nombre:
        self.broadcast_mensaje_especifico(socket_cliente, ("Nombre:", self.nombre_clientes[-1]))
        self.broadcast_mensaje_general(("Jugadores:", self.nombre_clientes))
        nombre = self.nombre_clientes[-1]
    
        try:
            while True:
                mensaje = self.recibir_mensaje(socket_cliente)
                if mensaje:
                    mensaje_decodificado = decodificar_y_desencriptar(mensaje, N_PONDERADOR)
                    self.log(f"Recibido: {mensaje_decodificado}. Enviado por {nombre}")
                    if mensaje_decodificado == "partir juego":
                        thread_juego = Thread(target=self.partir_juego, args=(socket_cliente,), daemon=True)
                        thread_juego.start()
                    elif type(mensaje_decodificado) is tuple:
                        if mensaje_decodificado[0] == "valor":
                            self.log(f"Se recibio la accion {mensaje_decodificado[1]} de {self.juego.jugador_en_turno.nombre}")
                            self.accionar_turno("valor", mensaje_decodificado[1])
                        elif mensaje_decodificado[0] == "pasar turno":
                            self.log(f"Se recibio la accion {mensaje_decodificado[0]} de {self.juego.jugador_en_turno.nombre}")
                            self.accionar_turno("pasar turno")
                        elif mensaje_decodificado[0] == "dudar":
                            self.log(f"Se recibio la accion {mensaje_decodificado[0]} de {self.juego.jugador_en_turno.nombre}")
                            self.accionar_turno("dudar")
                        elif mensaje_decodificado[0] == "cambiar dados":
                            self.cambiar_dados(mensaje_decodificado[1], socket_cliente) 
                else:
                    raise ConnectionResetError
        except ConnectionResetError:
            nombre_cliente = self.nombre_clientes[self.clientes.index(socket_cliente)]
            self.clientes.remove(socket_cliente)
            self.nombre_clientes.remove(nombre_cliente)
            NOMBRES.append(nombre_cliente)
            self.log(f"Se desconectó el cliente {nombre_cliente}.")
            self.log(f"Quedan {len(self.clientes)} clientes conectados.")
            self.log(f"Los jugadores que quedan son {self.nombre_clientes} en las direcciones {self.clientes}")
            self.broadcast_mensaje_general((f"desconectado: {nombre_cliente}", self.nombre_clientes))
            if self.jugando == False and len(self.clientes_standby) > 0:
                self.clientes.append(self.clientes_standby.pop(0))
                self.nombre_clientes.append(NOMBRES.pop(0))
                self.log(f"Se le asigno el nombre {self.nombre_clientes[-1]} a un cliente en standby")
                self.broadcast_mensaje_especifico(self.clientes[-1], ("Nombre:", self.nombre_clientes[-1]))
                self.broadcast_mensaje_general(("repaint:", self.nombre_clientes))
                thread_cliente = Thread(target=self.manejar_clientes, args=(self.clientes[-1], direccion_cliente), daemon=True)
                thread_cliente.start()
            elif self.jugando == True:
                print("Se desconecto un jugador en medio de la partida")
                self.kick_jugador(nombre_cliente)
                self.broadcast_mensaje_general(("desconectado_en_juego:", nombre_cliente))

        socket_cliente.close()


    def broadcast_mensaje_especifico(self, socket_cliente, mensaje):
        bytes_mensaje = encriptar_y_codificar(mensaje, N_PONDERADOR)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="big")
        socket_cliente.send(largo_mensaje)
        socket_cliente.send(bytes_mensaje)


    
    def broadcast_mensaje_general(self, mensaje):
        bytes_mensaje = encriptar_y_codificar(mensaje, N_PONDERADOR)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="big")
        for cliente in self.clientes:
            cliente.send(largo_mensaje)
            cliente.send(bytes_mensaje)

    def recibir_mensaje(self, socket_cliente):
        largo_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_mensaje, byteorder="big")
        mensaje = socket_cliente.recv(largo_mensaje)
        return mensaje
    
    def partir_juego(self, socket_cliente):
        if len(self.clientes) == NUMERO_JUGADORES:
            self.broadcast_mensaje_general(("Partir juego", self.nombre_clientes))
            self.juego = Juego(self.nombre_clientes, self.clientes) #instanciamos un juego
            self.jugando = True
            self.actualizar_cliente_y_front()
            self.enviar_dados_clientes()
            #le enviamos los dados a cada cliente

        elif len(self.clientes) <= NUMERO_JUGADORES:
            self.broadcast_mensaje_especifico(socket_cliente, ("Faltan Jugadores", self.nombre_clientes))

    def accionar_turno(self, accion, cantidad = None):
        error = False
        if cantidad is not None:
            cantidad = int(cantidad)
        if accion == "valor": #vemos que el valor sea valido
            if cantidad > 12 or cantidad <= self.juego.count:
                error = True
                razon = "valor invalido"
            else:
                self.juego.jugar_turno("valor", cantidad)
        elif accion == "pasar turno": 
            self.juego.jugar_turno("pasar turno")
        elif accion == "dudar":
            if self.juego.turno == 0: #si es el primer turno, no se puede dudar
                error = True
                razon = "no se puede dudar en el primer turno"
            else:
                self.juego.jugar_turno("dudar")
                self.broadcast_mensaje_general(("pierde_vida:", [self.juego.jugador_anterior.nombre, self.juego.jugador_anterior.vidas]))
                self.juego.nueva_ronda()
                self.checkear_ganador()
                self.enviar_dados_clientes()
        if not error:
            self.actualizar_cliente_y_front()
        else:
            self.broadcast_mensaje_especifico(self.juego.jugador_en_turno.socket, ("error_jugada:", razon))
    
    def kick_jugador(self, nombre):
        with self.lock:
            self.juego.jugador_desconectado(nombre)
            self.juego.nueva_ronda()
            self.checkear_ganador()
            self.enviar_dados_clientes()
            self.actualizar_cliente_y_front()

    def actualizar_cliente_y_front(self):
        #le señalamos al cliente la informacion
        self.broadcast_mensaje_general(("turno de:",  (self.juego.jugador_en_turno.nombre)))
        self.broadcast_mensaje_general(("valor actual:", self.juego.count))
        self.broadcast_mensaje_general(("turno actual:", self.juego.turno))

    def cambiar_dados(self, nombre_cliente, socket_cliente):
        for jugador in self.juego.jugadores:
            if jugador.nombre == nombre_cliente and jugador.dados_cambiados == False:
                jugador.cambiar_dados()
                self.log(f"Se le cambiaron los dados a {jugador.nombre} en la direccion {jugador.socket}")
                self.broadcast_mensaje_especifico(socket_cliente, ("dados:", jugador.mano))
                break
            elif jugador.nombre == nombre_cliente and jugador.dados_cambiados == True:
                self.broadcast_mensaje_especifico(socket_cliente, ("error_jugada:", "Ya cambiaste los dados"))
                break
    

    def enviar_dados_clientes(self):
        for jugador in self.juego.jugadores:
            self.log(f"Se le envio los dados {jugador.mano} a {jugador.nombre} en la direccion {jugador.socket}")
            self.broadcast_mensaje_especifico(jugador.socket, ("dados:", jugador.mano))

    def checkear_ganador(self):
        ganador = self.juego.checkear_ganador()
        if ganador == False:
            self.log("No hay ganador")
        else:
            self.jugando = False
            self.broadcast_mensaje_general(("ganador:", ganador.nombre))
            self.log(f"El ganador es {ganador.nombre}")
                

    def log(self, mensaje: str):
        print("\n|" + mensaje.center(80, " ") + "|\n")

        
        
        

        