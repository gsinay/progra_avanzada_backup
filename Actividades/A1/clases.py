from abc import abstractmethod, ABC
class Animal(ABC):
    
    def __init__(self, peso, nombre, *args, **kwargs):
        super().__init__(*kwargs, **kwargs)
        self.__energia = 100
        
    @abstractmethod
    def desplazarse(self):
        pass
    
    @property
    def get_energia(self):
        return self.__energia
    
    @get_energia
    def set_energia(self, cambio_energia):
        if self.__energia - cambio_energia < 0:
            self.__energia = 0
        else:
            self.__energia -= cambio_energia


class Terrestre(Animal, ABC):
    def __init__(self, cantidad_patas, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cantidad_patas = cantidad_patas

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 5
    
    def desplazarse(self) -> str:
       self.set_energia(self.energia_gastada_por_desplazamiento())
       return "caminando..."



    
class Acuatico(Animal, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 2
    
    def desplazarse(self) -> str:
        self.set_energia(self.energia_gastada_por_desplazamiento())
        return "nadando..."


class Perro:
    def __init__(self, raza, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.raza = raza

    def ladrar(self):
        return "guau guau"

class Pez:
    def __init__(self, color, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color

class Ornitorrinco:
    pass


if __name__ == '__main__':
    perro = Perro(nombre='Pongo', raza='Dalmata', peso=3)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2)

    perro.desplazarse()
    pez.desplazarse()
    ornitorrinco.desplazarse()