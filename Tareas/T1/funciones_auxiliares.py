from datos import excavadores, arenas
from arenas import Arena_magnetica, Arena_mojada, Arena_normal, Arena_rocosa
from excavadores import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido
from random import choice
from parametros import ARENA_INICIAL, EXCAVADORES_INICIALES

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
                                     Rareza = arena_inicial[2], Humedad = arena_inicial[3], \
                                    Dureza = arena_inicial[4], Estatica = arena_inicial[5])
    elif arena_inicial[1] == "mojada":
        arena_inicial = Arena_mojada(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                     Rareza = arena_inicial[2], Humedad = arena_inicial[3], \
                                    Dureza = arena_inicial[4], Estatica = arena_inicial[5])
    elif arena_inicial[1] == "rocosa":
        arena_inicial = Arena_rocosa(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                     Rareza = arena_inicial[2], Humedad = arena_inicial[3], \
                                    Dureza = arena_inicial[4], Estatica = arena_inicial[5])
    elif arena_inicial[1] == "magnetica":
        arena_inicial = Arena_magnetica(Nombre = arena_inicial[0], Tipo = arena_inicial[1], \
                                     Rareza = arena_inicial[2], Humedad = arena_inicial[3], \
                                    Dureza = arena_inicial[4], Estatica = arena_inicial[5])
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
                                                        Edad = excavador[2], Energia = excavador[3],
                                                         Fuerza = excavador[4], Suerte = excavador[5], \
                                                            Felicidad = excavador[6], Arena_actual = Arena_inicio))
        elif excavador[1] == "tareo":
            instancia_excavadores.add(ExcavadorTareo(Nombre = excavador[0], \
                                                        Edad = excavador[2], Energia = excavador[3],
                                                         Fuerza = excavador[4], Suerte = excavador[5], \
                                                            Felicidad = excavador[6], Arena_actual = Arena_inicio))
        elif excavador[1] == "hibrido":
            instancia_excavadores.add(ExcavadorHibrido(Nombre = excavador[0], \
                                                        Edad = excavador[2], Energia = excavador[3],
                                                         Fuerza = excavador[4], Suerte = excavador[5], \
                                                            Felicidad = excavador[6], Arena_actual = Arena_inicio))
    return instancia_excavadores

