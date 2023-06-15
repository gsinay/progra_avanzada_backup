from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QPushButton,
                             QMessageBox)

from PyQt5.QtGui import QPixmap
import os
import sys

class WaitingRoom(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.icons_jugadores = 0 #trackea cuantos icons de jugadores tenemos en pantalla
        

    def init_gui(self):
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.boton_partir = QPushButton("Partir")
        self.boton_partir.setStyleSheet("font-size: 20px; color: black;")
        self.boton_partir.clicked.connect(self.partir_juego)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.boton_partir)
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

    
    def partir_juego(self):
        pass

    def servidor_caido(self):
        QMessageBox.critical(self, "Servidor desconectado", "Se desconectó el servidor, se cerrará el programa")
        QApplication.instance().quit()
    
    def server_lleno(self):
        self.boton_partir.setEnabled(False)
        QMessageBox.critical(self, "Sala llena", "La sala esta en capacidad, reinicie el programa e  intene nuevamente mas tarde")
        



             

if __name__ == '__main__':
    app = QApplication([])
    gabo = WaitingRoom()
    sys.exit(app.exec())
        