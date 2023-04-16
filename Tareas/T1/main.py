from funciones_auxiliares import generar_arena_inicial, generar_excavadores_iniciales
from parametros import EXCAVADORES_INICIALES
from datos import excavadores
from random import choice
from torneo import Torneo

# def menu_inicio():
def menu_inicio():
    print("\n")
    print("*" * 60)
    print("**** {: ^50s} ****".format("MENÚ DE INICIO"))
    print("*" * 60)
    print("Eliga una opción:".center(62))
    print("[1]. Nueva partida")
    print("[2]. Cargar partida")
    print("[3]. Abandonar juego")
    input_usuario = input("Ingrese una opción: ")
    #write a try/except block to make sure the user enters a valid option
    try:
        if int(input_usuario) == 1:
            print("Nueva partida")
            Partida = generar_torneo()
            print(Partida)
            menu_acciones(Partida)
        elif int(input_usuario) == 2:
            print("Cargar partida")
        elif int(input_usuario) == 3:
            print("Abandonar juego, para cargar nuevamente el menú de inicio, ejecute el archivo main.py")
    except ValueError:
        print("Opción no válida")
        menu_inicio()

def menu_acciones(torneo):
    print("**** {: ^50s} ****".format("MENÚ DE ACCIONES"))
    print("-" * 60)
    print(f"Dia de torneo DCCCavaCava: {torneo.dias_transcurridos}")
    print(f"Tipo de arena: {torneo.arena.tipo}")
    print("[1]. Simular día")
    print("[2]. Mostrar estado")
    print("[3]. Ver mochila")
    print("[4]. Guardar partida")
    print("[5]. Volver al menú de inicio")
    print("[x]. Salir del programa")
    while True:
        try:
            input_usuario = input("Ingrese una opción para accionar: ")
            if input_usuario not in ["1", "2", "3", "4", "5", "x"]:
                raise ValueError("Opción no válida")
            break
        except ValueError:
            print("Opción no válida, intentelo nuevamente")
    if int(input_usuario) == 1:
        torneo.simular_dia()
        menu_acciones(torneo)
    elif int(input_usuario) == 2:
        torneo.mostrar_estado()
        menu_acciones(torneo)
    elif int(input_usuario) == 3:
        torneo.ver_mochila()
        menu_acciones(torneo)
    elif int(input_usuario) == 4:
        return
    elif int(input_usuario) == 5:
        menu_inicio()
    elif input_usuario == "x":
        print("Saliendo del programa")
        return




def generar_torneo():
    arena_inicial = generar_arena_inicial()
    excavadores_iniciales = generar_excavadores_iniciales(arena_inicial)
    torneo = Torneo(Arena = arena_inicial, Equipo = excavadores_iniciales, Mochila = [], \
                    Eventos = {"Lluvia", "Terremoto", "Derrumbe"}, Metros_cavados = 0, \
                        Dias_transcurridos = 0)
    return torneo

menu_inicio()

    

