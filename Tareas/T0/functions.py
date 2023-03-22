# Agregar los imports que estimen necesarios
import os

def valor_derecha(tablero: list, posicion : tuple) -> str: #retorna valor de la derecha de la celda
    return str(tablero[posicion[0]][posicion[1] + 1])

def valor_izquierda(tablero: list, posicion : tuple) -> str: #retorna valor de la izquierda de la celda
    return tablero[posicion[0]][posicion[1] - 1]

def valor_abajo(tablero: list, posicion : tuple) -> str: #retorna valor de abajo de la celda
    return tablero[posicion[0] + 1][posicion[1]]
def valor_abajo(tablero: list, posicion : tuple) -> str: #retorna valor de arriba de la celda
    return tablero[posicion[0] - 1][posicion[1]]

def encontrar_indices_vecinos(fila, columna, dimension):
    indices = []
    if fila > 0:
        indices.append((fila-1, columna))
    elif fila + 1 < dimension:
        indices.append((fila + 1, columna))
    if columna > 0:
        indices.append((fila, columna-1))
    elif columna + 1 < dimension:
        indices.append((fila, columna + 1))
    return indices



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
    cuenta_vertical, cuenta_horizontal = 0, 0 #variables auxilar que cuentan tortugas 
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
            if count_vecinos > 1:
                count += 1
    return count


            
    
                



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



    