import os
from funciones_auxiliares import generar_arena_inicial, generar_excavadores_iniciales, instanciar_arena, instanciar_excavador
from torneo import Torneo
from datos import lista_items

def guardar_torneo(torneo):
    with open(os.path.join("DCCavaCava.txt"), "w") as datos:
        datos.write(f"arena,{torneo.arena.nombre},{torneo.arena.tipo},{torneo.arena.rareza},{torneo.arena.humedad},{torneo.arena.dureza},{torneo.arena.estatica}\n")
        for excavador in torneo.equipo:
            datos.write(f"excavador,{excavador.nombre},{excavador.tipo}, {excavador.edad},{excavador.energia},{excavador.fuerza},{excavador.suerte},{excavador.felicidad}\n")
        for item in torneo.mochila:
            datos.write(f"item, {item.nombre}\n")
        datos.write(f"metros_cavados,{torneo.metros_cavados}\n")
        datos.write(f"meta, {torneo.meta}\n")
        datos.write(f"dias_transcurridos, {torneo.dias_transcurridos}")

def cargar_torneo():
    with open(os.path.join("DCCavaCava.txt"), "r") as datos:
        datos_lista = datos.readlines()
        lista_corregida = []
        for linea in datos_lista:
            linea = linea.strip().split(",")
            lista_corregida.append(linea)
        arena = instanciar_arena(lista_corregida[0][1:]) #lista_corregida[0][1:] es una lista con los datos de la arena, del uno en adelante
        excavadores = set() #set vacio                    porque el primer elemento es "arena" ocupado para la carga pero no la instanciacion
        mochila = []
        for elemento in lista_corregida:
            if elemento[0] == "excavador":
                excavadores.add(instanciar_excavador(elemento[1:], arena))
            if elemento[0] == "item":
                for tipo_item in lista_items: #recordar que los items estan instanciados en datos.py
                    for item in tipo_item:
                        if elemento[1] == item.nombre:
                            mochila.append(item)
            if elemento[0] == "metros_cavados":
                metros_cavados = float(elemento[1])
            if elemento[0] == "meta":
                meta = int(elemento[1])
            if elemento[0] == "dias_transcurridos":
                dias_transcurridos = int(elemento[1])
        
        return Torneo(Arena = arena, Equipo = excavadores, Mochila = mochila, \
                    Eventos = {"Lluvia", "Terremoto", "Derrumbe"}, Metros_cavados = metros_cavados, \
                        Dias_transcurridos = dias_transcurridos, Meta = meta)
                      
def generar_torneo():
    arena_inicial = generar_arena_inicial()
    excavadores_iniciales = generar_excavadores_iniciales(arena_inicial)
    torneo = Torneo(Arena = arena_inicial, Equipo = excavadores_iniciales, Mochila = [], \
                    Eventos = {"Lluvia", "Terremoto", "Derrumbe"}, Metros_cavados = 0, \
                        Dias_transcurridos = 0)
    return torneo
