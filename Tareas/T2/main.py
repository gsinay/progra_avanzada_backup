from PyQt5.QtWidgets import QApplication
from frontend_inicio import VentanaInicio
from frontend_juego_constructor import VentanaJuegoConstructor
from frontend_juego import VentanaJuego
from backend_inicio import Procesador
from models_juegos import Juego_constructor, Juego
import sys


if __name__ == '__main__':
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    procesador_inicio = Procesador(ventana_inicio)
    ventana_juego_constructor = VentanaJuegoConstructor()
    logica_juego_constructor = Juego_constructor()
    logica_juego = Juego()
    ventana_juego = VentanaJuego()
    logica_juego.setFocus()
    

    # Conectamos las señales del frontend inicio con el procesadord
    ventana_inicio.senal_verificar.connect(procesador_inicio.verificar_username)
    procesador_inicio.senal_username_verificado.connect(ventana_inicio.empezar_juego)
    procesador_inicio.senal_username_malo.connect(ventana_inicio.error_username)
    ventana_inicio.senal_empezar_constructor.connect(ventana_juego_constructor.empezar_juego)
    ventana_inicio.senal_empezar_juego.connect(ventana_juego.set_info)

    #señales juego

    ventana_juego_constructor.senal_agregar_elemento.connect(logica_juego_constructor.agregar_elemento)
    logica_juego_constructor.senal_error_agregar_elemento.connect(ventana_juego_constructor.error_agregar_elemento)
    logica_juego_constructor.senal_elemento_agregado.connect(ventana_juego_constructor.elemento_agregado)
    ventana_juego_constructor.senal_limpiar_grilla.connect(logica_juego_constructor.limpiar_grilla)
    ventana_juego_constructor.senal_empezar_juego.connect(logica_juego_constructor.empezar_juego)
    logica_juego_constructor.senal_check_partir.connect(ventana_juego_constructor.check_partir)
    #de ahora en adelante se conecta el back con la ventana juego y no juego_Constructor
    logica_juego_constructor.senal_partir_ventana_juego.connect(ventana_juego.set_info_desde_constructor)
    logica_juego_constructor.senal_partir.connect(logica_juego.partir)
   
    ventana_juego.senal_tecla_presionada.connect(logica_juego.tecla_presionada)

    ventana_juego.senal_poblar_grilla.connect(logica_juego.poblar_grilla_backend)
    logica_juego.senal_armar_front_inicial.connect(ventana_juego.poblar_grilla_front)
    logica_juego.senal_game_over.connect(ventana_juego.game_over)
    logica_juego.senal_actualizar_tiempo.connect(ventana_juego.actualizar_tiempo)
    logica_juego.senal_actualizar_vidas.connect(ventana_juego.actualizar_vidas)
    ventana_juego.senal_pausar.connect(logica_juego.pausar)
    logica_juego.senal_actualizar_boton_pausa.connect(ventana_juego.actualizar_boton_pausa)

    sys.exit(app.exec())