import os
from functions import cargar_tablero, guardar_tablero, verificar_valor_bombas 
from functions import verificar_alcance_bomba, verificar_tortugas, solucionar_tablero, checkear_solucion
from tablero import imprimir_tablero

menu_principal = True #variable para ver si estamos corriendo el programa
menu_acciones = True #variable para ver si estamos dentro del menu de archivo especifico

while menu_principal:
    lista_de_archivos = os.listdir("Archivos")

    print('''
    Bienvenido al menú de Inicio. ingrese el nombre del archivo a cargar incluyendo su extensión! 
    Debe ser alguno de los siguientes: \n
    ''')
    print(lista_de_archivos)
    nombre_archivo = input()
    if nombre_archivo in lista_de_archivos:
        tablero = cargar_tablero(nombre_archivo)
        while menu_acciones:
            print(f" \n Archivo Encontrado: {nombre_archivo}. ¿Que desea hacer? Ingrese el numero de la accion correspondiente")
            print('''
            1.) Mostrar Tablero
            2.) Validar bombas y tortugas
            3.) Validar solución
            4.) Solucionar tablero
            5.) Salir del programa
            ''')
            accion = int(input())
            if accion not in (1,2,3,4,5):
                print("No ingresó una acción valida, intente denuevo \n")
            else:
                if accion == 1:
                    print(f"Tablero para {nombre_archivo}")
                    imprimir_tablero(tablero)
                elif accion == 2:
                    if verificar_valor_bombas(tablero) == 0 and verificar_tortugas(tablero) == 0:
                        print("\n El tablero es valido!")
                    else:
                        print("\n El tablero es invalido :( sad momo")
                elif accion == 3:
                    if checkear_solucion(tablero) == True and verificar_tortugas(tablero) == 0:
                        print("\n El tablero esta solucionado")
                    else:
                        print("\n El tablero no esta solucionado")
                elif accion == 4:
                    if checkear_solucion(tablero) == True and verificar_tortugas(tablero) == 0:
                        print("\n El tablero esta solucionado, no hay nada que hacer")
                    else:
                        tablero_solucionado = solucionar_tablero(tablero)
                        if tablero_solucionado!= None:
                            guardar_tablero(nombre_archivo, tablero_solucionado)
                            print(f"¡Hay solucion! Se ha guardado en la carpeta Archivos y se ve así:")
                            imprimir_tablero(tablero_solucionado)
                        else:
                            print("No hay solucion :(. Favor cargar otro tablero")
                elif accion == 5:
                    print("Se ha terminado el programa. Si quiere volver a ocuparlo corralo nuevamente")
                    menu_acciones = False
                    menu_principal = False
    else:
        print('''
        No se encontró ese archivo, verifica que existe en la carpeta Archivos y que 
        escribiste bien el nombre. Te recomiendo hacer copy-pase tal cual aparece en el directorio.
        Se cerrará el programa, vuelvelo a correr para intentar denuevo
        ''')
        menu_principal = False
    
