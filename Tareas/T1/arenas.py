from abc import ABC
from parametros import POND_ARENA_NORMAL
from random import randint
from datos import lista_items

class Arena(ABC):
    def __init__(self, Nombre: str, Tipo: str, Rareza: int, Humedad: int, \
                 Dureza: int, Estatica: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.nombre = Nombre
        self.tipo = Tipo
        self.__rareza = Rareza
        self.__humedad = Humedad
        self.__dureza = Dureza
        self.__estatica = Estatica
        self.items = lista_items 

    @property 
    def rareza(self):
        return self.__rareza
    @rareza.setter
    def rareza(self, rareza_nueva):
        self.__rareza = min(10, max(1, rareza_nueva))
        
    @property
    def humedad(self):
        return self.__humedad
    @humedad.setter
    def humedad(self, humedad_nueva):
        self.__humedad = min(10, max(1, humedad_nueva))

    @property
    def dureza(self):
        return self.__dureza
    @dureza.setter
    def dureza(self, dureza_nueva):
        self.__dureza = min(10, max(1, dureza_nueva))

    @property
    def estatica(self):
        return self.__estatica
    @estatica.setter
    def estatica(self, estatica_nueva):
        self.__estatica = min(10, max(1, estatica_nueva))

    def dificultad_arena(self):
        return round((self.__rareza + self.__humedad +
                       self.__dureza + self.__estatica) / 40, 2)

class ArenaNormal(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dificultad_arena(self):
        return round(POND_ARENA_NORMAL*super().dificultad_arena(), 2)
    
class ArenaMojada(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class ArenaRocosa(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def dificultad_arena(self):
        return round((self.rareza + self.humedad + 2*self.dureza + self.estatica) / 50, 2)
    
class ArenaMagnetica(Arena):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def randomizer(self):
        self.humedad = randint(1, 10)
        self.dureza = randint(1, 10)


