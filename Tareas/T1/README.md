# Tarea 1: DCCavaCava 🏖⛏



## Consideraciones generales :octocat:

La tarea hace todo lo logrado. En generar, el funcionamiento es el siguiente: Se creaeron clases abstractar para excavadores y arenas, junto con sus clases hijas dependiendo de los tipos explicitados en el enunciado. Estas clases se encuentras en los archivos ```excavadores.py``` y ```arenas.py```,respectivamente. Luego, se hizo una clase pare el torneo en ```torneo.py``` la cual incluye un atributo de arena y un set de excavadores los cuales se acceden en sus metodos (principalmente simular_dia) con tal de calcular los metros cavados por dia. Los datos se leen en el archivos ```datos.py```, donde algunos objetos se instancian instantaneamente (como los items, mas sobre esto en la seccion de supuestos) mientras que otros, como las arenas y los excavadores, son ordenados en listas pero de forma desintanciada y se van instanciando a medida que sea necesario. Finalmente, el flujo del programa es mediante el archivo ```main.py``` y el archivo ```guardar_cargar.py```se carga de almacenar los datos de las partidas en una base de datos para guardar las partidas y de leer dichos archivos y instanciar el torneo nuevamente al cargar la partida. 


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Programación Orientada a Objetos: 42 pts (35%)
##### ❌✅🟠  Diagrama
__✅ Definición de clases, atributos, métodos y properties__: Se definen las clases en los archivos ya mencionados. Las clases padres son abstractas y las hijas heredan de estas. Algunos métodos son abstractos dependiendo del caso. Las clases tienen properties para los atributos que deben estar dentro de un rango específico como es mencionado en el enunciado.

__✅ Relaciones entre clases:__ Hay herencia (en las clases abstractas como Excavadores con los tipos de excavadores, y lo mismo para Arenas y Items). Torneo compone a arenas y excavadores, y arena agrega a excavadores. Para mas informacion ver diagrama.
#### Preparación programa: 11 pts (9%)
__✅ Creación de partidas__: En el menu inicio se permite crear una nueva partida. Se distingue entre una partida nueva o una cargada mediante el atributo booleano _nuevo_ de la clase torneo, el cual si es true genera la arena y los excavadores iniciales en el init del Torneo.
#### Entidades: 22 pts (18%)
 __✅ Excavador:__ Se encuentra dentro de ```excavadores.py``` Clase abstracta con tres clases hijas: ExcavadorTareo, ExcavadorDocencio y ExcavadorHibrido. Properties para edad, energia, fuerza, suerte y felicidad para mantenerlas siempre sobre 0 y bajo los valores explicitados en el enunciado. Notar que tiene un atributo de "durmiendo" que se activa si el trabajador llega a 0 energia y debe descansar lo estipulado en los parámetros. Notamos que en el metodo encontrar_item, si la arena es mojada luego los excavadores siempre encontraran items, como explicitado en el enunciado.
 
__✅ Arena:__ Se encuentra dentro de ```arenas.py```. Clase abstracta con clases hijas: ArenaNormal, ArenaRocosa, ArenaMojada, ArenaMagnetica. La clase padre define los properties rareza, dureza, humedad y estatica y el metodo dificultad_arena. De los metodos a destacar en las clases hijas, en ArenaNormal y ArenaRocosa se sobreescribe dificultad_arena, y en ArenaMagnetica se define el metodo randomizer que pone la humedad y la dureza en un valor aleatorio. Este último método se llama en la simulacion de dias cuando la arena es magnetica como estipulado en el enunciado. 

__✅ Torneo__: Se encuentra en ```torneo.py```. Instancia las arenas y los excavadores iniciales cuando es un torneo nuevo (no cargado) y define los métodos que serán utilizados en el flujo del programa. De estos, los princiaples son simular_dia, usar_consumible, abrir_tesoro y iniciar_evento (el cual se llama en simular dia si se le "gana" a la probabilidad). 

#### Flujo del programa: 31 pts (26%)
 __✅Menú de Inicio__: Una funcion sin parametros. En ella se llama un input para ver que accion quiere el usuario. Es a prueba de fuego por el while loop y el try,except,raise que hay dentro de ella. Se cumple el bonus y para cargar partida se lleva a un menu separado definido por la funcion menu_cargar.
 
___✅ Menú Principal___: Tiene todas las opciones que se piden, y es robusto por el try,except,raise dentro de el while loop. La función que lo ejecuta es menu_acciones. 

__✅ Simulación día Torneo__: Se llama al método simular_dia de la clase Torneo y se imprime en consola los eventos del día.

__✅ Mostrar estado torneo__: Se llama al método mostrar_estado de la clase Torneo y se imprime en consola el estado del torneo. La tabla funciona de forma bonita si la consola es grande, por lo cual se recomienda expandirla al momento de correr el main. 

__✅ Menú Ítems:__ Se llama el método ver_mochila de Torneo para imprimir en consola los items en la mochila, y se pide imput de usuario para ocupar un item. Al ingresar el numero del item este se consume y es borrado de la mochila. Notar que si se ingresa la tecla "x" se vuelve al menu principal.  

__✅ Guardar partida:__ Se pide un input para el nombre de la partida, la partida es guardada en un archivo .txt dentro del directorio ```partidas```. Estas luegos son leídas por las funciones en ``guardar_cargar.py``` cuando se carga la partida en el menu inicial. 

___✅ Robustez:__ Los inputs toleran cualquier tipo de entrada y solamente ejecutan las acciones cuando la entrada corresponde a una opción valida. Si no, sigue pidiendo. Notar que __SI__ son case-sensitive. 
#### Manejo de archivos: 14 pts (12%)
__✅ Archivos CSV:__ Son leidos y procesados en el archivo ```datos.py```, en los comentarios de dicho archivo se encuentra mas info de como se procesan los datos. 

__✅ Archivos TXT:__ Son escritos con nombres personalizados dentro del directorio Parametros. Cada linea corresponde a uno de los atributos del Torneo o un elemento de los conjuntos/listas de dichos atributos. La primera palabra de cada linea explicita el tipo de elemento que se está leyendo (por eso en la funcion cargar_torneo se encuentra repetidamente indices como [1:]. 

__✅ parametros.py:__ Todos los parametros estan ahi para evitar Hard-Codeo. 
#### Bonus: 3 décimas máximo

__✅ Guardar Partida:__ Implementado correctamente

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```arenas.csv``` en ```T1```
2. ```consumibles.csv``` en ```T1```
3. ```ecavadores.csv```en ```T1```
4. ```tesoros.csv``` en ```T1```

__TODOS__ estos archivos deben estar en el mismo formato que el  "practica" correspondiente que fueron subidos o el programa no correrá. 

__IMPORTANTE__: Para correr el programa, es necesario que el terminal se ubique en la carpeta T1 (el mismo directorio del ```main.py```), o saltará un error. Correr el programa con python3 ya que en algunos sistemas, como mac, python lo correrá con python 2.7 arrojando errores. 


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path```
2. 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```excavadores```: Contiene a ```Escavador(ABC)``` y sus clases hijas
2. ```arenas```: Contiene a ```Arena(ABC)``` y sus clases hijas
3. ```items```: Contiene a ````Items(ABC)``` y sus clases hijas
4. ```torneo```: Contiene a ```Torneo```. 
5. ```funciones_auxiliares```: Contiene funciones para modularizar y ser mas breve en el codigo. Principalmente, para filtrar la base de datos de arenas y excavadores por tipo, para instanciar dichos objetos y tambien para obtener los excavadores que no han sido utilizados todavía.
6. ```guardar_cargar```: Modulo con funciones que se encargan de escribir los archivos al guardar partias y de leerlos y instanciar torneos al momento de cararlas. 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los items pueden ser repetidos, es decir, que al encontrar uno este puede volver a aparecer.
2. Los trabajadores trabajan mientras tengan energía. Es decir, si excavar restra n energía y en un día hay m<n unidades de energía, se excavará igual dejando la energía en 0 y de ahí partir descansando. 
3. No se pueden repetir excavadores. Es decir, no hay clones :)
4. Se parte en el día 0. 
5. Se excava mientras hayan días. Es decir, el juegot termina al llegar a dias_totales, y solamente ahí revisa si se ha excavado los metros_meta necesarios. 


PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
