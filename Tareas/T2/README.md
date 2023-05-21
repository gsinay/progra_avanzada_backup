# Tarea 2: DCCazafantasmas 👻🧱🔥

## Consideraciones generales :octocat:

La tarea, a grande razgos, cumple con lo solicitado. Es decir, se puede acceder al modo constructor o directametne a un mapa, validando el nombre de usuario, donde se representa en una ventana la grilla, la cual se "dibuja" a base de la información alamcenada en el back(lista de lista de listas). Se puede mover a luigi con las teclas, actualizando así la grilla del back, y los fantasmas se mueven aleatoriamente también actualizando el back. Se cuenta con un temporizador y un contador de vidas de luigi a base de los parámetros y el juego recononoce cuando se ha ganado o perdido. 

### Cosas implementadas y no implementadas :white_check_mark: :x:



**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,

#### Ventanas: 27 pts (27%)
 __✅ Ventana de Inicio:__ Lograda correctamente. Se muestra la foto del background, se permite ingresar un nombre y verificar su largo y alfanumericidad. Se puede elegir los mapas cargados en la carpeta mapas y también el modo constructor. Hay un boton de partir que cierra la ventana y abre la ventana de juego o constructor, y un boton salir que cierra la aplicación si es apretado. 
__✅ Ventana de Juego:__ Lograda correctamente. Se muestra una ventana diferente en el caso del modo constructor. Si se elige este, se connectea la información de la ventana de inicio con las instancias de las clases VentanaJuegoConstructor y JuegoConstructor. en la instancia de la ventana, encargada del front, se muestra la grilla con los sprites de murallas, boton de limpiar / jugar (este solo funciona si hay un luigi y estrella en la grilla)  y una capacidad de filtrar los elementos a base de su tipo. Al agregar elementos en la grilla del front, se le pasa a una lista de listas de listas en el back (Logica) mediante una señal de agregar elemento. Una vez se parte el juego (lo cual solo es permitido si se encuentra un luigi y estrella en la grilla) , se cierra esta ventana y se abre una nueva la cual es una instancia de VentanaJuego y se puebla la del grilla, en paralelo a enviar esta informacion a una nueva lista de listas de listas en el back, ahora en la instancia Juego. Esta nueva ventana tiene un temporizador, y se puede pausar y renaudar (por boton y letra p). Se muestran las vidas de luigi y este se puede mover con las teclas asdw. Los fantasmas se mueven correctamente y se gana o pierde dependiendo de las condiciones correctamente. Notar que __NO__ importa si las teclas son mayusculas o minusculas, las condicieones funcionan correctamente (el movimiento de luigi, la pausa, y apretar G para liberar la estrella al agarrarla). En caso que se entre directamente, 
#### Mecánicas de juego: 47 pts (47%)
##### ❌✅🟠 Luigi
##### ❌✅🟠 Fantasmas
##### ❌✅🟠 Modo Constructor
##### ❌✅🟠 Fin de ronda
#### Interacción con el usuario: 14 pts (14%)
##### ❌✅🟠 Clicks
##### ❌✅🟠 Animaciones
#### Funcionalidades con el teclado: 8 pts (8%)
##### ❌✅🟠 Pausa
##### ❌✅🟠 K + I + L
##### ❌✅🟠 I + N + F
#### Archivos: 4 pts (4%)
##### ❌✅🟠 Sprites
##### ❌✅🟠 Parametros.py
#### Bonus: 8 décimas máximo
##### ❌✅🟠 Volver a Jugar
##### ❌✅🟠 Follower Villain
##### ❌✅🟠 Drag and Drop

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
