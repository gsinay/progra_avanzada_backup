from PyQt5.QtWidgets import QApplication
from frontend_inicio import VentanaInicio
from frontend_juego import VentanaJuego
import sys


if __name__ == '__main__':
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    ventana_juego = VentanaJuego()

    # Conectamos la señal
    ventana_inicio.senal_empezar.connect(ventana_juego.empezar_juego)

    sys.exit(app.exec())