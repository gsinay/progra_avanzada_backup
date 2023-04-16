from datos import excavadores, arenas
from arenas import Arena_magnetica, Arena_mojada, Arena_normal, Arena_rocosa
from excavadores import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido
from random import choice
from parametros import ARENA_INICIAL, EXCAVADORES_INICIALES
import os

def filtrar(lista, filtro):
    lista_a_retornar = []
    for elemento in lista:
        if elemento[1] == filtro:
            lista_a_retornar.append(elemento)
    return lista_a_retornar

        
def generar_arena_inicial():
    arenas_filtradas = filtrar(arenas, ARENA_INICIAL)
    arena_inicial = choice(arenas_filtradas)
    if arena_inicial[1] == "normal":
        arena_inicial = Arena_normal(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                    Rareza = int(arena_inicial[2]), Humedad = int(arena_inicial[3]), \
                                    Dureza = int(arena_inicial[4]), Estatica = int(arena_inicial[5]))
    elif arena_inicial[1] == "mojada":
        arena_inicial = Arena_mojada(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                    Rareza = int(arena_inicial[2]), Humedad = int(arena_inicial[3]), \
                                    Dureza = int(arena_inicial[4]), Estatica = int(arena_inicial[5]))
    elif arena_inicial[1] == "rocosa":
        arena_inicial = Arena_rocosa(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                    Rareza = int(arena_inicial[2]), Humedad = int(arena_inicial[3]), \
                                    Dureza = int(arena_inicial[4]), Estatica = int(arena_inicial[5]))
    elif arena_inicial[1] == "magnetica":
        arena_inicial = Arena_magnetica(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                    Rareza = int(arena_inicial[2]), Humedad = int(arena_inicial[3]), \
                                    Dureza = int(arena_inicial[4]), Estatica = int(arena_inicial[5]))
    return arena_inicial

def generar_excavadores_iniciales(Arena_inicio):
    lista_excavadores = []
    instancia_excavadores = set()
    while len(lista_excavadores) < EXCAVADORES_INICIALES:
        excavador = choice(excavadores)
        if excavador not in lista_excavadores:
            lista_excavadores.append(excavador)
    for excavador in lista_excavadores:
        if excavador[1] == "docencio":
            instancia_excavadores.add(ExcavadorDocencio(Nombre = excavador[0], \
                                                        Edad = int(excavador[2]), Energia = int(excavador[3]),
                                                         Fuerza = int(excavador[4]), Suerte = int(excavador[5]), \
                                                            Felicidad = int(excavador[6]), Arena_actual = Arena_inicio))
        elif excavador[1] == "tareo":
            instancia_excavadores.add(ExcavadorTareo(Nombre = excavador[0], \
                                                        Edad = int(excavador[2]), Energia = int(excavador[3]),
                                                         Fuerza = int(excavador[4]), Suerte = int(excavador[5]), \
                                                            Felicidad = int(excavador[6]), Arena_actual = Arena_inicio))
        elif excavador[1] == "hibrido":
            instancia_excavadores.add(ExcavadorHibrido(Nombre = excavador[0], \
                                                        Edad = int(excavador[2]), Energia = int(excavador[3]),
                                                         Fuerza = int(excavador[4]), Suerte = int(excavador[5]), \
                                                            Felicidad = int(excavador[6]), Arena_actual = Arena_inicio))
    return instancia_excavadores

def obtener_excavador_inutilizado(lista_excavadores_posibles, set_excavadores_en_uso):
    nuevo_objeto = None
    while not nuevo_objeto:
        excavador_random = choice(lista_excavadores_posibles)
        if excavador_random[0] not in {obj.nombre for obj in set_excavadores_en_uso}:
            return excavador_random
        
def instanciar_excavador(excavador, arena):
    if excavador[1] == "docencio":
        instancia_excavador = ExcavadorDocencio(Nombre = excavador[0], \
                                                    Edad = int(excavador[2]), Energia = int(excavador[3]),
                                                     Fuerza = int(excavador[4]), Suerte = int(excavador[5]), \
                                                        Felicidad = int(excavador[6]), Arena_actual = arena)
    elif excavador[1] == "tareo":
        instancia_excavador = ExcavadorTareo(Nombre = excavador[0], \
                                                    Edad = int(excavador[2]), Energia = int(excavador[3]),
                                                     Fuerza = int(excavador[4]), Suerte = int(excavador[5]), \
                                                        Felicidad = int(excavador[6]), Arena_actual = arena)
    elif excavador[1] == "hibrido":
        instancia_excavador = ExcavadorHibrido(Nombre = excavador[0], \
                                                    Edad = int(excavador[2]), Energia = int(excavador[3]),
                                                     Fuerza = int(excavador[4]), Suerte = int(excavador[5]), \
                                                        Felicidad = int(excavador[6]), Arena_actual = arena)
    return instancia_excavador

def instanciar_arena(arena):
    if arena[1] == "normal":
        instancia_arena = Arena_normal(Nombre = arena[0], Tipo = arena[1], \
                                    Rareza = int(arena[2]), Humedad = int(arena[3]), \
                                    Dureza = int(arena[4]), Estatica = int(arena[5]))
    elif arena[1] == "mojada":
        instancia_arena = Arena_mojada(Nombre = arena[0], Tipo = arena[1], \
                                    Rareza = int(arena[2]), Humedad = int(arena[3]), \
                                    Dureza = int(arena[4]), Estatica = int(arena[5]))
    elif arena[1] == "rocosa":
        instancia_arena = Arena_rocosa(Nombre = arena[0], Tipo = arena[1], \
                                    Rareza = int(arena[2]), Humedad = int(arena[3]), \
                                    Dureza = int(arena[4]), Estatica = int(arena[5]))
    elif arena[1] == "magnetica":
        instancia_arena = Arena_magnetica(Nombre = arena[0], Tipo = arena[1], \
                                    Rareza = int(arena[2]), Humedad = int(arena[3]), \
                                    Dureza = int(arena[4]), Estatica = int(arena[5]))
    return instancia_arena

def guardar_torneo():
    with open(os.path.join("DCCavaCava.txt"), "w") as datos:
        datos.write("2,2,2\n")
        datos.write("3,3,3")
        

