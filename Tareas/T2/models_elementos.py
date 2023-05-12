from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap
import random
import os
from parametros import (MIN_VELOCIDAD, MAX_VELOCIDAD)

class Fantasma(QThread):
    def __init__(self, parent, posicion_inicial, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = QLabel(parent)
        self.tiempo_fantasma = 1 / (random.randint(MIN_VELOCIDAD, MAX_VELOCIDAD))
        self.posicion_inicial = posicion_inicial

class FantasmaHorizontal(Fantasma):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'white_ghost_left_1.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)
        self.mover_derecha = True
class FantasmaVertical(Fantasma):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'red_ghost_vertical_1.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)
        self.mover_arriba = True