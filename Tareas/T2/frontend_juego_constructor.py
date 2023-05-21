from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout,
                             QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox,
                             QComboBox)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSignal, QSize
from models_juegos import Juego_constructor
import os
from parametros import (ANCHO_GRILLA, LARGO_GRILLA)

class VentanaJuegoConstructor(QWidget):
    senal_agregar_elemento = pyqtSignal(tuple, str)
    senal_limpiar_grilla =  pyqtSignal()
    senal_empezar_juego = pyqtSignal(str)
    senal_tecla_presionada = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.juego_constructor = Juego_constructor()
        self.nombre_sprite_clickeado = "luigi"
        #instanciaremos esto para mantener cuenta de cuantos elementos quedan en el back

    def init_gui(self):
        self.setFixedSize(800, 800)
        self.setWindowTitle('Ventana Juego')
    
    def empezar_juego(self, username, lugar):
        self.show()
        if lugar == "Modo Constructor":
            self.username = username
            self.modo_constructor()
    def modo_constructor(self):
        self.armar_grilla("Modo Constructor")
        self.setWindowTitle('Modo Constructor')
        self.condiciones_ok = False #booleano que checkea si podemos empezar

        #agregar elementos al lado izquierdo
        self.boton_luigi = QPushButton(f"{self.juego_constructor.luigi}")
        self.boton_luigi.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'luigi_rigth_1.png')))
        self.boton_luigi.tipo = "entidad"
        self.boton_pared = QPushButton(f"{self.juego_constructor.pared}")
        self.boton_pared.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'wall.png')))
        self.boton_pared.tipo = "bloque"
        self.boton_roca = QPushButton(f"{self.juego_constructor.roca}")
        self.boton_roca.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'rock.png')))
        self.boton_roca.tipo = "bloque"
        self.boton_estrella = QPushButton(f"{self.juego_constructor.estrella}")
        self.boton_estrella.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'osstar.png')))
        self.boton_estrella.tipo = "bloque"
        self.boton_fantasma_horizontal = QPushButton(f"{self.juego_constructor.fantasma_horizontal}")
        self.boton_fantasma_horizontal.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'white_ghost_left_1.png')))
        self.boton_fantasma_horizontal.tipo = "entidad"
        self.boton_fantasma_vertical = QPushButton(f"{self.juego_constructor.fantasma_vertical}")
        self.boton_fantasma_vertical.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'red_ghost_vertical_1.png')))
        self.boton_fantasma_vertical.tipo = "entidad"
        self.boton_fuego = QPushButton(f"{self.juego_constructor.fuego}")
        self.boton_fuego.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'fire.png')))
        self.boton_fuego.tipo = "bloque"
        self.botones_elementos_constructor = (self.boton_luigi, self.boton_pared, self.boton_roca, self.boton_estrella, 
                                         self.boton_fantasma_horizontal, self.boton_fantasma_vertical, self.boton_fuego)
        
        for boton in self.botones_elementos_constructor:
            boton.setIconSize(QSize(32, 32))
        #conectar los botones a slot con lambda para registrar los nombres
        self.boton_luigi.clicked.connect(lambda: self.boton_sprite_clickeado("luigi"))
        self.boton_pared.clicked.connect(lambda: self.boton_sprite_clickeado("pared"))
        self.boton_roca.clicked.connect(lambda: self.boton_sprite_clickeado("roca"))
        self.boton_estrella.clicked.connect(lambda: self.boton_sprite_clickeado("estrella"))
        self.boton_fantasma_horizontal.clicked.connect(lambda: self.boton_sprite_clickeado("fantasma_horizontal"))
        self.boton_fantasma_vertical.clicked.connect(lambda: self.boton_sprite_clickeado("fantasma_vertical"))
        self.boton_fuego.clicked.connect(lambda: self.boton_sprite_clickeado("fuego"))
        
        #botones partir y limpiar y conectarlos
        self.boton_partir = QPushButton("Partir")
        self.boton_partir.clicked.connect(self.partir)
        self.boton_limpiar = QPushButton("limpiar")
        self.boton_limpiar.clicked.connect(self.limpiar)

        #dropdown menu
        self.dropdown = QComboBox(self)
        self.dropdown.addItem("todos")
        self.dropdown.addItem("entidad")
        self.dropdown.addItem("bloque")
        self.dropdown.currentTextChanged.connect(self.filtrar_botones)

        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addWidget(self.dropdown)
        for boton in self.botones_elementos_constructor:
            vbox1.addWidget(boton)
        vbox1.addStretch(10)
        vbox1.addWidget(self.boton_partir)
        vbox1.addWidget(self.boton_limpiar)

        #agregando grilla al lado derecho
        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addLayout(self.grilla)
        vbox2.addStretch(1)
        hbox1 = QHBoxLayout()
        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)
        self.setLayout(hbox1)

    def boton_sprite_clickeado(self, nombre_sprite):
        self.nombre_sprite_clickeado = nombre_sprite
    
    def filtrar_botones(self, text):
        opcion = self.dropdown.currentText()
        for boton in self.botones_elementos_constructor:
            if opcion == "todos":
                boton.show()
            else:
                if boton.tipo != opcion:
                    boton.hide()
                else:
                    boton.show()

            

    def armar_grilla(self, modo_juego):
        self.rows = LARGO_GRILLA
        self.columns = ANCHO_GRILLA
        self.grilla = QGridLayout()
        self.grilla.setSpacing(0)
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0 or row == LARGO_GRILLA - 1 or column == 0 or column == ANCHO_GRILLA - 1:
                    elemento = QLabel()
                    elemento.setPixmap(QPixmap(os.path.join('sprites', 'Elementos', 'bordermap.png')).scaled(50,50))
                elif modo_juego != "Modo Juego":
                    elemento = QPushButton()
                    elemento.id = (row, column)
                    elemento.setStyleSheet('background-color: black; border: 1px solid white')
                    elemento.setFixedSize(50, 50)
                    elemento.clicked.connect(self.boton_grilla_clickeado)
                elif modo_juego == "Modo Juego":
                    elemento = QLabel()
                    elemento.id = (row, column)
                    elemento.setStyleSheet('background-color: black; border: 1px solid white')
                    elemento.setFixedSize(50, 50)
                elemento.setContentsMargins(0, 0, 0, 0) #quitar los margenes
                self.grilla.addWidget(elemento, row, column)

    def boton_grilla_clickeado(self):  ##conectar esto con backend!!!!
        elemento = self.sender()
        self.senal_agregar_elemento.emit(elemento.id, self.nombre_sprite_clickeado)

    def error_agregar_elemento(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)
    def elemento_agregado(self, nombre_elemento, button_id):
        bloque = self.grilla.itemAtPosition(button_id[0], button_id[1]).widget()
        if nombre_elemento == "luigi":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'luigi_rigth_1.png')))
            self.juego_constructor.luigi -= 1
            self.boton_luigi.setText(f"{self.juego_constructor.luigi}")
        elif nombre_elemento == "pared":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'wall.png')))
            self.juego_constructor.pared -= 1
            self.boton_pared.setText(f"{self.juego_constructor.pared}")
        elif nombre_elemento == "roca":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'rock.png')))
            self.juego_constructor.roca -= 1
            self.boton_roca.setText(f"{self.juego_constructor.roca}")
        elif nombre_elemento == "estrella":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'osstar.png')))
            self.juego_constructor.estrella -= 1
            self.boton_estrella.setText(f"{self.juego_constructor.estrella}")
        elif nombre_elemento == "fantasma_horizontal":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'white_ghost_left_1.png')))
            self.juego_constructor.fantasma_horizontal -= 1
            self.boton_fantasma_horizontal.setText(f"{self.juego_constructor.fantasma_horizontal}")
        elif nombre_elemento == "fantasma_vertical":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Personajes', 'red_ghost_vertical_1.png')))
            self.juego_constructor.fantasma_vertical -= 1
            self.boton_fantasma_vertical.setText(f"{self.juego_constructor.fantasma_vertical}")
        elif nombre_elemento == "fuego":
            bloque.setIcon(QIcon(os.path.join('sprites', 'Elementos', 'fire.png')))
            self.juego_constructor.fuego -= 1
            self.boton_fuego.setText(f"{self.juego_constructor.fuego}")
        else:
            print("error")

    def limpiar(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if row != 0 and row != LARGO_GRILLA - 1 and column != 0 and column != ANCHO_GRILLA - 1:
                    bloque = self.grilla.itemAtPosition(row, column).widget()
                    bloque.setIcon(QIcon())
                    bloque.setStyleSheet('background-color: black; border: 1px solid white')
        self.juego_constructor = Juego_constructor()
        self.boton_luigi.setText(f"{self.juego_constructor.luigi}")
        self.boton_pared.setText(f"{self.juego_constructor.pared}")
        self.boton_roca.setText(f"{self.juego_constructor.roca}")
        self.boton_estrella.setText(f"{self.juego_constructor.estrella}")
        self.boton_fantasma_horizontal.setText(f"{self.juego_constructor.fantasma_horizontal}")
        self.boton_fantasma_vertical.setText(f"{self.juego_constructor.fantasma_vertical}")
        self.boton_fuego.setText(f"{self.juego_constructor.fuego}")
        self.senal_limpiar_grilla.emit()
    
    def partir(self):
        self.senal_empezar_juego.emit(self.username)
        if self.condiciones_ok == True: 
            self.hide()
            for boton in self.botones_elementos_constructor:
                boton.deleteLater()
            for row in range(self.rows):
                for column in range(self.columns):
                    if row != 0 and row != LARGO_GRILLA - 1 and column != 0 and column != ANCHO_GRILLA - 1:
                        bloque = self.grilla.itemAtPosition(row, column).widget()
                        bloque.setEnabled(False)
            self.boton_limpiar.setEnabled(False)
            self.boton_partir.setEnabled(False)
    
    def check_partir(self, ok_para_partir, mensaje):
        if ok_para_partir == False:
            QMessageBox.warning(self, "Error", mensaje)
        else:
            self.condiciones_ok = True

    




    
       