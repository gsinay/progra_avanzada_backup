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
        elif int(input_usuario) == 2:
            print("Cargar partida")
        elif int(input_usuario) == 3:
            print("Abandonar juego")
    except ValueError:
        print("Opción no válida")
        menu_inicio()


def generar_torneo():
    arena_inicial = generar_arena_inicial()
    excavadores_iniciales = generar_excavadores_iniciales(arena_inicial)
    torneo = Torneo(Arena = arena_inicial, Equipo = excavadores_iniciales, Mochila = [], \
                    Eventos = {"Lluvia", "Terremoto", "Derrumbe"}, Metros_cavados = 0, \
                        Dias_transcurridos = 0)
    return torneo

menu_inicio()
     
    

