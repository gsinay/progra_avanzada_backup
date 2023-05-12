from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QPushButton
from PyQt5.QtGui import QPixmap
from parametros import (ANCHO_GRILLA, LARGO_GRILLA)
import os
import random
from parametros import (CANTIDAD_VIDAS, FANTASMAS_HORIZONTALES, FANTASMAS_VERTICALES, 
                        FUEGOS, ROCAS, MURALLAS, MIN_VELOCIDAD, MAX_VELOCIDAD)
import sys


class Juego_constructor(QObject):

    senal_error_agregar_elemento = pyqtSignal(str)
    senal_check_partir = pyqtSignal(bool, str)
    senal_elemento_agregado = pyqtSignal(str, tuple)
    senal_partir = pyqtSignal(list)

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
        print(self.list)

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

    def empezar_juego(self):
        if self.luigi == 1 or self.estrella == 1:
            self.senal_check_partir.emit(False, "No se puede empezar el juego sin Luigi o la estrella")
        else:
            self.senal_check_partir.emit(True, "Sucess")
            self.senal_partir.emit(self.list)


class Juego(QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def grilla_inicial(self):
        pass
        
