from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap
import os
from parametros import (CANTIDAD_VIDAS)
import sys

class Luigi(QObject):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vidas = CANTIDAD_VIDAS
        # Creamos el Label y definimos su tamaño
        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Personajes', 'luigi_rigth_1.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)

class Wall(QObject):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'wall.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)
class Rock(QObject):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'rock.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)
class Star(QObject):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'osstar.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)
class Fire(QObject):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'fire.png')))
        self.label.setScaledContents(True)
        self.label.setFixedSize(32, 32)
        self.label.setVisible(True)

#los ghosts son threads porque pueden haber varios funcionando al mismo tiempo. 

