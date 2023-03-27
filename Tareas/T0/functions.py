# Agregar los imports que estimen necesarios
import os

def encontrar_indices_vecinos(fila, columna, dimension):
    '''
    Funcion que retorna los indices vecinos de una posicion del tablero.
    Ej, si le paso los argumentos fila = 1, columna = 1, dimension = 5
    retorna [(0,1), (0,2), (1,0), (1,2)]
    Está citada en el readme de adonde la implementé

    '''
    indices = []
    if fila > 0:
        indices.append((fila-1, columna))
    if fila + 1 < dimension:
        indices.append((fila + 1, columna))
    if columna > 0:
        indices.append((fila, columna - 1))
    if columna + 1 < dimension:
        indices.append((fila, columna + 1))
    return indices


def cargar_tablero(nombre_archivo: str) -> list:
    with open(os.path.join("Archivos", nombre_archivo), "r") as lectura_de_archivo:
        lineas = lectura_de_archivo.readlines()
        dimension = int(lineas[0][0]) #dimension del tablero dado por el primer elemento
        lista_general = lineas[0][2:].split(",") #data sin primer elemento dimension y en format lista
        lista_final = []
        for i in range(0, len(lista_general), dimension): #cambia la lista a lista de listas cuadrada 
            posicion = i
            lista_final.append(lista_general[posicion : posicion + dimension])
        return lista_final


def guardar_tablero(nombre_archivo: str, tablero: list) -> None: 
    dimension = str(len(tablero))
    data_a_guardar = str(dimension + ",") #empezamos armando la string con el formato especificado
    for fila in tablero:
        for columna in fila:
            data_a_guardar += str(columna) +"," #concatenamos la data de la cordenada (fila, columna) a la string
    data_a_guardar = data_a_guardar[:-1] #borramos el ultimo coma 
    #en la siguiente linea ocupamos .rfind para no repetir la extension .txt
    with open(os.path.join("Archivos", nombre_archivo[ : nombre_archivo.rfind(".")]+"_sol.txt"), "w") as datos:
        datos.write(data_a_guardar)

def verificar_valor_bombas(tablero: list) -> int:
    cantidad_bombas_invalidas = 0
    for fila in tablero:
        for elemento in fila:
            if str(elemento).isnumeric(): #checkeando si es bomba
                if int(elemento) < 2 or int(elemento) > (2*len(tablero)) - 1:
                    cantidad_bombas_invalidas += 1 #sumando si se pasa de largo
    return cantidad_bombas_invalidas


def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:
    fila = coordenada[0]
    columna = coordenada[1]
    if fila < 0 or fila > (len(tablero) - 1):
        if columna < 0  or columna > (len(tablero-1)):
            print("ingresaste una coordenada invalida")
            return
    valor = tablero[fila][columna]
    if str(valor).isnumeric():
        valor_vertical_arriba = fila - 1
        valor_vertical_abajo = fila + 1
        valor_horizontal_derecha = columna + 1
        valor_horizontal_izquierda = columna -1

        conteo = 0
        #vamos a checkear los cuatro casos hasta que se tope a la celda o una tortuga
        while valor_vertical_arriba >= 0: 
            if tablero[valor_vertical_arriba][columna] == "T":
                break
            conteo += 1
            valor_vertical_arriba -= 1

        while valor_vertical_abajo < len(tablero):
            if tablero[valor_vertical_abajo][columna] == "T":
                break
            conteo += 1
            valor_vertical_abajo += 1
        
        while valor_horizontal_derecha < len(tablero):
            if tablero[fila][valor_horizontal_derecha] == "T":
                break
            conteo += 1
            valor_horizontal_derecha += 1

        while valor_horizontal_izquierda >= 0:
            if tablero[fila][valor_horizontal_izquierda] == "T":
                break
            conteo += 1
            valor_horizontal_izquierda -= 1
        
        return conteo + 1
    else:
        return 0 

def verificar_tortugas(tablero: list) -> int: 
    count = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            count_vecinos = 0 #contador de tortugas en indices vecinos
            elementos_vecinos = []
            if tablero[fila][columna] == "T":
                indices_vecinos = encontrar_indices_vecinos(fila, columna, len(tablero))
                for elemento in indices_vecinos:
                    if tablero[elemento[0]][elemento[1]] == "T":
                        count_vecinos += 1
            if count_vecinos >= 1:
                count += 1
    return count

def verificar_validad(tablero: list) -> bool:
    '''
    Esta funcion determina si el tablero viola las reglas:
    1.) relacionado al posicionamiento de tortugas
    2.) el alcanze de las bombas (sin contar si se ha quedado largo, solo si se restringio demasiado )
    '''
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            if str(tablero[fila][columna]).isnumeric():
                if verificar_alcance_bomba(tablero, (fila, columna)) < int(tablero[fila][columna]):
                    return False
            elif verificar_tortugas(tablero) > 0:
                return False
        return True

def solucionar_tablero(tablero: list) -> list:
    if obtener_solucion(tablero, 0, 0):
        return tablero
    return None

def checkear_solucion(tablero: list) -> bool:
    '''Esta funcion auxiliar chequea si el tablero se encuentra resuelto o no
    en cuanto al requerimiento de las bombas.'''
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            if str(tablero[fila][columna]).isnumeric():
                if verificar_alcance_bomba(tablero, (fila, columna)) != int(tablero[fila][columna]):
                    return False
    return True

def avanzar_posicion(tablero:list, fila: int, columna: int) -> tuple:
    '''Esta funcion toma la posicion en el tablero y retorna la siguiente moviendose
    primero horizontalmente y luego verticalmente'''
    if columna == len(tablero) - 1:
        return (fila + 1, 0)
    else:
        return (fila, columna + 1)

def obtener_solucion(tablero: list, columna: int, fila: int) -> bool:
    ''' funcion recursiva para solucionar tablero o establecer si no se puede'''
    #casos base
    if not verificar_validad(tablero):
        return False
    if checkear_solucion(tablero):
        return True
    if fila == len(tablero):
        return False

    fila_proxima, columna_proxima = avanzar_posicion(tablero, fila, columna)

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = 'T'
        #cambiamos un vacio a tortuga y llamamos recursion ahora con ese tablero
        if obtener_solucion(tablero, columna_proxima, fila_proxima):
            return True
        # si llega a un caso base falso, no era valido y cambiamos a vacio
        tablero[fila][columna] = '-'
        #si se cambia a vacio y tampoco se puede, retornamos falso ya que no hay solucion
        if obtener_solucion(tablero, columna_proxima, fila_proxima):
            return True
        return False
    #este else en caso que nos encontremos sobre tortuga o numero (no se pueden sobreponer elementos)
    else:
        return obtener_solucion(tablero, columna_proxima, fila_proxima)

            

#código de prueba     
# if __name__ == "__main__":
#     tablero_2x2 = [
#         ['-', 2],
#         ['-', '-']
#     ]
#     resultado = verificar_valor_bombas(tablero_2x2)
#     print(resultado)  # Debería ser 0

#     resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
#     print(resultado)  # Debería ser 3

#     tablero_resuelto = solucionar_tablero(tablero_2x2)
#     print(tablero_resuelto)

#     tablero_2x2_sol = [
#         ['T', 2],
#         ['-', '-']
#     ]

#     resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
#     print(resultado)  # Debería ser 2

#     resultado = verificar_tortugas(tablero_2x2_sol)
#     print(resultado)  # Debería ser 0




    