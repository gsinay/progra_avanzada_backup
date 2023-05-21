from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout,
                             QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox,
                             QApplication)
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSignal, QSize
import os
from parametros import (ANCHO_GRILLA, LARGO_GRILLA,
                        TIEMPO_CUENTA_REGRESIVA, CANTIDAD_VIDAS)

class VentanaJuego(QWidget):

    senal_poblar_grilla = pyqtSignal(str, str)
    senal_tecla_presionada = pyqtSignal(str)
    senal_pausar = pyqtSignal()
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(800, 800)

    def set_info(self, username, nombre_lugar):
        self.show()
        self.nombre_lugar = nombre_lugar
        self.username = username
        self.setWindowTitle(f"Juego en {nombre_lugar} - {username}")
        self.armar_botones_y_timer(TIEMPO_CUENTA_REGRESIVA, CANTIDAD_VIDAS)
        self.armar_grilla()
        self.poblar_grilla(nombre_lugar)
    def set_info_desde_constructor(self, grilla, username):
        self.show()
        self.username = username
        self.setWindowTitle(f"Juego de {username}")
        self.armar_botones_y_timer(TIEMPO_CUENTA_REGRESIVA, CANTIDAD_VIDAS)
        self.armar_grilla()
        self.poblar_grilla_front(grilla)
        
    def armar_botones_y_timer(self, tiempo, vidas):
        self.label_timer = QLabel(self)
        self.label_timer.setText(f"Tiempo restante: {tiempo}")
        self.label_vidas = QLabel(self)
        self.label_vidas.setText(f"Vidas restantes: {vidas}")
        self.boton_pausa = QPushButton(self)
        self.boton_pausa.setText("Pausar")
        self.boton_pausa.clicked.connect(self.pausar)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_timer)
        vbox.addWidget(self.label_vidas)
        vbox.addWidget(self.boton_pausa)
        self.hbox = QHBoxLayout()
        self.hbox.addLayout(vbox)

    def actualizar_tiempo(self, tiempo):
        self.label_timer.setText(f"Tiempo restante: {tiempo}")
    def actualizar_vidas(self, vidas):
        self.label_vidas.setText(f"Vidas restantes: {vidas}")
    def pausar(self):
        self.senal_pausar.emit()
    def actualizar_boton_pausa(self, juego_pausado):
        if juego_pausado:
            self.boton_pausa.setText("renaudar")
        else:
            self.boton_pausa.setText("pausar")
    

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
        
        self.hbox.addLayout(self.grilla)
        self.setLayout(self.hbox)
    
    def poblar_grilla(self, nombre_lugar):
        self.senal_poblar_grilla.emit(nombre_lugar, self.username)

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

    def keyPressEvent(self, event):
       self.senal_tecla_presionada.emit(event.text())

    def game_over(self, username, text, puntaje):
        if puntaje == 0:
            archivo_sonido = os.path.join('sounds', 'gameOver.wav')
            sonido = QSound(archivo_sonido)
            sonido.play()
            QMessageBox.information(self, "Game Over", f"{username}: {text}")
        else:
            archivo_sonido = os.path.join('sounds', 'stageClear.wav')
            sonido = QSound(archivo_sonido)
            sonido.play()
            QMessageBox.information(self, "Game Over", f"{username}: {text} con {puntaje} puntos")
        QApplication.quit()

            
    
            
