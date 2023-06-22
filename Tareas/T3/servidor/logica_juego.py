import json
import time
import random

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    NOMBRE_1 = parametros["id_1"]
    NOMBRE_2 = parametros["id_2"]
    NOMBRE_3 = parametros["id_3"]
    NOMBRE_4 = parametros["id_4"]
    N_PONDERADOR = int(parametros["N_PONDERADOR"])
    NUMERO_JUGADORES = int(parametros["NUMERO_JUGADORES"])
    NUMERO_VIDAS = int(parametros["NUMERO_VIDAS"])
    VALOR_PASO = int(parametros["VALOR_PASO"])

NOMBRES = [NOMBRE_1, NOMBRE_2, NOMBRE_3, NOMBRE_4]


class Jugador:
    def __init__(self, nombre, socket):
        self.nombre = nombre
        self.socket = socket
        self.vidas = NUMERO_VIDAS
        self.dados_cambiados = False #para saber si ya cambio los dados
        self.pasar = False #para saber si pasó en el turno anterior
        self.mano = list()

    def cambiar_dados(self):
        self.dados_cambiados = True
        self.mano = list()
        for _ in range(2):
            dado = random.randint(1, 6)
            self.mano.append(dado)

    def __repr__(self):
        return f"{self.nombre}"
    
    def __str__(self):
        return f"{self.nombre} con mano {self.mano} y {self.vidas} vidas"
    
    @property
    def valor_mano(self):
        return sum(self.mano)
    
class Juego:
    def __init__(self, nombre_jugadores: list, sockets_jugadores: list):
        self.jugadores = list()
        self.turno = 0 #contador de turno
        self.count = 0 #contador de las apuestas
        for indice_jugador in range(len(nombre_jugadores)): #creamos los jugadores
            jugador = Jugador(nombre_jugadores[indice_jugador], sockets_jugadores[indice_jugador])
            self.jugadores.append(jugador)
        #randomizamos el orden de los jugadores para la primera mano
        numero_random = random.randint(0, len(self.jugadores) - 1)
        self.jugadores = self.jugadores[numero_random:] + self.jugadores[:numero_random]
        self.shuffle_dados_general()

    def shuffle_dados_general(self):
        for jugador in self.jugadores:
            jugador.mano = list()
            for _ in range(2):
                dado = random.randint(1, 6)
                jugador.mano.append(dado)

    def shuffle_dados_jugador(self, jugador):
        for _ in range(2):
            dado = random.randint(1, 6)
            jugador.mano.append(dado)
        
    
    def jugar_turno(self, accion, valor = None):
        numero_jugador = self.turno % len(self.jugadores) #numero de jugador que le toca jugar
        self.jugadores[numero_jugador].mintiendo = False  #asumimos que el jugador no miente
        if accion == "valor": #el jugador subio el valor
            if valor > 12 or valor <= self.count:
                pass
            else:
                self.count = valor
                if valor > self.jugadores[numero_jugador].valor_mano:
                    self.jugadores[numero_jugador].mintiendo = True
                    self.log(F"el jugador {self.jugadores[numero_jugador].nombre} mintio")
                self.turno += 1


        elif accion == "cambiar":
            self.cambiar_dados()

        elif accion == "pasar turno":
            if self.jugador_en_turno.valor_mano != VALOR_PASO:
                self.jugadores[numero_jugador].mintiendo = True
                self.log(F"el jugador {self.jugadores[numero_jugador].nombre} mintio")
            else:
                self.jugador_en_turno.mintiendo = False
            
            self.turno += 1
        
        elif accion == "dudar": #ARREGLAR ESTO QUE ALGO PASA
            #checkeamos si el jugador anterior mintio
            if self.jugador_anterior.mintiendo:
                self.jugador_anterior.vidas -= 1
                self.log(F"el jugador {self.jugador_anterior.nombre} perdio una vida jujuju")
                self.turno - 1 #lo ocuparemos en el servidor para saber si el dudo fue correcto o erroneo
            else:
                self.jugador_en_turno.vidas -= 1
                self.log(F"el jugador {self.jugador_en_turno.nombre} perdio una vida pq no le achunto")
                self.turno += 1

    def nueva_ronda(self):
        self.jugadores_muertos = 0
        #vemos si algun jugador perdio. Si es asi, lo eliminamos
        for jugador in self.jugadores:
            if jugador.vidas == 0:
                self.jugadores.remove(jugador)
                self.jugadores_muertos += 1
            jugador.dados_cambiados = False
        #elegimos quien parte la ronda
        self.turno = 0
        self.count = 0
        self.shuffle_dados_general()
        numero_random = random.randint(0, len(self.jugadores) - 1)
        self.jugadores = self.jugadores[numero_random:] + self.jugadores[:numero_random]

    def checkear_ganador(self):
        if len(self.jugadores) - self.jugadores_muertos == 0:
            return self.jugadores[0]
        else:
            return False
        
    def jugador_desconectado(self, jugador):
        for jugador in self.jugadores:
            if jugador.nombre == jugador:
                jugador.vidas = 0
        self.jugadores.remove(jugador)
        


    
    @property
    def jugador_en_turno(self):
        return self.jugadores[self.turno % len(self.jugadores)]
    
    @property
    def jugador_anterior(self):
        return self.jugadores[(self.turno - 1) % len(self.jugadores)]
    
    def log(self, mensaje: str):
        print("\n|" + mensaje.center(80, " ") + "|\n")

        

    


