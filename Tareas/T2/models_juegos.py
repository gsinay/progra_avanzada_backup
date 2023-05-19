from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from parametros import (ANCHO_GRILLA, LARGO_GRILLA)
import os
import random
from parametros import (CANTIDAD_VIDAS, FANTASMAS_HORIZONTALES, FANTASMAS_VERTICALES, 
                        FUEGOS, ROCAS, MURALLAS, MIN_VELOCIDAD, MAX_VELOCIDAD, TIEMPO_CUENTA_REGRESIVA,
                        MULTIPLICADOR_PUNTAJE)
from models_elementos import Luigi, FantasmaHorizontal, FantasmaVertical
import math

class Juego_constructor(QObject):

    senal_error_agregar_elemento = pyqtSignal(str)
    senal_check_partir = pyqtSignal(bool, str)
    senal_elemento_agregado = pyqtSignal(str, tuple)
    senal_partir = pyqtSignal(list, str)
    senal_partir_ventana_juego = pyqtSignal(list, str)
    def __init__(self):
        super().__init__()
        self.luigi = 1
        self.roca = ROCAS
        self.pared = MURALLAS
        self.estrella = 1
        self.fantasma_horizontal = FANTASMAS_HORIZONTALES
        self.fantasma_vertical = FANTASMAS_VERTICALES
        self.fuego = FUEGOS
        self.armar_grilla_backend()

    def armar_grilla_backend(self):
        self.list = [[] for i in range(LARGO_GRILLA-2)]
        for sub_lista in self.list:
            for elemento in range(ANCHO_GRILLA-2):
                sub_lista.append([])

    def agregar_elemento(self, posicion, nombre_elemento):
        if len(self.list[posicion[0]-1][posicion[1]-1]) != 0:
            self.senal_error_agregar_elemento.emit("Ya hay un elemento en esa posición")
        elif getattr(self, nombre_elemento) == 0:
            self.senal_error_agregar_elemento.emit("No quedan elementos de ese tipo")
        else:
            self.list[posicion[0]-1][posicion[1]-1].append(nombre_elemento)
            self.senal_elemento_agregado.emit(nombre_elemento, posicion)
            setattr(self, nombre_elemento, getattr(self, nombre_elemento)-1)
            
    def limpiar_grilla(self):
        self.armar_grilla_backend()
        self.luigi = 1
        self.roca = ROCAS
        self.pared = MURALLAS
        self.estrella = 1
        self.fantasma_horizontal = FANTASMAS_HORIZONTALES
        self.fantasma_vertical = FANTASMAS_VERTICALES
        self.fuego = FUEGOS

    def empezar_juego(self, username):
        if self.luigi == 1 or self.estrella == 1:
            self.senal_check_partir.emit(False, "No se puede empezar el juego sin Luigi o la estrella")
        else:
            self.senal_check_partir.emit(True, "Sucess")
            self.senal_partir.emit(self.list, username)#esta se conecta al back
            self.senal_partir_ventana_juego.emit(self.list, username) #esta se conecta al front
            

class Juego(QWidget):
    
    senal_mover_luigi = pyqtSignal(tuple, str)
    senal_armar_front_inicial = pyqtSignal(list)
    senal_mover_fantasma = pyqtSignal(tuple, str, QThread)
    senal_game_over = pyqtSignal(str, str, float)
    senal_actualizar_tiempo = pyqtSignal(int)
    senal_actualizar_vidas = pyqtSignal(int)
    senal_actualizar_boton_pausa = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threads = {}
        self.senal_mover_fantasma.connect(self.mover_fantasma)
        self.game_over = False
        self.game_started = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.timer.start(1000)
        self.tiempo_restante = TIEMPO_CUENTA_REGRESIVA
        self.pausado = False
        self.tiene_estrella = False
        self.booleans = {"k": False, "i": False, "l" : False, "n" : False, "f": False} #cheatchodes


    def partir(self, grilla, username): #este metodo parte el juego desde el moodo constructor. COMPLETAR!
        self.grilla = grilla
        self.username = username
        self.crear_caracteres()
        

    def armar_grilla_backend(self):
        self.grilla = [[] for i in range(LARGO_GRILLA-2)]
        for sub_lista in self.grilla:
            for elemento in range(ANCHO_GRILLA-2):
                sub_lista.append([])
    
    def poblar_grilla_backend(self, nombre_archivo, username): #CAMBIAR POR CLASES CUANDO ESTEN LISTAS
        self.armar_grilla_backend()
        self.username = username
        with open(os.path.join("mapas", nombre_archivo + ".txt"), "r") as archivo:
            lineas = archivo.readlines()
            for linea in range(len(lineas)):
                for caracter in range(len(lineas[linea])):
                    if lineas[linea][caracter] == "L":
                        self.grilla[linea][caracter].append("luigi")
                    elif lineas[linea][caracter] == "R":
                        self.grilla[linea][caracter].append("roca")
                    elif lineas[linea][caracter] == "P":
                        self.grilla[linea][caracter].append("pared")
                    elif lineas[linea][caracter] == "S":
                        self.grilla[linea][caracter].append("estrella")
                    elif lineas[linea][caracter] == "H":
                        self.grilla[linea][caracter].append("fantasma_horizontal")
                    elif lineas[linea][caracter] == "V":
                        self.grilla[linea][caracter].append("fantasma_vertical")
                    elif lineas[linea][caracter] == "F":
                        self.grilla[linea][caracter].append("fuego")
                    else:
                        pass
        self.senal_armar_front_inicial.emit(self.grilla)
        self.crear_caracteres()

    def crear_caracteres(self):
        self.threads_fantasmas = set()
        for fila in range(len(self.grilla)):
            for columna in range(len(self.grilla[fila])):
                if self.grilla[fila][columna] == ["luigi"]:
                    self.Luigi_juego = Luigi((fila, columna))
                elif self.grilla[fila][columna] == ["fantasma_horizontal"]:
                    elemento =  FantasmaHorizontal(self.senal_mover_fantasma, (fila, columna))
                    self.threads_fantasmas.add(elemento)
                elif self.grilla[fila][columna] == ["fantasma_vertical"]:
                    elemento = FantasmaVertical(self.senal_mover_fantasma, (fila, columna))
                    self.threads_fantasmas.add(elemento)
        #conectar senñales de los fantasmas
        for thread in self.threads_fantasmas:
            thread.start()
        self.game_started = True
        
    def mover_fantasma(self, posicion, direccion, thread):
        if direccion == "derecha" and thread.vivo and self.pausado == False:
            if posicion[1] == ANCHO_GRILLA - 3:
                thread.direccion = "izquierda"
            elif self.grilla[posicion[0]][posicion[1] + 1] == ["pared"] or self.grilla[posicion[0]][posicion[1] + 1] == ["roca"]:
                thread.direccion = "izquierda"
            elif self.grilla[posicion[0]][posicion[1] + 1] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_horizontal")
            else:
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_horizontal")
                self.grilla[posicion[0]][posicion[1] + 1].append("fantasma_horizontal")
                thread.posicion = (posicion[0], posicion[1] + 1)

        elif direccion == "izquierda" and thread.vivo and self.pausado == False:
            if posicion[1] == 0:
                thread.direccion = "derecha"
            elif self.grilla[posicion[0]][posicion[1] - 1 ] == ["pared"] or self.grilla[posicion[0]][posicion[1] -1 ] == ["roca"]:
                thread.direccion = "derecha"
            elif self.grilla[posicion[0]][posicion[1] - 1] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_horizontal")
            else:
                
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_horizontal")
                self.grilla[posicion[0]][posicion[1] -1].append("fantasma_horizontal")
                thread.posicion = (posicion[0], posicion[1] - 1)
        self.senal_armar_front_inicial.emit(self.grilla)

        if direccion == "abajo" and thread.vivo and self.pausado == False:
            if posicion[0] == LARGO_GRILLA - 3:
                thread.direccion = "arriba"
            elif self.grilla[posicion[0] + 1 ][posicion[1]] == ["pared"] or self.grilla[posicion[0]+ 1][posicion[1]] == ["roca"]:
                thread.direccion = "arriba"
            elif self.grilla[posicion[0] + 1][posicion[1]] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
            else:
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
                self.grilla[posicion[0] +1][posicion[1]].append("fantasma_vertical")
                thread.posicion = (posicion[0] +  1, posicion[1])

        elif direccion == "arriba" and thread.vivo and self.pausado == False:
            if posicion[0] == 0:
                thread.direccion = "abajo"
            elif self.grilla[posicion[0] -1 ][posicion[1]] == ["pared"] or self.grilla[posicion[0] - 1][posicion[1]] == ["roca"]:
                thread.direccion = "abajo"
            elif self.grilla[posicion[0] - 1][posicion[1]] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
            else:
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
                self.grilla[posicion[0] - 1][posicion[1]].append("fantasma_vertical")
                thread.posicion = (posicion[0] - 1, posicion[1])
        self.senal_armar_front_inicial.emit(self.grilla)
        self.checkear_colisiones()
    

    def tecla_presionada(self, tecla): #esto va a tener muuuchos ifs
        posicion = self.Luigi_juego.posicion
        if tecla.lower() == "w" and self.pausado == False: #luigi se mueve para arriba 
            if posicion[0] != 0:
                if posicion[0] != 1 and self.grilla[posicion[0] - 1][posicion[1]] == ["roca"] and self.grilla[posicion[0] - 2][posicion[1]] == []:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0] - 1][posicion[1]].remove("roca")
                    self.grilla[posicion[0] - 1][posicion[1]].append("luigi") 
                    self.grilla[posicion[0] - 2][posicion[1]].append("roca") 
                    self.Luigi_juego.posicion = (posicion[0]-1, posicion[1]) 
                elif self.grilla[posicion[0] - 1][posicion[1]] == ["pared"]:
                    pass
                else:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0] - 1][posicion[1]].append("luigi") 
                    self.Luigi_juego.posicion = (posicion[0]-1, posicion[1])
        elif tecla.lower() == "d" and self.pausado == False:
            if posicion[1] != ANCHO_GRILLA - 3:
                if posicion[0] != ANCHO_GRILLA - 4 and self.grilla[posicion[0]][posicion[1] + 1] == ["roca"] and self.grilla[posicion[0]][posicion[1] + 2] == []:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0]][posicion[1] + 1].remove("roca")
                    self.grilla[posicion[0]][posicion[1] + 1].append("luigi") 
                    self.grilla[posicion[0]][posicion[1] + 2].append("roca") 
                    self.Luigi_juego.posicion = (posicion[0], posicion[1] + 1) 
                elif self.grilla[posicion[0]][posicion[1] + 1] == ["pared"]:
                    pass
                else:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0]][posicion[1] + 1].append("luigi") 
                    self.Luigi_juego.posicion = (posicion[0], posicion[1] + 1)
        elif tecla.lower() == "a" and self.pausado == False:

             if posicion[1] != 0:
                if posicion[0] != 1  and self.grilla[posicion[0]][posicion[1] - 1] == ["roca"] and self.grilla[posicion[0]][posicion[1] - 2] == []:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0]][posicion[1] - 1].remove("roca")
                    self.grilla[posicion[0]][posicion[1] - 1].append("luigi") 
                    self.grilla[posicion[0]][posicion[1] - 2].append("roca") 
                    self.Luigi_juego.posicion = (posicion[0], posicion[1] - 1) 
                elif self.grilla[posicion[0]][posicion[1] - 1] == ["pared"]:
                    pass
                else:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0]][posicion[1] - 1].append("luigi") 
                    self.Luigi_juego.posicion = (posicion[0], posicion[1] - 1)
        elif tecla.lower() == "s" and self.pausado == False:
            if posicion[0] != LARGO_GRILLA - 3:
                if posicion[0] != LARGO_GRILLA - 4 and self.grilla[posicion[0] + 1][posicion[1]] == ["roca"] and self.grilla[posicion[0] + 2][posicion[1]] == []:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0] + 1][posicion[1]].remove("roca")
                    self.grilla[posicion[0] + 1][posicion[1]].append("luigi") 
                    self.grilla[posicion[0] + 2][posicion[1]].append("roca") 
                    self.Luigi_juego.posicion = (posicion[0] + 1, posicion[1]) 
                elif self.grilla[posicion[0] + 1][posicion[1]] == ["pared"]:
                    pass
                else:
                    self.grilla[posicion[0]][posicion[1]].remove("luigi")
                    self.grilla[posicion[0] + 1][posicion[1]].append("luigi") 
                    self.Luigi_juego.posicion = (posicion[0] + 1, posicion[1])
        elif tecla.lower() == "p":
            self.pausar()
        elif tecla.lower() == "i":
            self.booleans["i"] = True
        elif tecla.lower() == "n" and self.booleans["i"]:
            self.booleans["n"] = True
        elif tecla.lower() == "f" and self.booleans["i"] and self.booleans["n"]:
            self.booleans["f"] = True
            self.timer.stop()
            self.Luigi_juego.vidas = math.inf


        elif tecla.lower() == "g" and self.tiene_estrella:
            for thread in self.threads_fantasmas:
                thread.vivo = False
            if self.booleans["i"] and self.booleans["n"] and self.booleans["f"]:
                self.senal_game_over.emit(self.username, 
                                        "ganaste!!!", 
                                        ((TIEMPO_CUENTA_REGRESIVA * MULTIPLICADOR_PUNTAJE) /
                                        (1)))
            print(self.tiempo_restante)
            print(self.Luigi_juego.vidas)
            self.senal_game_over.emit(self.username, 
                                        "ganaste!!!", 
                                        ((self.tiempo_restante * MULTIPLICADOR_PUNTAJE) /
                                        (1 + CANTIDAD_VIDAS - self.Luigi_juego.vidas)))
        else:
            self.resetear_booleanos()

        self.checkear_colisiones()
        self.senal_armar_front_inicial.emit(self.grilla)
        self.checkear_exito()

    def resetear_booleanos(self):
         for booleano in self.booleans:
                self.booleans[booleano] = False
    
    def checkear_colisiones(self):
        for fila in self.grilla:
            for columna in fila:
                if "luigi" in columna:
                    if "fantasma_vertical" in columna or "fantasma_horizontal" in columna or "fuego" in columna:
                        columna.remove("luigi")
                        self.Luigi_juego.vidas -= 1
                        self.Luigi_juego.posicion = (0,0)
                        self.grilla[0][0].append("luigi")
                        self.senal_armar_front_inicial.emit(self.grilla)
                        self.senal_actualizar_vidas.emit(self.Luigi_juego.vidas)
        if self.Luigi_juego.vidas == 0 and self.game_over == False:
            self.game_over = True
            for thread in self.threads_fantasmas:
                thread.vivo = False
            self.senal_game_over.emit(self.username, "perdiste por falta de vidas", 0 )
        


    def checkear_exito(self):
        for fila in self.grilla:
            for columna in fila:
                if "luigi" in columna and "estrella" in columna:
                    self.tiene_estrella = True
                    columna.remove("estrella")
                    self.senal_armar_front_inicial.emit(self.grilla)

    def actualizar_tiempo(self):
        if self.game_started == True:
            self.tiempo_restante -= 1
            if self.tiempo_restante == 0:
                self.timer.stop()
                self.game_over = True
                for thread in self.threads_fantasmas:
                    thread.vivo = False
                self.senal_game_over.emit(self.username, "perdiste por falta de tiempo", 0)
            self.senal_actualizar_tiempo.emit(self.tiempo_restante)
    
    def pausar(self):
        if self.pausado == False:
            self.pausado = True
            self.timer.stop()
        elif self.pausado == True:
            self.pausado = False
            self.timer.start()
        self.senal_actualizar_boton_pausa.emit(self.pausado)
        
                

    