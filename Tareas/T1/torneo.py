from  arenas import Arena, Arena_normal, Arena_mojada, Arena_rocosa, Arena_magnetica
from excavadores import ExcavadorDocencio, ExcavadorHibrido, ExcavadorTareo
from datos import arenas_mojadas, arenas_rocosas, arenas_magneticas,\
arenas_normales, excavadores
from parametros import PROB_LLUVIA, PROB_TERREMOTO, PROB_DERRUMBE, METROS_PERDIDOS_DERRUMBE, \
PROB_INICIAR_EVENTO, DIAS_TOTALES_TORNEO, METROS_META, ARENA_INICIAL, EXCAVADORES_INICIALES
from random import choices, randint, choice
from funciones_auxiliares import filtrar, obtener_excavador_inutilizado, instanciar_excavador, \
instanciar_arena



class Torneo:
    def __init__(self, Arena: Arena, Eventos: set, Equipo: set, \
                 Mochila: list, Metros_cavados: float,  \
                 Dias_transcurridos: int,  \
                 *args, **kwargs) -> None: 
        self.arena = Arena
        self.eventos = Eventos
        self.equipo = Equipo
        self.mochila = Mochila
        self.metros_cavados = Metros_cavados 
        self.meta = METROS_META
        self.dias_transcurridos = Dias_transcurridos
        self.dias_totales = DIAS_TOTALES_TORNEO

    @property
    def metros_cavados(self):
        return self.__metros_cavados
    @metros_cavados.setter
    def metros_cavados(self, metros_nuevos):
        if metros_nuevos < 0:
            self.metros_cavados = 0
        else:
            self.__metros_cavados = metros_nuevos

    def simular_dia(self):
        print(f" Dia {self.dias_transcurridos} de {self.dias_totales} ")
        print("-----------------------------------------")
        if self.arena.tipo == "magnetica": #enunciado las arenas magneticas no tienen eventos especiales
            self.arena.randomizer()
        suma_metros = 0
        suma_consumibles = 0
        suma_tesoros = 0
        for excavador in self.equipo: #se recorre el equipo 
            metros_cavados = excavador.cavar()
            print(f"{excavador.nombre} ha cavado {metros_cavados} metros")
            suma_metros += metros_cavados
            item = excavador.encontrar_item()
            if item != None:
                print(f"{excavador.nombre} ha encontrado un {item.nombre}")
                print(f"el item es un {item.nombre} de tipo {item.tipo}")
                if item.tipo == "Tesoro":
                    suma_tesoros += 1
                elif item.tipo == "Consumible":
                    suma_consumibles += 1
                self.mochila.append(item)
        self.metros_cavados += round(suma_metros, 2)
        print(f"Se han cavado {suma_metros} metros en total")
        print(f"Se han encontrado {suma_tesoros + suma_consumibles} items en total")
        print(f"- {suma_consumibles} consumibles")
        print(f"- {suma_tesoros} tesoros")


        evento = choices([True, False], weights=[PROB_INICIAR_EVENTO, 1-PROB_INICIAR_EVENTO], k=1)[0]
        if evento == True:
            self.iniciar_evento()
        
        self.dias_transcurridos += 1
        

    def mostrar_estado(self):
        print(("*** Estado Torneo ***").center(85))
        print("-"*85)
        print(f"Dia actual: {self.dias_transcurridos}")
        print(f"Tipo de arena: {self.arena.tipo}")
        print(f"Metros cavados: {self.metros_cavados} / {self.meta}")
        print("-"*85)
        print(("*** Excavadores ***").center(85))
        print("-"*85)
        print(f"   NOMBRE     |    TIPO      |   ENERGIA    |   FUERZA     |   SUERTE     |  FELICIDAD ")
        for excavador in self.equipo:
            print(f"{excavador.nombre: ^13s} | {excavador.tipo: ^12s} | {excavador.energia: ^12d} | {excavador.fuerza: ^12d} | {excavador.suerte: ^12d} | {excavador.felicidad} ")
        
    def ver_mochila(self):
        print(self.mochila)
        print(("*** Menu Items ***").center(100))
        print("-"*100)
        print(f"          NOMBRE                  |      TIPO      |                            DESCRIPCION                            ")
        print("-"*100)
        for indice_item in range(0,len(self.mochila)):
            print(f"[{indice_item + 1}] {self.mochila[indice_item].nombre: ^29s} | {self.mochila[indice_item].tipo: ^14s} | {self.mochila[indice_item].descripcion: ^64s}")

    def usar_consumible(self, consumible):
        for excavador in self.equipo:
            excavador.consumir(consumible)
        self.mochila.remove(consumible)

    def abrir_tesoro(self, tesoro):
        if tesoro.calidad == "1": #vamos a agregar un trabajador
            if tesoro.cambio.lower() == "docencio":
                excavadores_filtrados = filtrar(excavadores, "docencio")
                excavador_random = obtener_excavador_inutilizado(excavadores_filtrados)
                self.equipo.add(instanciar_excavador(excavador_random, self.arena))
            elif tesoro.cambio.lower() == "tareo":
                excavadores_filtrados = filtrar(excavadores, "tareo")
                excavador_random = obtener_excavador_inutilizado(excavadores_filtrados)
                self.equipo.add(instanciar_excavador(excavador_random, self.arena))
            elif tesoro.cambio.lower() == "hibrido":
                excavadores_filtrados = filtrar(excavadores, "hibrido")
                excavador_random = obtener_excavador_inutilizado(excavadores_filtrados)
                self.equipo.add(instanciar_excavador(excavador_random, self.arena))
        else:
            if tesoro.cambio.lower()== "normal":
                arena_random = choice(arenas_normales)
                self.arena = instanciar_arena(arena_random)
            elif tesoro.cambio.lower() == "mojada":
                arena_random = choice(arenas_mojadas)
                self.arena = instanciar_arena(arena_random)
            elif tesoro.cambio.lower() == "rocosa":
                arena_random = choice(arenas_rocosas)
                self.arena = instanciar_arena(arena_random)
            elif tesoro.cambio.lower() == "magnetica":
                arena_random = choice(arenas_magneticas)
                self.arena = instanciar_arena(arena_random)
        self.mochila.remove(tesoro)


    def iniciar_evento(self):
        evento = choices(["Lluvia", "Terremoto", "Derrumbe"], weights=[PROB_LLUVIA, \
                    PROB_TERREMOTO, PROB_DERRUMBE], k=1)[0]
        if evento == "Lluvia" and self.arena.tipo == "normal":
            numero_random = randint(1, len(arenas_mojadas)- 1) #elegimos arena mojada random
            self.arena = Arena_mojada(Nombre = arenas_mojadas[numero_random][0], \
                                        Tipo = arenas_mojadas[numero_random][1], \
                                        Rareza = arenas_mojadas[numero_random][2], \
                                        Humedad = arenas_mojadas[numero_random][3], \
                                        Dureza = arenas_mojadas[numero_random][4], \
                                        Estatica = arenas_mojadas[numero_random][5])
            print(f"Se ha producido una lluvia, la arena normal se ha mojado y la nueva arena es {self.arena.nombre}")
        elif evento.lower() == "lluvia" and self.arena.tipo.lower()== "rocosa":
            numero_random = randint(1, len(arenas_magneticas)- 1) #elegimos arena magnetica random
            self.arena = Arena_magnetica(Nombre = arenas_magneticas[numero_random][0], \
                                        Tipo = arenas_magneticas[numero_random][1], \
                                        Rareza = arenas_magneticas[numero_random][2], \
                                        Humedad = arenas_magneticas[numero_random][3], \
                                        Dureza = arenas_magneticas[numero_random][4], \
                                        Estatica = arenas_magneticas[numero_random][5])
            print(f"Se ha producido una lluvia, la arena rocosa se ha electrificado y la nueva arena es {self.arena.nombre}")
        
        elif evento.lower() == "terremoto" and self.arena.tipo.lower() == "normal":
            numero_random = randint(1, len(arenas_rocosas)- 1) #elegimos arena rocosa random
            self.arena = Arena_rocosa(Nombre = arenas_rocosas[numero_random][0], \
                                        Tipo = arenas_rocosas[numero_random][1], \
                                        Rareza = arenas_rocosas[numero_random][2], \
                                        Humedad = arenas_rocosas[numero_random][3], \
                                        Dureza = arenas_rocosas[numero_random][4], \
                                        Estatica = arenas_rocosas[numero_random][5])
            print(f"Se ha producido un terremoto, la arena normal se ha vuelto rocosa y la nueva arena es {self.arena.nombre}")
        elif evento.lower() == "terremoto" and self.arena.tipo.lower() == "mojada":
            numero_random = randint(1, len(arenas_magneticas)- 1) #elegimos arena rocosa random
            self.arena = Arena_magnetica(Nombre = arenas_magneticas[numero_random][0], \
                                        Tipo = arenas_magneticas[numero_random][1], \
                                        Rareza = arenas_magneticas[numero_random][2], \
                                        Humedad = arenas_magneticas[numero_random][3], \
                                        Dureza = arenas_magneticas[numero_random][4], \
                                        Estatica = arenas_magneticas[numero_random][5])
            print(f"Se ha producido un terremoto, la arena mojada se ha vuelto magnetica y la nueva arena es {self.arena.nombre}")
        
        elif evento.lower() == "derrumbe":
            self.metros_cavados -= METROS_PERDIDOS_DERRUMBE
            print(f"Se ha producido un derrumbe, se han perdido {METROS_PERDIDOS_DERRUMBE} metros")
            numero_random = randint(1, len(arenas_normales)- 1) #elegimos arena normal random
            self.arena = Arena_normal(Nombre = arenas_normales[numero_random][0], \
                                        Tipo = arenas_normales[numero_random][1], \
                                        Rareza = arenas_normales[numero_random][2], \
                                        Humedad = arenas_normales[numero_random][3], \
                                        Dureza = arenas_normales[numero_random][4], \
                                        Estatica = arenas_normales[numero_random][5])
            print(f"La arena se ha vuelto normal y la nueva arena es {self.arena.nombre}")

    def __str__(self):
        return (f"jugando en Arena: {self.arena.nombre}, con {self.mochila} en la mochila y el {self.equipo} equipo ")
 
