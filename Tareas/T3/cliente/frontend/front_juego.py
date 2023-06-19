
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QPushButton,
                             QMessageBox, QLineEdit)
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtGui import QPixmap
import os
import sys
import json

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    NUMERO_VIDAS = int(parametros["NUMERO_VIDAS"])

class GameRoom(QWidget):
    senal_anunciar_accion = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter_turno = 0
        
    def init_gui(self, nombre_propio, nombre_jugadores):
        self.setGeometry(200, 200, 1200, 1200)
        self.setFixedSize(1000, 1000)
        self.setWindowTitle('Sala de juego de ' + nombre_propio)
        self.setFixedSize(1000, 1000)

        #foto de background
        self.label_background = QLabel(self)
        self.label_background.setGeometry(0, 0, 1000, 1000)
        pixeles = QPixmap(os.path.join("Sprites", "background", "background_juego"))
        self.label_background.setPixmap(pixeles)
        self.label_background.setMaximumSize(1000, 1000)
        self.label_background.setScaledContents(True)

        #label de turno
        self.label_turno = QLabel("turno numero: 0", self)
        self.label_turno.setStyleSheet("font-size: 20px; color: white;")
        self.label_turno.resize(self.label_turno.sizeHint())
        self.label_turno.move(50, 60)

        #label de cantidad anunciada
        self.label_cantidad = QLabel("cantidad anunciada: x", self)
        self.label_cantidad.setStyleSheet("font-size: 20px; color: white;")
        self.label_cantidad.move(400, 60)

        #label de jugador en turno
        self.label_jugador_turno = QLabel("turno de: x", self)
        self.label_jugador_turno.setStyleSheet("font-size: 20px; color: white;")
        self.label_jugador_turno.move(700, 60)

        #armamos las "islas de los jugdaores". El primero de la lista es el propio y tiene acceso a los botones el resto son contrincantes
        for i in range(len(nombre_jugadores)):
            icono_jugador = QLabel(self)
            pixeles = QPixmap(os.path.join("Sprites", "extra", "user_profile.png")).scaled(50,50)
            icono_jugador.setPixmap(pixeles)
            setattr(self, f"vidas_{nombre_jugadores[i]}", QLabel("vidas: " + str(NUMERO_VIDAS), self))
            getattr(self, f"vidas_{nombre_jugadores[i]}").setStyleSheet("font-size: 20px; color: white;")
            setattr(self, f"nombre_{nombre_jugadores[i]}", QLabel(nombre_jugadores[i], self))
            label_nombre = QLabel(nombre_jugadores[i], self)
            label_nombre.setStyleSheet("font-size: 20px; color: white;")
            if i == 0: #jugador propio
                icono_jugador.move(400, 100)
                getattr(self, f"vidas_{nombre_jugadores[i]}").move(500, 130)
                label_nombre.move(400, 150)
            elif i == 1: #jugador de la derecha
                icono_jugador.move(800, 400)
                getattr(self, f"vidas_{nombre_jugadores[i]}").move(900, 430)
                label_nombre.move(800, 450)
            elif i == 2: #jugador de abajo
                icono_jugador.move(400, 800)
                getattr(self, f"vidas_{nombre_jugadores[i]}").move(500, 830)
                label_nombre.move(400, 850)
            elif i == 3: #jugador de la izquierda
                icono_jugador.move(100, 400)
                getattr(self, f"vidas_{nombre_jugadores[i]}").move(200, 430)
                label_nombre.move(100, 450)
            
        #botones de accion
        self.boton_anunciar_accion = QPushButton("anunciar accion", self)
        self.boton_anunciar_accion.move(600, 800)
        self.casilla_valor = QLineEdit(self)
        self.casilla_valor.move(800, 800)
        self.boton_pasar_turno = QPushButton("pasar turno", self)
        self.boton_pasar_turno.move(600, 850)
        self.boton_cambiar_dados = QPushButton("cambiar dados", self)
        self.boton_cambiar_dados.move(800, 850)
        self.boton_usar_poder = QPushButton("usar poder", self)
        self.boton_usar_poder.move(600, 900)
        self.boton_dudar = QPushButton("dudar", self)
        self.boton_dudar.move(800, 900)

        #conectar botones a slots
        self.boton_anunciar_accion.clicked.connect(self.anunciar_accion)
        self.boton_pasar_turno.clicked.connect(self.pasar_turno)
        self.boton_cambiar_dados.clicked.connect(self.cambiar_dados)
        self.boton_usar_poder.clicked.connect(self.usar_poder)
        self.boton_dudar.clicked.connect(self.dudar)
        
        self.botones = {self.boton_anunciar_accion, 
                        self.boton_pasar_turno, 
                        self.boton_cambiar_dados, 
                        self.boton_usar_poder, 
                        self.boton_dudar
                        }
        self.show()

    def turno(self, booleano_turno, info_turno):
        if booleano_turno:
            for boton in self.botones:
                boton.setEnabled(True)
        else:
            for boton in self.botones:
                boton.setEnabled(False)

        self.label_jugador_turno.setText("turno de: " + str(info_turno[0]))
        self.label_jugador_turno.resize(self.label_jugador_turno.sizeHint())
        self.label_cantidad.setText("cantidad anunciada: " + str(info_turno[1]))
        self.label_cantidad.resize(self.label_cantidad.sizeHint())
        self.label_turno.setText("turno numero: " + str(info_turno[2]))
        


    
    def anunciar_accion(self):
        self.senal_anunciar_accion.emit(self.casilla_valor.text())

    def pasar_turno(self):
        pass

    def cambiar_dados(self):
        pass

    def usar_poder(self):
        pass

    def dudar(self):
        pass


    
    