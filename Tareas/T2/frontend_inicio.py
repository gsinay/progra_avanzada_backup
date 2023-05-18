import sys
import os
from PyQt5.QtWidgets import  (QApplication, QWidget, QLabel, QLineEdit,
                             QComboBox, QPushButton, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from parametros import (MIN_CARACTERES, MAX_CARACTERES)

class VentanaInicio(QWidget):

    senal_empezar_constructor = pyqtSignal(str, str)
    senal_empezar_juego = pyqtSignal(str, str)
    senal_verificar = pyqtSignal(str)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(200, 200, 600, 750)
        self.setWindowTitle('Ventana Inicial')
        self.setFixedSize(600, 750)
        
        #foto de background
        self.label_background = QLabel(self)
        self.label_background.setGeometry(0, 0, 600, 600)
        pixeles = QPixmap(os.path.join('sprites', 'Fondos', 'fondo_inicio.png'))
        self.label_background.setPixmap(pixeles)
        self.label_background.setMaximumSize(1000, 1000)
        self.label_background.setScaledContents(True)

        #label username
        self.label_username = QLabel(self)
        self.label_username.setStyleSheet('color: white')
        self.label_username.setText('Username:')
        self.label_username.move(50, 500)

        #text input username
        self.text_username = QLineEdit(self)
        self.text_username.setStyleSheet('background-color: white')
        self.text_username.move(150, 500)

        #dropdown menu de lugares para jugar
        self.dropdown_lugares = QComboBox(self)
        self.dropdown_lugares.move(50,620)
        self.dropdown_lugares.resize(500, 40)
        directorio_mapas = os.listdir("mapas")
        for mapa in directorio_mapas:
            nombre_mapa = mapa[:-4]
            self.dropdown_lugares.addItem(nombre_mapa)
        self.dropdown_lugares.addItem("Modo Constructor")


        #boton para iniciar el juego
        self.boton_iniciar = QPushButton(self)
        self.boton_iniciar.setText('Empezar Juego')
        self.boton_iniciar.move(50, 650)

        self.boton_salir = QPushButton(self)
        self.boton_salir.setText('Salir del programa')
        self.boton_salir.move(50, 700)



        #conectar el boton a un slot que verifica la informacion
        self.boton_iniciar.clicked.connect(self.verificar_info)
        self.boton_salir.clicked.connect(self.salir)

        self.show()

    

    def verificar_info(self): 
        username = self.text_username.text()
        self.senal_verificar.emit(username)

    def salir(self):
        self.close()
    
    def error_username(self, mensaje):
        QMessageBox.warning(self, 'Error', mensaje)
        
    def empezar_juego(self, username):
            lugar = self.dropdown_lugares.currentText()
            if lugar == "Modo Constructor":
                self.senal_empezar_constructor.emit(username, lugar)
            else:
                self.senal_empezar_juego.emit(username, lugar)
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    ventana_inicio.show()
    sys.exit(app.exec())