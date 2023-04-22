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
##### ❌✅🟠 Excavador
##### ❌✅🟠 Arena
##### ❌✅🟠 Torneo
#### Flujo del programa: 31 pts (26%)
##### ❌✅🟠 Menú de Inicio
##### ❌✅🟠 Menú Principal
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
