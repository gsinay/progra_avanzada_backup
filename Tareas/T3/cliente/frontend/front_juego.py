
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QPushButton,
                             QMessageBox, QLineEdit)
from PyQt5.QtCore import pyqtSignal, QTimer, QCoreApplication

from PyQt5.QtGui import QPixmap
import os
import sys
import json

with open("parametros.json") as archivo:
    parametros = json.load(archivo)
    NUMERO_VIDAS = int(parametros["NUMERO_VIDAS"])

class GameRoom(QWidget):
    senal_anunciar_accion = pyqtSignal(str)
    senal_paso_turno = pyqtSignal()
    senal_dudar = pyqtSignal()
    senal_cambiar_dados = pyqtSignal()
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
        self.casilla_valor.setPlaceholderText("ingrese valor acá")
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
                        self.boton_usar_poder, 
                        self.boton_dudar
                        }
        self.boton_cambiar_dados.setEnabled(True)
        
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

    def actualizar_vidas(self, info_vidas):
        getattr(self, f"vidas_{info_vidas[0]}").setText("vidas: " + str(info_vidas[1]))


    def paint_dados(self, set_dados):
        for i in range(len(set_dados)):
            valor_dado = set_dados[i]
            pixel_dado = QPixmap(os.path.join("Sprites", "dices", f"dice_{valor_dado}.png")).scaled(50,50)
            dado = QLabel(self)
            dado.setPixmap(pixel_dado)
            dado.move(400 + 100*i, 200)
            dado.show()
        
        #pintar dados ocultos contrincantes
        for i in range(3):
            for j in range(2):
                pixel_dado = QPixmap(os.path.join("Sprites", "dices", f"dice_background.png")).scaled(50,50)
                dado = QLabel(self)
                dado.setPixmap(pixel_dado)
                if i == 0:
                    dado.move(100 + 70*j, 500)
                elif i == 1:
                    dado.move(800 + 70*j, 500)
                elif i == 2:
                    dado.move(400 + 70*j, 870)
                dado.show()

    def jugador_desconectado(self, nombre):
        QMessageBox.warning(self, "Jugador desconectado", nombre + " se ha desconectado, se partirá una nueva ronda")
        #le asignamos 0 vidas a su label como si estuviera muerto
        getattr(self, f"vidas_{nombre}").setText("vidas: 0")

    def error_turno(self, str):
        QMessageBox.warning(self, "Error en tu jugada", str)

    
    def anunciar_accion(self):
        self.senal_anunciar_accion.emit(self.casilla_valor.text())
        self.casilla_valor.setText("")

    def pasar_turno(self):
        self.senal_paso_turno.emit()

    def dudar(self):
        self.senal_dudar.emit()

    def cambiar_dados(self):
        self.senal_cambiar_dados.emit()

    def error_cambiar_dados(self):
        QMessageBox.warning(self, "Error en tu jugada", "Ya has cambiado los dados anteriormente")

    def usar_poder(self):
        pass

    def anuncio_ganador(self, nombre):
        QMessageBox.information(self, "Ganador", nombre + " ha ganado la partida")
        for boton in self.botones:
            boton.setEnabled(False)
        self.boton_cambiar_dados.setEnabled(False)
        self.boton_salir = QPushButton("salir", self)
        self.boton_salir.move(700, 900)
        self.boton_salir.clicked.connect(self.quit)
        self.boton_salir.show()

    def quit(self):
        print("Raise connection error para manejar el quit")
        raise ConnectionError
    





    
    