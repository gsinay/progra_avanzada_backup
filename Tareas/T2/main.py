from PyQt5.QtWidgets import QApplication
from frontend_inicio import VentanaInicio
from frontend_juego import VentanaJuego
from backend_inicio import Procesador
import sys


if __name__ == '__main__':
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    procesador_inicio = Procesador(ventana_inicio)
    ventana_juego = VentanaJuego()

    # Conectamos las señales del frontend inicio con el procesador
    ventana_inicio.senal_verificar.connect(procesador_inicio.verificar_username)
    procesador_inicio.senal_username_verificado.connect(ventana_inicio.empezar_juego)
    procesador_inicio.senal_username_malo.connect(ventana_inicio.error_username)
    ventana_inicio.senal_empezar.connect(ventana_juego.empezar_juego)
    


    sys.exit(app.exec())