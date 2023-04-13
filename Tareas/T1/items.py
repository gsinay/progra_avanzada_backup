from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, Nombre, Tipo, Descripcion, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.nombre = Nombre
        self.tipo = Tipo
        self.descripcion = Descripcion

class Consumible(Item):
    def __init__(self, Energia, Fuerza, Suerte, Felicidad, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.energia = Energia
        self.fuerza = Fuerza
        self.suerte = Suerte
        self.felicidad = Felicidad

