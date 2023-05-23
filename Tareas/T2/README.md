# Tarea 2: DCCazafantasmas 👻🧱🔥

## Consideraciones generales :octocat:

La tarea, a grande razgos, cumple con lo solicitado. Es decir, se puede acceder al modo constructor o directamente a un mapa, validando el nombre de usuario, donde se representa en una ventana la grilla, la cual se "dibuja" a base de la información almacenada en el back(lista de lista de listas). Se puede mover a luigi con las teclas, actualizando así la grilla del back, y los fantasmas se mueven aleatoriamente también actualizando el back. Se cuenta con un temporizador y un contador de vidas de luigi a base de los parámetros y el juego recononoce cuando se ha ganado o perdido. Lo único no logrado fueron las siguientes dos cosas: las animaciones de los elementos en la grilla al moverse, los cuales se moderalon con movimiento discreto de una casilla a la otra, y el cheatcode KIL.

### Cosas implementadas y no implementadas :white_check_mark: :x:

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,

#### Ventanas: 27 pts (27%)
 __✅ Ventana de Inicio:__ Lograda correctamente. Se muestra la foto del background, se permite ingresar un nombre y verificar su largo y alfanumericidad. Se puede elegir los mapas cargados en la carpeta mapas y también el modo constructor. Hay un boton de partir que cierra la ventana y abre la ventana de juego o constructor, y un boton salir que cierra la aplicación si es apretado. 
__✅ Ventana de Juego:__ Lograda correctamente. Se muestra una ventana diferente en el caso del modo constructor. Si se elige este, se connectea la información de la ventana de inicio con las instancias de las clases VentanaJuegoConstructor y JuegoConstructor. en la instancia de la ventana, encargada del front, se muestra la grilla con los sprites de murallas, boton de limpiar / jugar (este solo funciona si hay un luigi y estrella en la grilla)  y una capacidad de filtrar los elementos a base de su tipo. Al agregar elementos en la grilla del front, se le pasa a una lista de listas de listas en el back (Logica) mediante una señal de agregar elemento. Una vez se parte el juego (lo cual solo es permitido si se encuentra un luigi y estrella en la grilla del back) , se cierra esta ventana y se abre una nueva la cual es una instancia de VentanaJuego y se puebla su grilla, en paralelo a enviar esta informacion a una nueva lista de listas de listas en el back, ahora en la instancia Juego. Esta nueva ventana tiene un temporizador, y se puede pausar y renaudar (por boton y letra p). Se muestran las vidas de luigi y este se puede mover con las teclas asdw. Los fantasmas se mueven correctamente y se gana o pierde dependiendo de las condiciones correctamente. Notar que __NO__ importa si las teclas son mayusculas o minusculas, las condiciones funcionan correctamente (el movimiento de luigi, la pausa, y apretar G para liberar la estrella al agarrarla). Notar que cada vez que hay un cambio en la grilla del back, se le manda TODA la informacion de la grilla actualizada al front mediante la señal "senal_armar_front_inicial" de tal manera que se actualize la grilla visual de la ventana. En caso que se entre directamente (sin pasar por el modo constructor), se utiliza solamente Juego y VentanaJuego, donde al back se le da la inforamción para poblar la lista de lista de listas dependiendo de la información en el archivo de texto del mapa. 

Las clases para la lógica se encuentran en el archivo ```models_juegos.py```y las del front en los archivos de tipo ```frontend.....py``` dependiendo de la ventana que se este utilizando. 

#### Mecánicas de juego: 47 pts (47%):
__✅ Luigi:__ Se intancia un luigi al partir el juego, el cual tiene una cantidad de vidas dependiendo de los parametros y tambien un atributo de posición para mantener memoria de donde se encuentra en la grilla. El método KeyPressEvent está conectado con el slot tecla_presionada del back Juego, el cual checkea si la tecla es awsd. Si es una de esas, intentará mover el luigi. Intentará pues también checkea para cada dirección si hay una muralla o un fuego/fantasma (en tal caso pierde una vida y vuelve al inicio). Luigi puede mover las rocas, siempre mientras estas no estén frente a una muralla o o limite de grilla en la dirección de movimiento. 
__✅Fantasmas__: Son Qthreads que tienen un temporizador aleatorio dado por los parametros y un atributo que establece su dirección de movimiento. El temporizador llama a un método de tal manera que en ese intervalo de tiempo se actualize la grilla del back Juego dependiendo de quien llama al método y su dirección. Esto se hace a través de la senal_movimiento, la cual se conecta al slot mover_fantasma del back y envía la dirección del fantasma que se esta moviendo, la posición del fantasma, y el fantasma mismo. Si el fantasma no puede moverse en la dirección establecida por muralla o roca, se cambia su direccion de movimiento. Si choca con un fuego, el fantasma se saca de la grilla y se para el thread. 
__✅ Modo Constructor:__ Funciona correctamente. Se puede poner una cierta cantidad de elementos en la grilla dependiendo de los parámetros, y se pueden filtrar por tipo. Esto se logra seteandole un atributo tipo a cada boton. El boton para jugar solo funciona si se cumple que hay un luigi y una estrella en la grilla, sino se da un popup de alerta de tipo ```QMessageBox```. Tuve que definir un tamaño para la ventana pues por alguna razón, al ocupar .scaled() para los sprites, no se permitía mantener la naturaleza rectangular de la grilla al extender la pagina. 
__✅ Fin de ronda__: Dependiendo de si se gana o se pierde, suenan los sonidos de la carpeta sounds. Se muestra el puntaje y el usuario a través de una QMessageBox. Nuevamente esta informacion es pasada del back al front mediante una señal. 
#### Interacción con el usuario: 14 pts (14%)
__✅Clicks__: Los clicks de los botones son mediante click izquierdo. En el caso de los botones, se conectan con sus slots respectivos mediante .clicked.connect(), donde de ahí en adelante se emitea una señal si es necesario. En el caso del juego constructor, al clickear en un boton de sprite, este queda seleccionado hasta que se aprete otro botón. Por ejemplo, si clickeo en la muralla, luego puedo clickear en una posicion en la grilla para settear esa muralla. Luego puedo clickear nuevamente en la grilla en otra posicion (siempre mientras queden murallas y la nueva posicion esté vacía) para poner una nueva muralla sin tener que haber apretado el boton de muralla nuevamente(Es decir, los botones tienen memoria). En un inicio, cuando no se ha apretado ningun botón, se asume que el boton clickeado es luigi. 
__❌Animaciones__:   No implementado, los sprites se mueven discretamente en la grilla del front. Se eligió un único archivo para cada elemento del juego png de la carpeta sprites para representarlo en el front. 
#### Funcionalidades con el teclado: 8 pts (8%)
__✅ Pausa__: Se puede pausar/renaudar el juego con el botón p del teclado y con el boton pausar/renaudar de la ventana. Esto pausa y renauda el timer de acorde. Se bloquean tambien los movimientos de los threads y de luigi con sus teclas correspondientes.
__❌ K + I + L:__ No implementado.
__✅ I + N + F__: Se pausa el timer infinitamente y se le entregan virtualmente infinitas vidas a luigi (mediante math.inf). Notar que este cambio de vidas en la ventana solamente se muestra en el front una vez que luigi choque con un fuego o fantasma, aunque en el back se tenga memoria de esto. Una vez terminado el juego, se calcula el puntaje como si fuera el máximo. Notar que para hacer uso del cheatcode se debe apretar la tecla I, luego la N y después la F, sin apretar ninguna tecla entremedio, si no se vuelve al inicio de la sequencia (tipo Gta jaja)
#### Archivos: 4 pts (4%)
__✅ Sprites__: Los archivos utilizados son importados correctamente (de forma relativa) desde la carpeta sprites. Son implementados en los Qlabels o QPushButtons con setIcon() o setPixmap().
__✅ Parametros.py:__ Correctamente definidos en ```parametros.py``` y importados a los otros archivos .py  segun sea necesario. 
#### Bonus: 8 décimas máximo
__❌ Volver a Jugar:__
__❌ Follower Villain:__
__❌ Drag and Drop:__

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` ubicado en T2. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```mapas``` en ```T2``` el cual contiene la información de los mapas predefinidos en el mismo formato del enunciado
2. ```sounds``` en ```T2``` el cual debe tener dos archivos .wav: ```gameOver.wav```y ```stageClear.wav```
3. ```sprites```en ```T2```el cual debe tener tres sub directorios: ```Elementos```, ```Fondos``` y ```Personajes```, cada uno con los arhcivos entregados en el enunciado. Notar que los archivos "right" estaban mal escritos con rigth. Por ejemplo, ```luigi_rigth_1.py``` en vez de  ```luigi_right_1.py```. Ocupar la forma mal escrita o habrán errores. 

Es sumamente importante asegurarse que los archivos ```frontend_inicio.py```, ```frontend_juego.py```, ```frontend_juego_constructor.py```,  ```models_elementos.py```,  ```models.juegos``` y  ```main.py``` se encuentren en el mismo directorio que  ```mapas```,  ```sounds``` y  ```sprites```. Por default, este es T2 (por lo cual es importante ubicarse ahí). Pero, si llegasen a cambiar algo para la recorreción, favor mantener esto en mente. 


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path```
2. ```math```: ```inf()``` (A mi conocimiento, no debe instalarse). La ocupé en ```models_juegos.py```en la línea 272, para setear las vidas de luigi a un numero muuuuy alto (virtualmente infinito) al hacer uso del cheatcode IND

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```models_elementos```: Contiene a ```Luigi```, un Qwidget, y a ```Fantasma```  un Qthread con sus clases hijas ```FantasmaHorizontal```y ```FantasmaVertical```
2. ```models_juegos```: Contiene a ```JuegoConstructor```y ```Juego```, los modelos del back para el juego constructor y el juego como tal. 
3. ```frontend_inicio.py```: Contiene a ```VentanaInicio```, la cual se preocupa del frontend del menú de inicio
4. ```backend_inicio.py```: Contiene a ```Procesador```, el cual se encarga principalmente a verificar que el nombre de usuario ingresado en el inicio sea valido
5. ```frontend_juego_constructor.py```: Contiene a ```VentanaJuegoConstructor```, clase que se encarga del front en el constructor.
6. ```frontend_juego.py```: Contiene a ```VentanaJuego```, clase que se encarga del front una vez que se habilitan las mecánicas del juego.  

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:
 - Al finalizar el juego, se muestra el popup, y al cerrar el popup, se cierra la aplicación, pues al no implementar la opción jugar de nuevo no hace sentido mantener la aplicación abierta. 
 - El cheatcode INF funciona solamente si INF se apretan de forma directa una despues de la otra. Si se apreta una tecla entre medio, se reinicia la secuencia. 
 


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://doc.qt.io/qtforpython-5/PySide2/QtCore/QMutex.html>: Esto es un lock dentro del mundo de PyQT5 para que los threads fantasmas no tengan problema de sincronización al moverse en la grilla. Esta implementado en ```models_elementos.py``` en la linea 11, y se accede al lock en los metodos run de cada thread. 

En general, ocupé muuuchos métodos, atributos, clases, etc. de PyQt5 que no vimos directamente en clases. Por ejemplo: el método set_params, las clase QComboBox, QmessageBox y Qsound, etc. En general, toda la información de estas clases y como ocuparlas las encontré en la documentación oficial de PyQt5 que se encuenra en <https://doc.qt.io/qt.html#qtforpython>.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
