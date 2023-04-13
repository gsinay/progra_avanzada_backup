from abc import ABC, abstractmethod
from parametros import PROB_ENCONTRAR_ITEM, PROB_ENCONTRAR_CONSUMIBLE, PROB_ENCONTRAR_TESORO, \
FELICIDAD_ADICIONAL_DOCENCIO, FUERZA_ADICIONAL_DOCENCIO, ENERGIA_PERDIDA_DOCENCIO
from random import choices
from datos import tesoros, consumibles

class Excavador(ABC):
    def __init__(self, Nombre, Edad, Energia, Fuerza, Suerte, \
                  Felicidad, Arena_actual, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.nombre = Nombre
        self.__edad = Edad #los parametros privados los getearemos y setearemos para que no se pasen de los limites
        self.__energia = Energia
        self.__fuerza = Fuerza
        self.__suerte = Suerte
        self.__felicidad = Felicidad
        self.arena_actual = Arena_actual
        self.descansando = False
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

    @abstractmethod
    def cavar(self):
        pass

    @abstractmethod
    def consumir(self):
        pass


    def descansar(self): #metodo para descansar
        dias_a_descansar  = int(self.__edad / 20)
        if self.__energia == 0 and self.descansando == False: #si la energia es 0, se descansa
            self.descansando = True
        if self.descansando == True and self.dias_descanso < dias_a_descansar: 
            #si se esta descansando y no se han cumplido los dias a descansar, se aumenta el contador de dias de descanso
            self.dias_descanso += 1
        elif self.descansando == True and self.dias_descanso == dias_a_descansar:
            #si se esta descansando y se han cumplido los dias a descansar, se termina el descanso
            self.dias_descanso = 0
            self.descansando = False
            self.__energia = 100

    def encontrar_item(self):
        prob_item = PROB_ENCONTRAR_ITEM * (self.__suerte / 10)
        #se calcula la probabilidad de encontrar un item
        encontrar_item = choices([True, False], weights=[prob_item, 1-prob_item], k=1)[0]
        if encontrar_item or self.arena_actual.tipo == "mojada": 
            encontrar_consumible = choices([True, False], \
                            weights=[PROB_ENCONTRAR_CONSUMIBLE, 1-PROB_ENCONTRAR_CONSUMIBLE], k=1)[0] 
            if encontrar_consumible:
                return # llenar con ITEM-CONSUMIBLE cuando clase esté lista
            else:
                return # llenar con ITEM-TESORO cuando clase esté lista
            
    def gastar_energia(self):
        energia_gastada = int((10 / self.__fuerza) + (self.__edad / 6))
        return energia_gastada

    

class ExcavadorDocencio(Excavador):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def cavar(self):
        if self.descansando == False:
            metros_cavados = round((30/self.edad + (self.felicidad + 2*self.fuerza)/10) * \
                                    (1/10 * 5), 2) #ojo con esto mas adelante
            self.energia -= self.gastar_energia()
            self.felicidad += FELICIDAD_ADICIONAL_DOCENCIO
            self.fuerza += FUERZA_ADICIONAL_DOCENCIO
            self.energia -= ENERGIA_PERDIDA_DOCENCIO
            self.descansar() #se checkea si se tiene que partir descansando
            return metros_cavados
        else:
            self.descansar() #si se esta descansando, se sigue descansando o se termina de descansar
            return 0
    
    def calcular_gasto_energia_total(self):
        return self.gastar_energia() +  ENERGIA_PERDIDA_DOCENCIO
    
    def consumir(self, consumibe): #completar cuando esté items listos
        pass

class ExcavadorTareo(Excavador):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def cavar(self):
        if self.descandando == False:
            metros_cavados = round((30/self.__edad + (self.felicidad + 2*self.fuerza)/10) * \
                                    (1/10 * self.arena_actual.dificultad_arena), 2) #ojo con esto mas adelante
            self.energia -= self.gastar_energia()
            self.descansar() #se checkea si se tiene que partir descansando
            return metros_cavados
        else:
            self.descansar() #si se esta descansando, se sigue descansando o se termina de descansar
            return 0 
        
    def consumir(self, consumibe): #completar cuando esté items listos
        pass

class ExcavadorHibrido(ExcavadorDocencio, ExcavadorTareo):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def cavar(self):
        perdida_energia = int((ExcavadorDocencio.calcular_gasto_energia_total(self) + \
                            ExcavadorTareo.gastar_energia(self)) / 2)
        self.energia -= perdida_energia
        metros_cavados = round((30/self.edad + (self.felicidad + 2*self.fuerza)/10) * \
                                (1/10 * self.arena_actual.dificultad_arena), 2) #ojo con esto mas adelante
        return metros_cavados

gabe = ExcavadorDocencio(Nombre = "Gabe", Edad = 60, Fuerza = 10, Suerte = 10, Felicidad = 10, Energia = 30, Arena_actual = "seca")
for i in range (0,40):
    print(gabe.energia)
    print(f"se han cavado {gabe.cavar()} metros y la energia ahora es {gabe.energia}")


