from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QPushButton,
                             QMessageBox)
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtGui import QPixmap
import os
import sys

class WaitingRoom(QWidget):
    senal_partir_juego = pyqtSignal()
    senal_armar_ventana_juego = pyqtSignal(str, list)
    senal_salir_juego = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.icons_jugadores = 0 #trackea cuantos icons de jugadores tenemos en pantalla
        

    def init_gui(self):
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.boton_partir = QPushButton("Partir")
        self.boton_partir.setStyleSheet("font-size: 20px; color: black;")
        self.boton_partir.clicked.connect(self.check_partir_juego)
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.setStyleSheet("font-size: 20px; color: black;")
        self.boton_salir.clicked.connect(self.salir_juego)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.boton_partir)
        self.vbox.addWidget(self.boton_salir)
        self.setLayout(self.vbox)

        self.setGeometry(200, 200, 600, 750)
        self.setFixedSize(600, 750)
        self.setWindowTitle('Sala de espera')
        self.setFixedSize(600, 750)
        
        #foto de background
        self.label_background = QLabel(self)
        self.label_background.setGeometry(0, 0, 600, 600)
        pixeles = QPixmap(os.path.join("Sprites", "background", "background_inicio"))
        self.label_background.setPixmap(pixeles)
        self.label_background.setMaximumSize(1000, 1000)
        self.label_background.setScaledContents(True)
        self.show()


    def actualizar_waiting_room(self, nombres):
        for nombre in nombres[self.icons_jugadores:]:
            vbox = QVBoxLayout()
            label_nombre = QLabel(nombre)
            label_nombre.setStyleSheet("font-size: 20px; color: white;")
            label = QLabel(nombre)
            pixeles = QPixmap(os.path.join("Sprites", "extra", "user_profile.png")).scaled(50,50)
            label.setPixmap(pixeles)
            vbox.addWidget(label)
            vbox.addWidget(label_nombre)
            self.hbox.addLayout(vbox)
            self.icons_jugadores += 1
        self.update()
        self.show()

    def jugador_desconectado(self, nombres):
        self.clear_layout(self.hbox)
        self.icons_jugadores = 0
        self.actualizar_waiting_room(nombres)


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            else:
                self.clear_layout(item.layout())

    def repaint(self, nombres, bool_standby, bool_estuvo_en_standby):
        self.clear_layout(self.hbox)
        self.icons_jugadores = 0
        self.actualizar_waiting_room(nombres)
        if bool_standby:
            self.boton_partir.setEnabled(True)
        if bool_estuvo_en_standby:
            self.boton_partir.setEnabled(True)
            self.label_lleno.setParent(None)
        
    def salir_juego(self):
        self.senal_salir_juego.emit()

    
    def check_partir_juego(self):
        self.senal_partir_juego.emit()

    def partir_juego(self, nombre_propio, nombres):
        self.hide()
        self.senal_armar_ventana_juego.emit(nombre_propio, nombres)

    def servidor_caido(self):
        QMessageBox.critical(self, "Servidor desconectado", "Se desconectó el servidor, se cerrará el programa")
        QApplication.instance().quit()
    
    def server_lleno(self):
        self.boton_partir.setEnabled(False)
        self.label_lleno = QLabel("El servidor está lleno, espere a que se libere un cupo")
        self.label_lleno.resize(200, 200)
        self.label_lleno.setStyleSheet("font-size: 20px; color: white;")
        self.vbox.addWidget(self.label_lleno)
        self.update()

    def error_partir_juego(self, razon):
        if razon == "faltan jugadores":
            QMessageBox.warning(self, "Faltan jugadores", "No se puede partir el juego, faltan jugadores")
        



             

if __name__ == '__main__':
    app = QApplication([])
    gabo = WaitingRoom()
    sys.exit(app.exec())
        