from abc import abstractmethod, ABC
class Animal(ABC):

    id = 0
    
    def __init__(self, peso, nombre, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__energia = 100
        self.peso = peso
        self.nombre = nombre
        self.identificador = Animal.id
        Animal.id += 1

    @abstractmethod
    def desplazarse(self):
        pass
    
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, nueva_energia):
        if nueva_energia < 0:
            self.__energia = 0
        else:
            self.__energia = nueva_energia


class Terrestre(Animal, ABC):
    def __init__(self, cantidad_patas, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cantidad_patas = cantidad_patas

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 5
    
    def desplazarse(self) -> str:
       valor = self.energia_gastada_por_desplazamiento()
       self.energia = self.energia - valor
       return "caminando..."

      

    
class Acuatico(Animal, ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def energia_gastada_por_desplazamiento(self) -> int:
        return self.peso * 2
    
    def desplazarse(self) -> str:
        valor = self.energia_gastada_por_desplazamiento()
        self.energia = self.energia - valor
        return "nadando..."


class Perro(Terrestre):
    def __init__(self, raza, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.raza = raza
        

    def ladrar(self):
        return "guau guau"

class Pez(Acuatico):
    def __init__(self, color, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color
    
    def nadar(self):
        return "moviendo aleta"

class Ornitorrinco(Terrestre, Acuatico):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
   
    def desplazarse(self) -> str:
        valor_tierra =  Terrestre.energia_gastada_por_desplazamiento(self)
        valor_agua = Acuatico.energia_gastada_por_desplazamiento(self)
        promedio = round((valor_tierra + valor_agua) / 2)
        self.energia = self.energia - promedio
        return "caminando...nadando..." 


    


if __name__ == '__main__':

   

    perro = Perro(nombre='Pongo', raza='Dalmata', peso=3, cantidad_patas = 4)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2, cantidad_patas = 6)
    