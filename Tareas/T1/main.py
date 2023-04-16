from funciones_auxiliares import generar_arena_inicial, generar_excavadores_iniciales
from torneo import Torneo
from guardar_cargar import guardar_torneo, cargar_torneo



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
    while True:
        try:
            input_usuario = input("Ingrese una opción para accionar: ")
            if input_usuario not in ["1", "2", "3"]:
                raise ValueError("Opción no válida")
            break
        except ValueError:
            print("Opción no válida, intentelo nuevamente")
    if int(input_usuario) == 1:
        print("Nueva partida")
        Partida = generar_torneo()
        menu_acciones(Partida)
    elif int(input_usuario) == 2:
        torneo = cargar_torneo()
        menu_acciones(torneo)
    elif int(input_usuario) == 3:
        print("Abandonar juego, para cargar nuevamente el menú de inicio, ejecute el archivo main.py")

def menu_acciones(torneo):
    print("**** {: ^50s} ****".format("MENÚ DE ACCIONES"))
    print("-" * 60)
    print(f"Dia de torneo DCCCavaCava: {torneo.dias_transcurridos}")
    print(f"Tipo de arena: {torneo.arena.tipo}")
    print("[1]. Simular día")
    print("[2]. Mostrar estado")
    print("[3]. Ver mochila")
    print("[4]. Guardar partida")
    print("[5]. Volver al menú de inicio. RECUERDE GUARDAR SU PARTIDA O PERDERA EL PROGRESO!")
    print("[x]. Salir del programa")
    while True:
        try:
            input_usuario = input("Ingrese una opción para accionar: ")
            if input_usuario not in ["1", "2", "3", "4", "5", "x"]:
                raise ValueError("Opción no válida")
            break
        except ValueError:
            print("Opción no válida, intentelo nuevamente")
    if input_usuario == "1":
        torneo.simular_dia()
        if torneo.dias_transcurridos == torneo.dias_totales:
            print("El torneo ha terminado!")
            if torneo.metros_cavados >= torneo.meta:
                print("Felicidades, has ganado el torneo!")
                print(f" Has cavado {torneo.metros_cavados} metros, y la meta era {torneo.meta} metros")
            else:
                print(f"Has perdido el torneo, la meta era {torneo.meta} metros y has cavado {torneo.metros_cavados} metros")
                print("Vuelve a intentarlo!")
            #agregar carcar una vez que tenga funcion definida
            menu_inicio()
        menu_acciones(torneo)
    elif input_usuario == "2":
        torneo.mostrar_estado()
        menu_acciones(torneo)
    elif input_usuario == "3":
        menu_mochila(torneo)
    elif input_usuario == "4":
        guardar_torneo(torneo)
        menu_inicio()
    elif input_usuario == "5":
        menu_inicio()
    elif input_usuario == "x":
        print("Saliendo del programa")
        return

def menu_mochila(torneo):
    print("**** {: ^50s} ****".format("MENÚ DE MOCHILA"))
    print("-" * 60)
    print(f"Dia de torneo DCCCavaCava: {torneo.dias_transcurridos}")
    print(f"Tipo de arena: {torneo.arena.tipo}")
    torneo.ver_mochila()
    print("ingrese el numero del objeto que desea utilizar o la opción x para voler al menú de acciones:")
    while True:
        try:
            input_usuario = input("Ingrese una opción para accionar: ")
            lista_numeros = [*range(1, len(torneo.mochila) + 1, 1)]
            for elemento in range(len(lista_numeros)):
                lista_numeros[elemento] = str(lista_numeros[elemento])
            lista_numeros.append("x")
            if input_usuario not in lista_numeros:
                raise ValueError("Opción no válida")
            break
        except ValueError:
            print("Opción no válida, intentelo nuevamente")
    if input_usuario == "x":
        menu_acciones(torneo)
    else:
        item = torneo.mochila[int(input_usuario) - 1]
        if item.tipo == "Tesoro":
            torneo.abrir_tesoro(item)
            
        else:
            torneo.usar_consumible(item)
    menu_acciones(torneo)

def generar_torneo():
    arena_inicial = generar_arena_inicial()
    excavadores_iniciales = generar_excavadores_iniciales(arena_inicial)
    torneo = Torneo(Arena = arena_inicial, Equipo = excavadores_iniciales, Mochila = [], \
                    Eventos = {"Lluvia", "Terremoto", "Derrumbe"}, Metros_cavados = 0, \
                        Dias_transcurridos = 0)
    return torneo

menu_inicio()


    

