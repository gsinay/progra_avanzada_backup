from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QMutex
from PyQt5.QtGui import QPixmap
import random
import os
from time import sleep
from parametros import (MIN_VELOCIDAD, MAX_VELOCIDAD)

class Fantasma(QThread):
    lock = QMutex()
    def __init__(self, senal_movimiento, posicion, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.tiempo_fantasma = 1 / ((random.randint(MIN_VELOCIDAD, MAX_VELOCIDAD))/10)
        self.posicion = posicion
        self.senal_movimiento = senal_movimiento
        self.vivo = True
        self.senal_movimiento = senal_movimiento
        self.daemon = True
        
        


class FantasmaHorizontal(Fantasma):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'white_ghost_left_1.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.direccion = "derecha" #se parten moviendo a la derecha


    def run(self):
       while self.vivo:
            sleep(self.tiempo_fantasma)
            self.lock.lock()
            self.senal_movimiento.emit(self.posicion, self.direccion, self)
            self.lock.unlock()

class FantasmaVertical(Fantasma):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'red_ghost_vertical_1.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.direccion = "arriba" #se parten moviendo hacia arriba

    def run(self):
        while self.vivo:
            sleep(self.tiempo_fantasma)
            self.lock.lock()
            self.senal_movimiento.emit(self.posicion, self.direccion, self)
            self.lock.unlock()
            
class Luigi(QWidget):
    senal_mover = pyqtSignal(str)
    def __init__(self, posicion, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label  = QLabel()
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'luigi_rigth_1.png')))
        self.posicion = posicion
        self.label.setScaledContents(True)
        self.vidas = 3