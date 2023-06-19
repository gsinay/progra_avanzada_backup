import json
import time
import random

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    NOMBRES = parametros["NOMBRES"]
    N_PONDERADOR = int(parametros["N_PONDERADOR"])
    NUMERO_JUGADORES = int(parametros["NUMERO_JUGADORES"])
    NUMERO_VIDAS = int(parametros["NUMERO_VIDAS"])

class Jugador:
    def __init__(self, nombre, socket):
        self.nombre = nombre
        self.socket = socket
        self.vidas = NUMERO_VIDAS
        self.dados_cambiados = False #para saber si ya cambio los dados
        self.pasar = False #para saber si pasó en el turno anterior
        self.mano = set()

    def __repr__(self):
        return f"{self.nombre}"
    
    def __str__(self):
        return f"{self.nombre} con mano {self.mano} y {self.vidas} vidas"
    
class Juego:
    def __init__(self, nombre_jugadores: list, sockets_jugadores: list):
        self.jugadores = list()
        self.turno = 0 #contador de turno
        self.count = 0 #contador de las apuestas
        for indice_jugador in range(len(nombre_jugadores)): #creamos los jugadores
            jugador = Jugador(nombre_jugadores[indice_jugador], sockets_jugadores[indice_jugador])
            self.jugadores.append(jugador)
        #randomizamos el orden de los jugadores
        random.shuffle(self.jugadores)

    
    def jugar_turno(self, accion):
        numero_jugador = self.turno % len(self.jugadores) #numero de jugador que le toca jugar
        if accion == "apostar":
            self.subir_apuesta(accion, numero_jugador)
        elif accion == "cambiar":
            self.cambiar_dados()
        elif accion == "pasar":
            self.pasar()
        

    def subir_apuesta(self, apuesta, numero_jugador):
        if apuesta >= self.count and apuesta <= 12: #si la apuesta es mayor a la anterior y menor a 12
            self.count = apuesta
            return True
        else:
            return False
        
    @property
    def jugador_en_turno(self):
        return self.jugadores[self.turno % len(self.jugadores)]

    


