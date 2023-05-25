from collections import defaultdict, deque
class Jugador:
    def __init__(self, nombre: str, velocidad: int) -> None:
        self.nombre = nombre
        self.velocidad = velocidad
    
    def __repr__(self) -> None:
        return f'Jugador: {self.nombre}, Velocidad: {self.velocidad}'
class Equipo:
    def __init__(self) -> None:
        self.jugadores = dict()
        self.dict_adyacencia = defaultdict(set)
    
    def agregar_jugador(self, id_jugador: int, jugador: Jugador) -> bool:
        if len(self.jugadores) == 0:
            self.jugadores[id_jugador] = jugador
            return True
        elif id_jugador in self.jugadores:
            return False
        else:
            self.jugadores[id_jugador] = jugador
            return True
   
    def agregar_vecinos(self, id_jugador: int, vecinos: list[int]) -> int:
        count = 0
        if id_jugador not in self.jugadores:
            return -1
        else:
            for vecino in vecinos:
                if vecino not in self.dict_adyacencia[id_jugador]:
                    self.dict_adyacencia[id_jugador].add(vecino)
                    count += 1
        return count
       
    def mejor_amigo(self, id_jugador: int) -> Jugador:
        jugador = self.jugadores[id_jugador]
        numero = 1000000 #numero grande
        if len(self.dict_adyacencia[id_jugador]) == 0:
            return None
        
        for id_vecino in self.dict_adyacencia[id_jugador]:
            velocidad_vecino = self.jugadores[id_vecino].velocidad
            velocidad_jugador =  self.jugadores[id_jugador].velocidad
            resta = abs(velocidad_jugador - velocidad_vecino)
            if resta < numero:
                numero = resta
                id_jugador_mejor_amigo = id_vecino
        return self.jugadores[id_jugador_mejor_amigo]
    def peor_compañero(self, id_jugador: int) -> Jugador:
        jugador = self.jugadores[id_jugador]
        numero = -1000000 #numero chico
        if len(self.dict_adyacencia[id_jugador]) == 0:
            return None
        
        for id_compañero in self.jugadores:
            velocidad_compañero = self.jugadores[id_compañero].velocidad
            velocidad_jugador =  self.jugadores[id_jugador].velocidad
            resta = abs(velocidad_compañero - velocidad_jugador)
            if resta > numero:
                numero = resta
                id_jugador_peor_compañero = id_compañero
        return self.jugadores[id_jugador_peor_compañero]
    
    def peor_conocido(self, id_jugador: int) -> Jugador:
        cola = deque()
        visitados = list()
        cola.append(id_jugador)
        while len(cola) > 0:
            jugador = cola.popleft()
            visitados.append(jugador)
            for jugador_vecino in self.dict_adyacencia[jugador]:
                if jugador_vecino not in visitados:
                    cola.append(jugador_vecino)
        visitados.remove(id_jugador)
        jugador = self.jugadores[id_jugador]
        numero = -10000 #numero chico
        if len(visitados) == 0:
            return None
        
        for conocido in visitados:
            jugador_conocido = self.jugadores[conocido]
            resta = abs (jugador_conocido.velocidad - jugador.velocidad)
            if resta > numero:
                numero = resta
                jugador_retorno = jugador_conocido
        return jugador_retorno
        
    def distancia(self, id_jugador_1: int, id_jugador_2: int) -> int:
        if id_jugador_1 == id_jugador_2:
            return 0
        
        cola = deque()
        visitados = [[]]
        numero_camino = 0
        cola.append(id_jugador_1)
        if len(self.dict_adyacencia[id_jugador_1]) > 0:
            while len(cola) > 0:
                jugador = cola.pop()
                if jugador != id_jugador_1:
                    visitados[numero_camino].append(jugador)
                for jugador_vecino in self.dict_adyacencia[jugador]:
                    if jugador_vecino not in visitados[numero_camino]:
                        cola.append(jugador_vecino)
                if jugador == id_jugador_2:
                    numero_camino += 1
                    visitados.append([])
        else:
            return - 1
        
        for camino in visitados:
            if id_jugador_2 not in camino:
                visitados.remove(camino)
        if len(visitados) == 0:
            return -1
        
        minimo = 100000 #numero grande
        for camino in visitados:
            if len(camino) < minimo:
                minimo = len(camino)
        return minimo
        
        
    
if __name__ == '__main__':
    equipo = Equipo()
    jugadores = {
        0: Jugador('Alonso', 1),
        1: Jugador('Alba', 3),
        2: Jugador('Alicia', 6),
        3: Jugador('Alex', 10)
    }
    adyacencia = {
        0: [1],
        1: [0, 2],
        2: [1],
    }
    for idj, jugador in jugadores.items():
        equipo.agregar_jugador(id_jugador=idj, jugador=jugador)
    for idj, vecinos in adyacencia.items():
        equipo.agregar_vecinos(id_jugador=idj, vecinos=vecinos)
        
    
    
    print(f'El mejor amigo de Alba es {equipo.mejor_amigo(1)}') 
    print(f'El peor compañero de Alex es {equipo.peor_compañero(3)}')
    print(f'El peor conocido de Alonso es {equipo.peor_conocido(0)}')
    
    print(f'La distancia entre Alicia y Alonso es {equipo.distancia(2, 0)}')
    print(f'La distancia entre Alba y Alex es {equipo.distancia(1, 3)}')



    equipo = Equipo()
    equipo.jugadores = {
            0: Jugador('Alan', 2),
            1: Jugador('Alberto', 3),
            2: Jugador('Alejandra', 5),
            3: Jugador('Alex', 8),
            4: Jugador('Alonso', 13),
            5: Jugador('Alba', 21),
            6: Jugador('Alicia', 34),
            7: Jugador('Alfredo', 55),
            8: Jugador('Alma', 16),
            9: Jugador('Aldo', 89)
        }
    adyacencia = {
            0: {1},
            1: {0, 2, 3},
            2: {1, 3},
            3: {1},
            4: {5},
            5: {4, 6},
            6: {4, 5},
            7: {8},
            8: {9},
            9: set()
        }

    equipo.dict_adyacencia = defaultdict(set)
    for key, value in adyacencia.items():
        equipo.dict_adyacencia[key] = value
    print(equipo.distancia(0 ,))
