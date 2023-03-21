# Agregar los imports que estimen necesarios
import os
from traceback import print_tb


def cargar_tablero(nombre_archivo: str) -> list:
    with open(os.path.join( "Archivos", nombre_archivo), "r") as lectura_de_archivo:
        lineas = lectura_de_archivo.readlines()
        dimension = int(lineas[0][0]) #dimension del tablero dado por el primer elemento
        lineas = lineas[0][2:] #limpia la linea de data para excluir la informacion de la dimension del tablero
        lista_general = lineas.split(",") #splita la string a una lista de dimension n^2x1
        lista_final = []
        for i in range(0, len(lista_general), dimension): #cambia la lista a lista de listas cuadrada de dimensión del tablero
            posicion = i
            lista_final.append(lista_general[posicion : posicion + dimension])
        return lista_final


def guardar_tablero(nombre_archivo: str, tablero: list) -> None:
    dimension = str(len(tablero))
    data_a_guardar = str(dimension + ",") #empezamos armando la string a guardar con el formato especificado
    for fila in tablero:
        for columna in fila:
            data_a_guardar += str(columna) +"," #concatenamos la data de la cordenada (fila, columna) a la string
    data_a_guardar = data_a_guardar[:-1] #borramos el ultimo coma 
    


    pass


def verificar_valor_bombas(tablero: list) -> int:
    pass


def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:
    pass


def verificar_tortugas(tablero: list) -> int:
    pass


def solucionar_tablero(tablero: list) -> list:
    pass


if __name__ == "__main__":
    tablero_2x2 = [
        ['-', 2],
        ['-', '-']
    ]
    resultado = verificar_valor_bombas(tablero_2x2)
    print(resultado)  # Debería ser 0

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 3

    tablero_resuelto = solucionar_tablero(tablero_2x2)
    print(tablero_resuelto)

    tablero_2x2_sol = [
        ['T', 2],
        ['-', '-']
    ]

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 2

    resultado = verificar_tortugas(tablero_2x2_sol)
    print(resultado)  # Debería ser 0



    