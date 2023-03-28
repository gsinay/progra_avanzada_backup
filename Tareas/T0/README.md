# Tarea 0: DCCeldas 💣🐢🏰
- Nombre: Gabriel Sinay
- Sección: 2
- Usuario GitHub: @gsinay

## Consideraciones generales :octocat:

La tarea logra todos los objetivos planteados. En funciones.py se completaron las funciones pedidas en el enunciado con la ayuda de otras funciones. El funcionamiento de aquellas esta comentado adentro del codigo. La mas importante a recalcar es la funcion solucionar, que retorna True o False dependiendo de si se puede o no solucionar el tablero, modificandolo al mismo tiempo pues es una función de recursion tipo backtracking que toma como parametro la lista de listas del tablero que es mutable.

Notar que para solucionar el tablero, el metodo recursivo de backtracking es del tipo _fuerza bruta_. Es decir, ve uno por uno las posilibidades del tablero hasta llegar a una que sirva. Notar que por cada dimension del tablero que subimos, hay 2<sup>n<sup>2</sup> - (n-1) <sup>2</sup></sup> mas posibilidades que recorrer que antes. Por ende, si prueban con tableros altos, el codigo va a demorar un rato en correr (procuren tener bateria y el computador en un lugar frio :))

### Cosas implementadas y no implementadas :white_check_mark: :x:


#### Menú de Inicio (5 pts) (7%)
##### ✅ Seleccionar Archivo. Se printea los archivos dentro del directorio T0/Archivos y se debe typear el nombre del archivo a abrir
##### ✅ Validar Archivos: Si el nombre del archivo no existe, se termina el programa.
#### Menú de Acciones (11 pts) (15%) 
##### ✅ Opciones
##### ✅ Mostrar tablero 
##### ✅ Validar bombas y tortugas
##### ✅ Revisar solución
##### ✅ Solucionar tablero. Al solucionar tablero, se guarda la solucion en T0/Archivos y se mantiene el menu de acciones pero con este nuevo tablero solucionado como el elemento en cuestión (es decir, no se puede solucionar nuevamente).
##### ✅ Salir
#### Funciones (34 pts) (45%)
##### ✅ Cargar tablero
##### ✅ Guardar tablero
##### ✅ Valor bombas
##### ✅ Alcance bomba
##### ✅ Verificar tortugas
##### ✅ Solucionar tablero: Llama a una función auxiliar recursiva obtener_solucion que retorna booleanos,y modifica la lista de listas original al ser objetos mutables. 
#### General: (19 pts) (25%)
##### ✅ Manejo de Archivos
##### ✅ Menú
##### ✅ tablero.py. Es llamado correctamente en las opciones 1 y 4 del menu de acciones
##### ✅ Módulos
##### 🟠 PEP-8. Puede ser que se me pasó alguna indentación a espacio y no tab. Algunas lineas de mas de 100 carácteres si se cuenta comentarios informativos.
#### Bonus: 6 décimas
##### 🟠 Funciones atómicas: todas menos 2 (obtener_solucion y verificar_alcance_bombas)
##### ❌ Regla 5
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se deben crear mas archivos. Es mas, si el archivo archivo_sol.txt falta en la carepata Archivos (lo cual sucede cuando se está probando un tablero nuevo, por ejemplo, con un nombre nuevo expecífico) el codigo lo crea. Todos los archivos que se pueden seleccionar son los de la carpeta archivos y se guardan ahi mismo. Por esto mismo, para el correcto uso del código, se deben seguir los siguientes pasos:
1. Clonear el repositorio en el computador local. 
2. Cargar los archivos en formato .txt a la carpeta ```Archivos``` en el formato específicado en el tablero. 
3. Ubicarse dentro de la carpeta T0 ocupando el comando cd del terminal. Esto es crucial. 
4. Correr el ```main.py``` y hacer uso del programa mediante la interfaz del terminal. 
5. Una vez terminado el programa, si se subió un tablero valido y se encontró una solución, esta será guardada en la carpeta Archivos al igual que el tablero original en el formato específico. 


### IMPORTANTE: SE RECALCA LA IMPORTANCIA DE ESTAR EN EL DIRECTORIO .../..../T0 PARA EJECUTAR EL CODIGO. ES CONDICIÓN NECESARIA QUE EL TERMINAL ESTÉ UBICADO ADENTRO DE DICHA CARPETA PUES LOS PATHS SON RELATIVOS DESDE AHÍ

Sobre la ejecución: Para el correcto funcionamiento del programa, se debe verificar que existan los siguientes acrhivos / directorios dentro de T0:
1. ```main.py```
2. ```funcitons.py```
3. ```tablero.py```: EL cual fue ocupado con el parametro utf8 = True
4. ```Archivos```


## Librerías :books:
### Librerías externas utilizadas
1. módulo os

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:
No se crearon modulos nuevos. TODAS las funciones estan en functions.py el cual no exede las 200 lineas. Estas luegos fueron importadas al ```main.py``` ocupando el formato adecuado. 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Al salir del programa en el menú de acciones, no se vuelve al menu principal sino que se termina el codigo y para acceder a este hay que correrlo denuevo.
2. Al ingresar incorrectamente el nombre de un archivo en el menú principal, el programa se cierra y para intentar nuevamente hay que correr el programa denuevo.
3. Si existe una solucion para un acrhivo en la carpeta Archivos y luego se soluciona el mismo tablero con otra solucion, al guardarla, se pierde la solucion anterior (es decir, si existe el archivo _nombre.txt_ y _nombre_sol.txt_ al decedir solucionar _nombre.txt_ nuevamente, el acrhivo _nombre_sol.txt_ es sobreescrito con la nueva solucion si la que se encotrase es diferente a la ya existente)
4. Los archivos que serán cargados serán todos en archivos .txt y subidos a la carpeta Archivos dentro de T0, y son todos en el formato:
   ##### Dimension, n <sub>1</sub>, ... , n<sub>dimension<sup>2<sup></sub>
5. Los tableros cargados no serán de dimension "grandes" i.e. del orden 10, pues la complejidad del problema crece al orden de 2<sup>n<sup>2</sup></sup>. Con un tablero 7x7 de el código demora aprox 7 minutos en solucionar, desconozco en dimensiones mayores.
6. Los archivos a probar serán subidos antes de correr el main al directorio Archivos. El programa solamente muestra los archivos en este directorio y solamente puede leer / solucionar los archivos de este directorio. Si el archivo no se encuentra en la carpeta Archivos, se considerará que exte no existe (ver punto 2.)
7. El codigo se corre en python 3.10, o en su defecto, python 3.x. 

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \https://stackoverflow.com/questions/51657128/how-to-access-the-adjacent-cells-of-each-elements-of-matrix-in-python: esto hace facil saber los indices adyacentes de los elementos del tablero (2 si es equina, 3 si es muralla, 4 si está al medio) y está implementado en el archivo functions.py en las líneas 4-14.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
