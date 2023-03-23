import os
from functions import cargar_tablero, guardar_tablero, verificar_valor_bombas, verificar_alcance_bomba, verificar_tortugas, solucionar_tablero, checkear_solucion
from tablero import imprimir_tablero

menu_principal = True #variable para ver si estamos corriendo el programa
while menu_principal:
    lista_de_archivos = os.listdir("Archivos")
    print(lista_de_archivos)
    print('''
    Bienvenido al menú de Inicio. ingrese el nombre del archivo a cargar incluyendo su extensión!
    ''')
    nombre = input()
    if nombre in lista_de_archivos:
        print(f"success")
        break
    else:
        print('''
        No se encontró ese archivo, verifica que existe en la carpeta Archivos y que 
        escribiste bien el nombre. Te recomiendo hacer copy-pase tal cual aparece en el directorio.
        Se cerrará el programa, vuelvelo a correr para intentar denuevo
        ''')
        menu_principal = False
    


    # lista_de_archivos = os.listdir("Archivos")
    # dicionario_de_archivos = dict(enumerate(lista_de_archivos))
    # for numero, nombre_de_archivo in dicionario_de_archivos.items():
    #     print(f"{str(numero)}, : {str(nombre_de_archivo)} \n")
    # archivo = input("ingrese su numero")
    # if archivo.isdigit():

#with open(os.path.join("Archivos", "probandoo.txt"), "w") as datos:
    #datos.write("oopsies")