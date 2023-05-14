from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout,
                             QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox,
                             QFrame)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSignal, QSize
from models_juegos import Juego_constructor
import os
from parametros import (ANCHO_GRILLA, LARGO_GRILLA, FANTASMAS_HORIZONTALES,
                        FANTASMAS_VERTICALES, FUEGOS, ROCAS, MURALLAS)

class VentanaJuego(QWidget):

    senal_poblar_grilla = pyqtSignal(str)
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(800, 800)

    def set_info(self, username, nombre_lugar):
        self.show()
        self.setWindowTitle(f"Juego en {nombre_lugar} - {username}")
        self.armar_grilla()
        self.poblar_grilla(nombre_lugar)
        self.nombre_lugar = nombre_lugar
    def set_info_desde_constructor(self, grilla, username):
        self.show()
        self.setWindowTitle(f"Juego de {username}")
        self.armar_grilla()
        self.poblar_grilla_front(grilla)

    def armar_grilla(self):
        self.rows = LARGO_GRILLA
        self.columns = ANCHO_GRILLA
        self.grilla = QGridLayout()
        self.grilla.setSpacing(0)
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0 or row == LARGO_GRILLA - 1 or column == 0 or column == ANCHO_GRILLA - 1:
                    elemento = QLabel()
                    elemento.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'bordermap.png')).scaled(50,50))
                else:
                    elemento = QLabel()
                    elemento.id = (row, column)
                    elemento.setStyleSheet('background-color: black; border: 1px solid white')
                    elemento.setFixedSize(50, 50)
                elemento.setContentsMargins(0, 0, 0, 0) #quitar los margenes
                self.grilla.addWidget(elemento, row, column)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(self.grilla)
        hbox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)
    
    def poblar_grilla(self, nombre_lugar):
        self.senal_poblar_grilla.emit(nombre_lugar)

    def poblar_grilla_front(self, grilla):
        for fila in range(len(grilla)):
            for columna in range(len(grilla[0])):
                if len(grilla[fila][columna]) == 1:
                    if grilla[fila][columna][0] == "luigi":
                        pixmap = QPixmap(os.path.join('sprites', 'Personajes', 'luigi_front.png')).scaled(50,50)
                    elif grilla[fila][columna][0] == "fantasma_vertical":
                        pixmap = QPixmap(os.path.join('sprites', 'Personajes', 'red_ghost_vertical_1.png')).scaled(50,50)
                    elif grilla[fila][columna][0] == "fantasma_horizontal":
                        pixmap = QPixmap(os.path.join('sprites', 'Personajes', 'white_ghost_rigth_1.png')).scaled(50,50)
                    elif grilla[fila][columna][0] == "fuego":
                        pixmap = QPixmap(os.path.join('sprites', 'Elementos', 'fire.png')).scaled(50,50)
                    elif grilla[fila][columna][0] == "roca":
                        pixmap = QPixmap(os.path.join('sprites', 'Elementos', 'rock.png')).scaled(50,50)
                    elif grilla[fila][columna][0] == "pared":
                        pixmap = QPixmap(os.path.join('sprites', 'Elementos', 'wall.png')).scaled(50,50)
                    elif grilla[fila][columna][0] == "estrella":
                        pixmap = QPixmap(os.path.join('sprites', 'Elementos', 'osstar.png')).scaled(50,50)
                    bloque = self.grilla.itemAtPosition(fila + 1, columna + 1).widget()
                    bloque.setPixmap(pixmap)
                elif len(grilla[fila][columna]) == 0:
                    bloque = self.grilla.itemAtPosition(fila + 1, columna + 1).widget()
                    bloque.clear()
            
