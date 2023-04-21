from abc import ABC

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

    def __str__(self):
        return (f"Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion} \
                \nEnergia: {self.energia}\nFuerza: {self.fuerza}\
                \nSuerte: {self.suerte}\nFelicidad: {self.felicidad}")
    
class Tesoro(Item):
    def __init__(self, Calidad, Cambio, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.calidad = Calidad
        self.cambio = Cambio

    def __str__(self):
        return (f"Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion} \
                \nCalidad: {self.calidad}\nCambio: {self.cambio}")
    


