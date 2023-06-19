# Tarea 3: DCCachos :school_satchel:




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
__✅ Desconexión Repentina:__ Los jugadores pueden desconectarse sin causar que el servidor se caiga, esto se logra mediante los extensos try and except blocks de tanto los archivos ```server.py``` en la carpeta ```servidor``` y ```back_cliente.py```en la carpeta ```cliente```
#### Arquitectura Cliente - Servidor: 18 pts (16%)
##### ❌✅🟠 Roles
##### ❌✅🟠 Consistencia
##### ❌✅🟠 Logs
#### Manejo de Bytes: 26 pts (22%)
##### ❌✅🟠 Codificación
##### ❌✅🟠 Decodificación
##### ❌✅🟠 Encriptación
##### ❌✅🟠 Desencriptación
##### ❌✅🟠 Integración
#### Interfaz Gráfica: 22 pts (19%)
##### ❌✅🟠 Ventana de Inicio
##### ❌✅🟠 Ventana de juego
#### Reglas de DCCachos: 22 pts (19%)
##### ❌✅🟠 Inicio del juego
##### ❌✅🟠 Bots
##### ❌✅🟠 Ronda
##### ❌✅🟠 Termino del juego
#### Archivos: 10 pts (9%)
##### ❌✅🟠 Parámetros (JSON)
##### ❌✅🟠 main.py
##### ❌✅🟠 Cripto.py
#### Bonus: 4 décimas máximo
##### ❌✅🟠 Cheatcodes
##### ❌✅🟠 Turno con tiempo

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
