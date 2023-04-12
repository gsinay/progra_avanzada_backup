from abc import ABC, abstractmethod
from parametros import PROB_ENCONTRAR_ITEM, PROB_ENCONTRAR_CONSUMIBLE, PROB_ENCONTRAR_TESORO
from random import choices


with open("consumibles.csv", "r") as archivo: #haciendo lista de listas de los consumibles
    lineas = archivo.readlines()[1:]
    consumibles = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        consumibles.append(linea_limpia.split(","))
with open("tesoros.csv", "r") as archivo: #haciendo lista de listas de los tesoros
    lineas = archivo.readlines()[1:]
    tesoros = []
    for linea in lineas:
        linea_limpia = linea.strip("\n")
        tesoros.append(linea_limpia.split(","))

print(consumibles)
print(tesoros)




class Excavador(ABC):
    def __init__(self, Nombre, Edad, Energia, Fuerza, Suerte, \
                  Felicidad, Arena_actual, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
        self.nombre = Nombre
        self.__edad = Edad #los parametros privados los getearemos y setearemos para que no se pasen de los limites
        self.__energia = Energia
        self.__fuerza = Fuerza
        self.__suerte: Suerte
        self.__felicidad = Felicidad
        self.arena_actual = Arena_actual
        self.descandando = False
        self.dias_descanso = 0
    
    @property
    def edad(self): #getter de edad
        return self.__edad
    @edad.setter #setter de edad
    def edad(self, edad_nueva):
        self.__edad = min(60, max(18, edad_nueva))

    @property
    def energia(self): #getter de energia
        return self.__energia
    @energia.setter #setter de energia
    def energia(self, nueva_energia):
        self.__energia = min(100, max(0, nueva_energia))
    
    @property
    def fuerza(self): #getter de fuerza
        return self.__fuerza
    @fuerza.setter
    def fuerza(self, fuerza_nueva): #setter de fuerza
        self.__fuerza = min(10, max(1, fuerza_nueva))

    @property
    def suerte(self): #getter de suerte
        return self.__suerte
    @suerte.setter
    def suerte(self, suerte_nueva): #setter de suerte
        self.__suerte = min(10, max(1, suerte_nueva))

    @property
    def felicidad(self):#getter de felicidad
        return self.__felicidad
    @felicidad.setter
    def felicidad(self, felicidad_nueva): #setter de felicidad
        self.__felicidad = min(10, max(1, felicidad_nueva))
    


    
    
    @abstractmethod #metodo abstracto pues sera sobreescrito dependiendo de las clases hijas
    def cavar(self): 
        pass

    @abstractmethod #metodo abstracto pues sera sobreescrito dependiendo de las clases hijas
    def consumir(self):
        pass

    def descansar(self): #metodo para descansar
        dias_a_descansar  = int(self.__edad / 20)
        if self.__energia == 0: #si la energia es 0, se descansa
            descansando = True
        elif descansando == True and self.dias_descanso < dias_a_descansar: 
            #si se esta descansando y no se han cumplido los dias a descansar, se aumenta el contador de dias de descanso
            self.dias_descanso += 1
        elif descansando == True and self.dias_descanso == dias_a_descansar:
            #si se esta descansando y se han cumplido los dias a descansar, se termina el descanso
            self.dias_descanso = 0
            descansando = False
            self.__energia = 100

    def encontrar_item(self):
        prob_item = PROB_ENCONTRAR_ITEM * (self.__suerte / 10)
        #se calcula la probabilidad de encontrar un item
        encontrar_item = choices([True, False], weights=[prob_item, 1-prob_item], k=1)[0]
        encontrar_consumible = choices([True, False], \
                        weights=[PROB_ENCONTRAR_CONSUMIBLE, 1-PROB_ENCONTRAR_CONSUMIBLE], k=1)[0] 
        #seguir con esto
        pass
        
