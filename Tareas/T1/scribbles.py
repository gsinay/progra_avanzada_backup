from datos import excavadores, arenas
from torneo import Torneo
from arenas import Arena_magnetica, Arena_mojada, Arena_normal, Arena_rocosa
from excavadores import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido
from random import choice
from parametros import ARENA_INICIAL, EXCAVADORES_INICIALES

print(arenas)
print()
excavadores_filtrados = [excavador for excavador in excavadores if excavadores[3] == "docencio"]
excavador_random = choice(excavadores_filtrados)
print(excavador_random)