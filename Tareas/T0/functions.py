# Agregar los imports que estimen necesarios
import os
from traceback import print_tb


def cargar_tablero(nombre_archivo: str) -> list:
    with open(os.path.join( "Archivos", nombre_archivo), "r") as lectura_de_archivo:
        lineas = lectura_de_archivo.readlines()
        dimension = int(lineas[0][0]) #dimension del tablero dado por el primer elemento
        lista_general = lineas[0][2:].split(",") #data sin primer elemento dimension y en format lista
        lista_final = []
        for i in range(0, len(lista_general), dimension): #cambia la lista a lista de listas cuadrada 
            posicion = i
            lista_final.append(lista_general[posicion : posicion + dimension])
        return lista_final


def guardar_tablero(nombre_archivo: str, tablero: list) -> None: ##ME FALTA ESCRIBIR ARCHIVO
    dimension = str(len(tablero))
    data_a_guardar = str(dimension + ",") #empezamos armando la string con el formato especificado
    for fila in tablero:
        for columna in fila:
            data_a_guardar += str(columna) +"," #concatenamos la data de la cordenada (fila, columna) a la string
    data_a_guardar = data_a_guardar[:-1] #borramos el ultimo coma 
    

def verificar_valor_bombas(tablero: list) -> int:
    cantidad_bombas_invalidas = 0
    for fila in tablero:
        for elemento in fila:
            if str(elemento).isnumeric(): #checkeando si es bomba
                if int(elemento) < 2 or elemento > (2*len(tablero)) - 1:
                    cantidad_bombas_invalidas += 1 #sumando si se pasa de largo
    return cantidad_bombas_invalidas



def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:
    valor = tablero[coordenada[0]][coordenada[1]]
    cuenta_vertical, cuenta_horizontal = 0, 0 
    if str(valor).isnumeric():
        #primero checkeamos verticalmente
        for numero_fila in range(len(tablero)):
            if numero_fila < coordenada[0]: #vemos si estamos arriba del caracter
                if str(tablero[numero_fila][coordenada[1]]) != "T": cuenta_vertical += 1
                else: cuenta_vertical = 1 #restauramos pues tenemos una tortuga hacia la celda
            elif numero_fila > coordenada[0]:
                if str(tablero[numero_fila][coordenada[1]]) != "T": cuenta_vertical += 1
                else: break
        #ahora checkeamos para los lados
        for numero_columna in range(len(tablero)):
            if numero_columna < coordenada[1]: #vemos si estamos a la izquierda del caracter
                if str(tablero[coordenada[0]][numero_columna]) != "T": cuenta_horizontal += 1
                else: cuenta_horizontal= 1 #restauramos pues tenemos una tortuga hacia la celda
            elif numero_columna > coordenada[1]:
                if str(tablero[coordenada[0]][numero_columna]) != "T": cuenta_horizontal += 1
        return cuenta_horizontal + cuenta_vertical + 1 #sumamos 1 para contar la celda misma
    else:
        return 0 

        


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



    