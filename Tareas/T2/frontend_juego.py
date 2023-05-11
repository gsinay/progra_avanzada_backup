from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout,
                             QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSignal, QSize
from models import Luigi
import os
from parametros import (ANCHO_GRILLA, LARGO_GRILLA)

class VentanaJuego(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setFixedSize(600, 700)
        self.setWindowTitle('Ventana Juego')
    
    def empezar_juego(self, username, lugar):
        self.show()
        if lugar == "Modo Constructor":
            self.armar_grilla()
            self.modo_constructor()
        else:
            self.armar_grilla()
            self.modo_juego(lugar)

    def armar_grilla(self):
        self.rows = LARGO_GRILLA
        self.columns = ANCHO_GRILLA
        self.grilla = QGridLayout()
        self.grilla.setSpacing(0)
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0 or row == LARGO_GRILLA - 1 or column == 0 or column == ANCHO_GRILLA - 1:
                    label = QLabel()
                    label.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'bordermap.png')))
                else:
                    label = QLabel(self)
                    label.setStyleSheet('background-color: black; border: 1px solid white')
                    label.setFixedSize(32, 32)
                label.setContentsMargins(0, 0, 0, 0) #quitar los margenes
                self.grilla.addWidget(label, row, column)

    def modo_constructor(self):
        self.setWindowTitle('Modo Constructor')
        #agregar elementos al lado izquierdo
        boton_luigi = QPushButton(f"")
        boton_luigi.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'luigi_rigth_1.png')))
        boton_pared = QPushButton(f"")
        boton_pared.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'wall.png')))
        boton_roca = QPushButton(f"")
        boton_roca.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'rock.png')))
        boton_estrella = QPushButton(f"")
        boton_estrella.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'osstar.png')))
        boton_fantasma_horizontal = QPushButton(f"")
        boton_fantasma_horizontal.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'white_ghost_left_1.png')))
        boton_fantasma_vertical = QPushButton(f"")
        boton_fantasma_vertical.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'red_ghost_vertical_1.png')))
        boton_fuego = QPushButton(f"")
        boton_fuego.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'fire.png')))
        botones_elementos_constructor = (boton_luigi, boton_pared, boton_roca, boton_estrella, 
                                         boton_fantasma_horizontal, boton_fantasma_vertical, boton_fuego)
        for boton in botones_elementos_constructor:
            boton.setIconSize(QSize(32, 32))

        
        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        for boton in botones_elementos_constructor:
            vbox1.addWidget(boton)
        vbox1.addStretch(1)
        #agregando grilla al lado derecho
        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addLayout(self.grilla)
        vbox2.addStretch(1)
        hbox1 = QHBoxLayout()
        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)
        self.setLayout(hbox1)

    
       








    def modo_juego(self, lugar):
        pass
