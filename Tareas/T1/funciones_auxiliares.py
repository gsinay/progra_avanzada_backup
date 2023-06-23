
from arenas import ArenaMagnetica, ArenaMojada, ArenaNormal, ArenaRocosa, Arena
from excavadores import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido, Excavador
from random import choice
                                                                                                    
def filtrar(lista: list, filtro: str):
    lista_a_retornar = []
    for elemento in lista:
        if elemento[1] == filtro:
            lista_a_retornar.append(elemento)
    return lista_a_retornar

def instanciar_excavador(excavador: list, arena: Arena):
    if excavador[1] == "docencio":
        instancia_excavador = ExcavadorDocencio(Nombre = excavador[0], 
                                                    Edad = int(excavador[2]), 
                                                    Energia = int(excavador[3]),
                                                    Fuerza = int(excavador[4]),
                                                    Suerte = int(excavador[5]), 
                                                    Felicidad = int(excavador[6]), 
                                                    Arena_actual = arena)
    elif excavador[1] == "tareo":
        instancia_excavador = ExcavadorTareo(Nombre = excavador[0], 
                                                    Edad = int(excavador[2]),
                                                    Energia = int(excavador[3]),
                                                    Fuerza = int(excavador[4]), 
                                                    Suerte = int(excavador[5]), 
                                                    Felicidad = int(excavador[6]),
                                                    Arena_actual = arena)
    elif excavador[1] == "hibrido":
        instancia_excavador = ExcavadorHibrido(Nombre = excavador[0], 
                                                    Edad = int(excavador[2]), 
                                                    Energia = int(excavador[3]),
                                                    Fuerza = int(excavador[4]), 
                                                    Suerte = int(excavador[5]), 
                                                    Felicidad = int(excavador[6]), 
                                                    Arena_actual = arena)
    return instancia_excavador

def instanciar_arena(arena: list):
    diccionario_arenas = {"normal": ArenaNormal, "rocosa": ArenaNormal, "mojada": ArenaMojada, "magnetica": ArenaMagnetica}
    instancia_arena = diccionario_arenas[arena[1]](Nombre = arena[0],
                                                    Tipo = arena[1],
                                                    Rareza = int(arena[2]),
                                                    Humedad = int(arena[3]),
                                                    Dureza = int(arena[4]),
                                                    Estatica = int(arena[5]))
    return instancia_arena

        
def obtener_excavador_inutilizado(lista_excavadores_posibles: list, set_excavadores_en_uso: set):
    nuevo_objeto = None
    #primero vemos si tenemos alguno que no este en uso, es decir, que hayan disponibles:
    nombres_en_uso = {obj.nombre for obj in set_excavadores_en_uso}
    existente = False
    for excavador in lista_excavadores_posibles:
        if excavador[0] not in nombres_en_uso:
            existente = True
    if not existente:
        return False   #en caso que no hayn excavadores disponibles retornamos False
    while not nuevo_objeto:
        #elegimos un excavador random hasta que lleguemos a uno que no este en uso, no es muy eficiente pero sirve
        excavador_random = choice(lista_excavadores_posibles)
        if excavador_random[0] not in {obj.nombre for obj in set_excavadores_en_uso}: 
            return excavador_random
        

        

