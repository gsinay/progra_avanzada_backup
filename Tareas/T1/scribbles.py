from excavadores import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido
from funciones_auxiliares import generar_arena_inicial, generar_excavadores_iniciales, filtrar, \
obtener_excavador_inutilizado, instanciar_excavador, instanciar_arena
from datos import excavadores, arenas_normales
from random import choice

arena_random = choice(arenas_normales)
arena = instanciar_arena(arena_random)
print(arena.tipo, arena.nombre)


