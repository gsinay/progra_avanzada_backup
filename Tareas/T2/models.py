from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QPushButton
from PyQt5.QtGui import QPixmap
from parametros import (ANCHO_GRILLA, LARGO_GRILLA)
import os
from parametros import (CANTIDAD_VIDAS, FANTASMAS_HORIZONTALES, FANTASMAS_VERTICALES, 
                        FUEGOS, ROCAS, MURALLAS)
import sys


class Juego_constructor(QObject):

    senal_error_agregar_elemento = pyqtSignal(str)
    senal_elemento_agregado = pyqtSignal(str, tuple)

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
                sub_lista.append(None)

    def agregar_elemento(self, posicion, nombre_elemento):
        print(posicion, nombre_elemento)
        if self.list[posicion[0]-1][posicion[1]-1] != None:
            self.senal_error_agregar_elemento.emit("Ya hay un elemento en esa posición")
        elif getattr(self, nombre_elemento) == 0:
            self.senal_error_agregar_elemento.emit("No quedan elementos de ese tipo")
        else:
            self.list[posicion[0]-1][posicion[1]-1] = nombre_elemento
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

    
        
    



class Luigi(QThread):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.vidas = CANTIDAD_VIDAS
        # Creamos el Label y definimos su tamaño
        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'luigi_rigth_1.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)

