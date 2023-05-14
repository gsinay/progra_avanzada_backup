from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from parametros import (ANCHO_GRILLA, LARGO_GRILLA)
import os
import random
from parametros import (CANTIDAD_VIDAS, FANTASMAS_HORIZONTALES, FANTASMAS_VERTICALES, 
                        FUEGOS, ROCAS, MURALLAS, MIN_VELOCIDAD, MAX_VELOCIDAD)
from models_elementos import Luigi, FantasmaHorizontal, FantasmaVertical
import sys
import time


class Juego_constructor(QObject):

    senal_error_agregar_elemento = pyqtSignal(str)
    senal_check_partir = pyqtSignal(bool, str)
    senal_elemento_agregado = pyqtSignal(str, tuple)
    senal_partir = pyqtSignal(list)
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
        print(posicion, nombre_elemento)
        if len(self.list[posicion[0]-1][posicion[1]-1]) != 0:
            self.senal_error_agregar_elemento.emit("Ya hay un elemento en esa posición")
        elif getattr(self, nombre_elemento) == 0:
            self.senal_error_agregar_elemento.emit("No quedan elementos de ese tipo")
        else:
            self.list[posicion[0]-1][posicion[1]-1].append(nombre_elemento)
            print(f"quedan {getattr(self, nombre_elemento)} {nombre_elemento}")
            self.senal_elemento_agregado.emit(nombre_elemento, posicion)
            setattr(self, nombre_elemento, getattr(self, nombre_elemento)-1)
            print(f"Se agregó {nombre_elemento} en la posición {posicion}. quedan {getattr(self, nombre_elemento)} {nombre_elemento}")
            
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
            self.senal_partir.emit(self.list)#esta se conecta al back
            self.senal_partir_ventana_juego.emit(self.list, username) #esta se conecta al front
            

class Juego(QWidget):
    
    senal_mover_luigi = pyqtSignal(tuple, str)
    senal_armar_front_inicial = pyqtSignal(list)
    senal_mover_fantasma = pyqtSignal(tuple, str, QThread)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threads = {}
        self.senal_mover_fantasma.connect(self.mover_fantasma)
    def partir(self, grilla): #este metodo parte el juego desde el moodo constructor. COMPLETAR!
        self.grilla = grilla
        self.crear_caracteres()
        

    def armar_grilla_backend(self):
        self.grilla = [[] for i in range(LARGO_GRILLA-2)]
        for sub_lista in self.grilla:
            for elemento in range(ANCHO_GRILLA-2):
                sub_lista.append([])
    
    def poblar_grilla_backend(self, nombre_archivo): #CAMBIAR POR CLASES CUANDO ESTEN LISTAS
        self.armar_grilla_backend()
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
                    print(f"Se creó Luigi en la posición {fila, columna}")
                #elif self.grilla[fila][columna] == ["roca"]:
                    #self.Roca_juego = Roca((fila, columna))
               # elif self.grilla[fila][columna] == ["pared"]:
                   # self.Pared_juego = Pared((fila, columna))
                #elif self.grilla[fila][columna] == ["estrella"]:
                    #self.Estrella_juego = Estrella((fila, columna))
                elif self.grilla[fila][columna] == ["fantasma_horizontal"]:
                    elemento =  FantasmaHorizontal(self.senal_mover_fantasma, (fila, columna))
                    self.threads_fantasmas.add(elemento)
                elif self.grilla[fila][columna] == ["fantasma_vertical"]:
                    elemento = FantasmaVertical(self.senal_mover_fantasma, (fila, columna))
                    self.threads_fantasmas.add(elemento)
               # elif self.grilla[fila][columna] == ["fuego"]:
                    #self.Fuego_juego = Fuego((fila, columna))
        #conectar senñales de los fantasmas
        for thread in self.threads_fantasmas:
            print(thread)
            thread.start()
        
    def mover_fantasma(self, posicion, direccion, thread):
        print(ANCHO_GRILLA - 3)
        print(posicion[1])
        if direccion == "derecha":
            if posicion[1] == ANCHO_GRILLA - 3:
                thread.direccion = "izquierda"
                print("cambio de direccion")

            elif self.grilla[posicion[0]][posicion[1] + 1] == ["pared"] or self.grilla[posicion[0]][posicion[1] + 1] == ["roca"]:
                thread.direccion = "izquierda"
            elif self.grilla[posicion[0]][posicion[1] + 1] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_horizontal")
            else:
                print(self.grilla)
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_horizontal")
                self.grilla[posicion[0]][posicion[1] + 1].append("fantasma_horizontal")
                print(self.grilla)
                thread.posicion = (posicion[0], posicion[1] + 1)

        elif direccion == "izquierda":
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

        if direccion == "abajo":
            if posicion[0] == LARGO_GRILLA - 3:
                thread.direccion = "arriba"
                print("cambio de direccion")

            elif self.grilla[posicion[0] + 1 ][posicion[1]] == ["pared"] or self.grilla[posicion[0]+ 1][posicion[1]] == ["roca"]:
                thread.direccion = "arriba"
            elif self.grilla[posicion[0] + 1][posicion[1]] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
            else:
                print(self.grilla)
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
                self.grilla[posicion[0] +1][posicion[1]].append("fantasma_vertical")
                print(self.grilla)
                thread.posicion = (posicion[0] +  1, posicion[1])

        elif direccion == "arriba":
            if posicion[0] == 0:
                thread.direccion = "abajo"
                print("cambio de direccion")

            elif self.grilla[posicion[0] -1 ][posicion[1]] == ["pared"] or self.grilla[posicion[0] - 1][posicion[1]] == ["roca"]:
                thread.direccion = "arriba"
            elif self.grilla[posicion[0] - 1][posicion[1]] == ["fuego"]:
                thread.vivo = False
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
            else:
                print(self.grilla)
                self.grilla[posicion[0]][posicion[1]].remove("fantasma_vertical")
                self.grilla[posicion[0] - 1][posicion[1]].append("fantasma_vertical")
                print(self.grilla)
                thread.posicion = (posicion[0] - 1, posicion[1])
        self.senal_armar_front_inicial.emit(self.grilla)
        
    

    def tecla_presionada(self, tecla):
        if tecla.lower() == "w":
            if self.Luigi_juego.posicion[0] != 1:
                self.actualizar_grilla(tecla.lower()) #actualizar se encarga de actualizar grilla backend
        elif tecla.lower() == "d":
            if self.Luigi_juego.posicion[1] != ANCHO_GRILLA - 2:
                self.actualizar_grilla(tecla.lower())
        elif tecla.lower() == "a":
             if self.Luigi_juego.posicion[1] != 1:
                self.actualizar_grilla(tecla.lower())
        elif tecla.lower() == "s":
            if self.Luigi_juego.posicion[0] != LARGO_GRILLA - 2:
                self.actualizar_grilla(tecla.lower())
        else:
            pass

    def actualizar_grilla(self, direccion):
        if direccion == "w":
            self.grilla[self.Luigi_juego.posicion[0]-1][self.Luigi_juego.posicion[1]-1].remove("luigi")
            self.grilla[self.Luigi_juego.posicion[0]-2][self.Luigi_juego.posicion[1]-1].append("luigi")
            self.Luigi_juego.posicion = (self.Luigi_juego.posicion[0]-1, self.Luigi_juego.posicion[1])
            self.senal_mover_luigi.emit(self.Luigi_juego.posicion, "arriba")
        elif direccion == "d":
            self.grilla[self.Luigi_juego.posicion[0]-1][self.Luigi_juego.posicion[1]-1].remove("luigi")
            self.grilla[self.Luigi_juego.posicion[0]-1][self.Luigi_juego.posicion[1]].append("luigi")
            self.Luigi_juego.posicion = (self.Luigi_juego.posicion[0], self.Luigi_juego.posicion[1]+1)
            self.senal_mover_luigi.emit(self.Luigi_juego.posicion, "derecha")
        elif direccion == "a":
            self.grilla[self.Luigi_juego.posicion[0]-1][self.Luigi_juego.posicion[1]-1].remove("luigi")
            self.grilla[self.Luigi_juego.posicion[0]-1][self.Luigi_juego.posicion[1]-2].append("luigi")
            self.Luigi_juego.posicion = (self.Luigi_juego.posicion[0], self.Luigi_juego.posicion[1]-1)
            self.senal_mover_luigi.emit(self.Luigi_juego.posicion, "izquierda")
        elif direccion == "s":
            self.grilla[self.Luigi_juego.posicion[0]-1][self.Luigi_juego.posicion[1]-1].remove("luigi")
            self.grilla[self.Luigi_juego.posicion[0]][self.Luigi_juego.posicion[1]-1].append("luigi")
            self.Luigi_juego.posicion = (self.Luigi_juego.posicion[0]+1, self.Luigi_juego.posicion[1])
            self.senal_mover_luigi.emit(self.Luigi_juego.posicion, "abajo")

            

        
                    

        
        
