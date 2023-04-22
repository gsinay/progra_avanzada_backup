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
##### ❌✅🟠 Simulación día Torneo
##### ❌✅🟠 Mostrar estado torneo
##### ❌✅🟠 Menú Ítems
##### ❌✅🟠 Guardar partida
##### ❌✅🟠 Robustez
#### Manejo de archivos: 14 pts (12%)
##### ❌✅🟠 Archivos CSV 
##### ❌✅🟠 Archivos TXT
##### ❌✅🟠 parametros.py
#### Bonus: 3 décimas máximo
##### ❌✅🟠 Guardar Partida

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```función() / módulo```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

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
