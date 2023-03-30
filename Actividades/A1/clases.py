from abc import abstractmethod, ABC
class Animal(ABC):
    
    def __init__(self, peso, nombre, *args, **kwargs):
        super().__init__(*kwargs, **kwargs)
        self.__energia = 100
        self.peso = peso
        self.nombre = nombre

    @abstractmethod
    def desplazarse(self):
        pass
    
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, cambio_energia):
        if self.__energia - cambio_energia < 0:
            self.__energia = 0
        else:
            self.__energia -= cambio_energia


class Terrestre(Animal, ABC):
    def __init__(self, cantidad_patas = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cantidad_patas = cantidad_patas

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 5
    
    def desplazarse(self) -> str:
       valor = self.energia_gastada_por_desplazamiento()
       self.energia -= valor
       return "caminando..."

      

    
class Acuatico(Animal, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 2
    
    def desplazarse(self) -> str:
        valor = self.energia_gastada_por_desplazamiento()
        self.__energia = self.__energia - valor
        return "nadando..."


class Perro(Terrestre):
    def __init__(self, raza, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.raza = raza
        self.cantidad_patas = 4

    def ladrar(self):
        return "guau guau"

class Pez(Acuatico):
    def __init__(self, color, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color

class Ornitorrinco(Acuatico, Terrestre):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    
    
    


if __name__ == '__main__':
    perro = Perro(nombre='Pongo', cantidad_patas=4, raza='Dalmata', peso=3)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2)

    print(perro.energia)
    alo = perro.desplazarse()
    print(perro.energia)
   
   #pez.desplazarse()
    #ornitorrinco.desplazarse()