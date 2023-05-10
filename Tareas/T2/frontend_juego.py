from PyQt5.QtWidgets import QWidget, QLabel

class VentanaJuego(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(200, 200, 600, 700)
        self.setWindowTitle('Ventana Juego')
    
    def empezar_juego(self, username, lugar):
        self.show()
        label_titulo = QLabel(self)
        if lugar == "Modo Constructor":
            label_titulo.setText("Modo Constructor")
        else:
            label_titulo.setText("Modo Juego")
        label_titulo.move(50, 50)
        label_titulo.show()
        print(username)