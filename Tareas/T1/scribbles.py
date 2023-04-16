from excavadores import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido
from funciones_auxiliares import generar_arena_inicial, generar_excavadores_iniciales, filtrar, \
obtener_excavador_inutilizado, instanciar_excavador, instanciar_arena
from datos import excavadores, arenas_normales
from random import choice

My_list = [*range(10, 20, 1)]
My_list.append("x")
  
# Print the list
print(My_list)