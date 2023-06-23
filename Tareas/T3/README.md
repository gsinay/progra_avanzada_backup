# Tarea 3: DCCachos :school_satchel:

HOLA AYUDANTE :). Voy a entregar la tarea con cupones probablemente el viernes, por si alguna razon abren este directorio antes de eso y se encuentran con el read me hasta la mitad es por eso. g


## Consideraciones generales :octocat:
Hasta el momento, la tarea es ejecutable pero con algunas consideraciones. En general, la sala de espera funciona como esperado: Se permite el ingreso de jugadores donde los primeros 4 tienen la capacidad de partir el juego. Luego, si alguno de ellos se desconecta y hay algún otro cliente conectado (es decir, un 5to cliente), a este se le permite entrar a la sala de espera y poder partir la partida. Notamos que __NO__ implementé bots. Luego, solo se puede partir la partida si hay 4 clientes conectados como minimo, sino salta una advertencia.

En cuanto a la partida, mientras hayan cuatro jugadores en la sala funciona como esperado en un juego de cachos basico: Hay turnos, se puede dudar y subir la apuesta. Si la acción es "ilegal" (subir la apuesta a un numero menor del ya anunciado o dudar el primer turno), salta una advertencia. Por ahora, no he implementado cambiar dados y usar poder. Cuando queda solamente una persona viva, se anuncia el ganador y se cierra el programa. 


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 18 pts (16%)
__✅ Protocolo__: Se instancian los sockets con AF_INET y SOCK.STREAM tanto en el client-side como el server-side. 

__✅ Correcto uso de sockets:__ El servidor y cada cliente tienen un parametro que es self.socket, el cual se rellena con la informacion del localhost y puerto ingresado al ejecutar los archivos main tanto del client-side como el server-side. 

__✅Conexión:__ Los sockets del servidor y cliente se connectan mediante connect y bind. A medida que se suman conecciones al servidor, se ejecutan threads que manejan a cada cliente en pos de que puedan funcionar cada uno de forma simultanea. 

__✅Manejo de Clientes:__ Se pueden sumar cuantos clientes permita python y la maquina al servidor, pero no todos son sumados al parametro del servidor self.jugadores (algunos se suman a self.jugadores_standby), especificamente cuando las conecciones sobrepasan NUMERO_JUGADORES cantidad de conecciones. 

__✅ Desconexión Repentina:__ Los jugadores pueden desconectarse sin causar que el servidor se caiga, esto se logra mediante los extensos try and except blocks de tanto los archivos ```server.py``` en la carpeta ```servidor``` y ```back_cliente.py```en la carpeta ```cliente```.

#### Arquitectura Cliente - Servidor: 18 pts (16%)

__✅ Roles:__ Hay una clara separación de roles. En el lado del cliente, dentro de la carpeta ```cliente``` se encuentra el archivo ```back_cliente.py```, el cual define la clase ```LogicaCliente```, la cual hereda de QObject y instancia un atributo que es self.socket_cliente, el cual intenta conectarse al servidor. En esta clase de cliente, se reciben mensajes del servidor y se envían a las ventanas de juego y espera, y vicecersa. __NO__ se tratan los datos de los clientes (digase: checkear condiciones, actualizar juego, etc.) Pues todo esto sucede en la clase ```Servidor``` dentro de ```Server.py``` en el directorio ```servidor```

__🟠 Consistencia:__ Al haber un cambio en el juego o vetnana de un jugador, este se refleja en el de los otros jugadores (pues todos los cambios pasan por la clase Servidor). No obstante, __NO__ se utilizaron Locks, por lo cual se debe procurar de hacer una accion a la vez (Instanciar cada cliente uno a la vez, no apretar botones al mismo tiempo, etc.) 

__✅ Logs:__ La consola del servidor imprime Logs cada vez que le llega informacion necesaria llamando a su metodo log. E

#### Manejo de Bytes: 26 pts (22%)
__✅ Codificación:__ Se encuentra la función codificar en ambos archivos ```cripto.py```. Esta funciona calculando la cantidad de chunks que será necesario, luego iterando sobre un for loop en dicha cantidad donde se rellena la cola del mensaje con 0's ocupando la funcion built-in ljust si es necesario. Se ocupan los formatos endians mediante la funcion to_bytes o from_bytes a medida que sea necesario. 

__✅Decodificación:__ Funciona a la inversa de Codifiación. Se encuentra la funcion decodificar en ambos archivos ```cripto.py```. Notar que se hace uso de la funcion built-in rstrip(b'\x00') con finalidad de sacar los place-holders de al final. Se ocupan los formatos endians mediante la funcion to_bytes o from_bytes a medida que sea necesario. 

__✅Encriptación:__ Se encuentra la función encriptar en ambos archivos ```cripto.py```, la cual toma como parametro el bytearrar a encriptar y el numero a mover. Hacemos uso del operador mod % para lograr lo pedido. 

__✅ Desencriptación:__ Lo mismo a lo anterior pero al reverso. 

__✅ Integración:__ Se combinan los elementos codificacion-encriptacion y decodificacion-desencriptacion en las funciones ```encriptar_y_codificar```y ```desencriptar_y_decodificar```las cuales se usan tanto en ```back_cliente.py```y ```server.py```cada vez que se envia un mensaje (via los metodos broadcast_mensaje_especifico, broadcast_mensaje_general y enviar_mensaje)
#### Interfaz Gráfica: 22 pts (19%)
__✅Ventana de Inicio:__ Se define dentro del archivo ```front_inicio.py``` dentro de la carpeta ```frontend```del cliente. Cada vez que se conecta un cliente, se llama a la funcion ```actualizar_waiting_room```, suponiendo que el cliente no está en standby. En caso que si(es decir, es el >4 cliente conectado), se llama la funcion server_lleno de tal modo de inhabilitarle el boton de partir el juego y además se le pone un label avisandole de tal. Cuando se desconecta un cliente, se llama a la funcion jugador_desconectado y repaint para actualizar los íconos de los jugadores en la sala de espera (y al siguiente cliente en standby se la habilitan las funciones para partir juego ya que ahora hay un espacio para el)

__🟠 Ventana de juego:__ Funciona casi a la completitud, excepto por el hecho que el boton usar_poder existe pero solamente de forma visual (no se implementó esto es el juego). La clase de la ventana se encuentra dentro del archivo ```front_juego.py``` dentro de la carpeta ```frontend```del cliente. En esta, se define la informacion  de ronda como atributos de instancia, junto con los labels de la vida de cada jugador (esto mediante la funcion set_attr de tal manera de poder hacerlo dentro de un forloop de los nombres de los jugadores que se llama al instanciar la ventana). Notamos que los jugadores estan en circulo donde cada jugador se visualiza a el mismo arriba de la ventana, y se respeta el orden del circulo para cada jugador. Al recibir la informacion que un jugador se desconectó del server, se llama al atributo self.vidas_nombrejugador de tal manera de displayear 0 vidas constantemente. Los labels de informacion se actualizan despues de cada turno, y los turnos en cada ventana siguen el orden logico de los "puestos" de los jugadores. El jugador solamente puede visualizar sus dados y cambiarlos una vez, sino se gatilla la funcion ```error_cambiar_dados```la cual levanta un  Qmessagebox indicando que no se puede hacer dicha accion. Cuando un jugador quiere dudar siendo que este partio la partida o cuando quiere ingresar un valor invalido tambien se gatilla un Qmessagebox mediante el metodo ```error_turno```.  


#### Reglas de DCCachos: 22 pts (19%)
__✅ Inicio del juego:__ Implementado correctanente. El jugador del turno 0 se elige aleatoriamente (esto eligiendo un numero random edl largo de lista de jugadores en el cual "sliciear" dicha lista en 2), cada jugador es asignado dados aleatorios (mediante el metodo ``` shuffle_dados_general``` de la clase Juego en el archivo ```logica_juego.py```, la cual se instancia en ```server.py```al partir el juego). Los turno siguen el orden de la lista self.jugadores de la clase Juego que se instanció. (Ej: lista_jugadores = [1,2,3,4]. Luego sliceamos con un indice random, digamos el 2 de tal manera que quede lista_jugadores = [3,4,1,2], luego parte el juego el jugdaor 4 y se juega circularmente siguiendo el orden de la lista). El jugador en turno y del turno anterior puede ser detectado ocupando las properties definidas para la clase, la cual hace uso del modulo (%) y el atributo de instancia turno para saber a que indice de la lista de jugadores le toca jugar.

__❌ Bots:__ No implementado. Para partir la partida se necesita que hayan 4 jugadores conectados. 

__🟠 Ronda:__ Casi imlementado en su totalida, excepto por la parte de los poderes. Al momento de pasar o subir una apuesta, el metodo ```jugar_turno```de la clase Juego verifica si el jugador mintió o no. Si mintió, establece que jugador.mintiendo = True, y False e.o.c. Luego, al dudar, se checkea si el jugador anterior estaba mintiendo o no. Si estaba mintiendo, el pierde una vida y se refleja tanto en su atributo de vidas como en su label correspondiente en el front. Si no minitó, luego el jugador que dudó sufre estos efectos. De ahí, la instancia de Juego llama a ```nueva_ronda``` donde se vuelve a remixiar la lista de jugaddores para definir una nueva persona que parta el turno. 

__✅ Termino del juego:__ Después de cada turno, se llama a ```checkear_ganador``` de la clase Juego. En ella, se ve si los jugadores totales - jugadores muertos = 1. En tal caso, hay un ganador que es la unica persona quien queda en Juego.jugadores. Se envía una señal a todos los jugadores en la ventana de juego que tal persona es la ganadora.  
#### Archivos: 10 pts (9%)
__✅Parámetros (JSON):__ Se importan correctamente tanto en el servidor como el cliente donde cada Json tiene los parametros importantes para su rol. 

__✅main.py:__ Se encuentran estos archivos dentro de los directorios base de cliente y servidor. Se puede pasar el puerto mediante consola al hacer uso de sys.argv

__✅ Cripto.py:__ Los archivos crpito.py tanto del cliente y servidor son identicos y se encuentran dentro de las carpetas scrpits de cada rol. En estos, se encuentran las funciones encriptar, codificar, desencriptar, decodificar, y encriptar_y_codificiar y decodificar_y_desencriptar que une ambos procesos. Estas ultimas dos funciones son ocupadas tanto en server.py del servidor y back_cliente.py del cliente para enviar y recibir mensajes.
#### Bonus: 4 décimas máximo
__❌Cheatcodes:__

__❌Turno con tiempo:__

## Ejecución :computer:
Los módulos principal de la tarea a ejecutar son  ```main.py``` tanto del servidor como del cliente. Es __SUMAMENTE IMPORTANTE__ Ejectutar primero el archivo main.py del servidor una unica vez para levantar el servidor y despues el main del clietne cuantas veces sea necesario. Además se debe crear los siguientes archivos y directorios adicionales:
1. todos los directorios estaticos(background, dices, extra) con sus respectivos arhivos (background_inicio.png, dice_1.png etc. et.c) dentro del directorio basico edl cliente, es decir, en ```cliente``` a la misma artura de ```main.py```, ```parametros.json```, ```Scripts```, ```frontend```y ```backend```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```
2. ```random```
3. ```sys```
4. ```json```
5. ```socket```
6. ```threading```
7. ```time```
8. ```PyQt5```: una variedad de metodos de QtCore, QtWidgets y QtGui



### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cripto.py```: contiene ```encriptar_y_codificiar´´´, ´´´decodificar_y_desencriptar```las cuales se usa al enviar mensajes
2. ```logica_juego.py```: contiene las clases ```Juagdor``` y ```Juego```, ambas clases representan la logica de las partidas (debe instalarse). Los jugadores se instancian dentro de la clase Juego y la clase Juego se instancia en server.py al partir el juego.
3. ```server.py``` dentro de ```servidor``` contiene a la clase Servidor que se instancia en el main del servidor. Este se encarga de todo lo relacionado a la comunicacion con clientes y manejo de datos. 
```back_cliente.py```dentro de la carpeta ```backend``` de ```cliente``` contiene a la clase LogicaCliente la cual se instancia en el main del cliente y se encarga de comunicarse con el servidor mediante sockets para recibir datos de la partida
```front_inicio.py``` y ```front_juego.py```, las cuales se encargan de las ventanas PyQt5 del cliente. Estas se instancian en el main y se muestran/hidean dependiendo de la informacion que va recibiendo el jugador del server del estadod el juego. Se comunican con __VARIAS__ señales a la logica del juego para habilitar botones, mandar y recibir informacion, mostrar popups, etc.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los jugadores juegan turnos de manera circular, como si estuvieran en una mesa de poker
2. Los jugadores unicamente pueden salir del juego a decision propia (i.e. el boton salir) cuando se termina la partida (para que no hayan jugadores que "chackreen" el juego). Si salen mediante quit del terminal el servidor lo atrapa como un error.
3. Los jugadores en sale de espera "standby" entran a la sala de espera "habilitada" en el orden que van lelgando (i.e. si hay dos jugadores en sala de espera antes de la partida del juego, si se desconecta uno de los jugadores que esta por jugar, el primer jugadaor en standby en haber llegdo será el que toma su puesto)
4. Una vez partido el juego los jugadores en standby no pueden ingresar a el, aunque haya una desconección 
5. Se necesitan 4 jugadores para partir el juego (pues no implementé bots)



-------



## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. En general, ocupé muuuchos métodos, atributos, clases, etc. de PyQt5. Por ejemplo: QmessageBox.  En general, toda la información de estas clases y como ocuparlas las encontré en la documentación oficial de PyQt5 que se encuenra en <https://doc.qt.io/qt.html#qtforpython>.
2. Uso de Rstrip para eliminar los trailing zeros de los bytearrays: <https://www.w3schools.com/python/ref_string_rstrip.asp>




## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
