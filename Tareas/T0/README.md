# Tarea 0: DCCeldas 💣🐢🏰


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

La tarea logra todos los objetivos planteados. En funciones.py se completaron las funciones pedidas en el enunciado con la ayuda de otras funciones. El funcionamiento de aquellas esta comentado adentro del codigo. La mas importante a recalcar es la funcion solucionar, que retorna True o False dependiendo de si se puede o no solucionar el tablero, modificandolo al mismo tiempo pues es una función de recursion tipo backtracking.

Notar que para solucionar el tablero, el metodo recursivo de backtracking es del tipo _fuerza bruta_. Es decir, ve uno por uno las posilibidades del tablero hasta llegar a una que sirva. Notar que por cada dimension del tablero que subimos, hay 2^(dimiension-dimension_anterior) mas posibilidades que recorrer que antes. Por ende, si prueban con tableros altos, el codigo va a demorar un rato en correr (procuren tener bateria y el computador en un lugar frio :))

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:

#### Menú de Inicio (5 pts) (7%)
##### ✅ Seleccionar Archivo
##### ✅ Validar Archivos
#### Menú de Acciones (11 pts) (15%) 
##### ✅ Opciones
##### ✅ Mostrar tablero 
##### ✅ Validar bombas y tortugas
##### ✅ Revisar solución
##### ✅ Solucionar tablero
##### ✅ Salir
#### Funciones (34 pts) (45%)
##### ✅ Cargar tablero
##### ✅ Guardar tablero
##### ✅ Valor bombas
##### ✅ Alcance bomba
##### ✅ Verificar tortugas
##### ✅ Solucionar tablero
#### General: (19 pts) (25%)
##### ✅ Manejo de Archivos
##### ✅ Menús
##### ✅ tablero.py
##### ✅ Módulos
##### 🟠 PEP-8
#### Bonus: 6 décimas
##### 🟠 Funciones atómicas (todas menos 2)
##### ❌ Regla 5
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se deben crear mas archivos. Es mas, si el archivo archivo_sol.txt falta, el codigo lo crea. Todos los archivos que se pueden seleccionar son los de la carpeta archivos y se guardan ahi mismo

### IMPORTANTE: PARA EJECUTAR EL CODIGO ES CONDICIÓN NECESARIA QUE EL TERMINAL ESTÉ UBICADO ADENTRO DE LA CARPETA T0 PUES LOS PATHS SON RELATIVOS DESDE AHÍ



## Librerías :books:
### Librerías externas utilizadas
No se ocuparon librerias externas, solamente el modulo os.

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:
No se crearon modulos nuevos. TODAS las funciones estan en functions.py el cual no exede las 200 lineas.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Al salir del programa en el menú de acciones, no se vuelve al menu principal sino que se termina el codigo y para acceder a este hay que correrlo denuevo.
2. Al ingresar incorrectamente el nombre de un archivo en el menú principal, el programa se cierra y para intentar nuevamente hay que correr el programa denuevo.
3. Si existe una solucion para un acrhivo en la carpeta Archivos y luego se soluciona el mismo tablero con otra solucion, al guardarla, se pierde la solucion anterior (es decir, si existe el archivo _nombre.txt_ y _nombre_sol.txt_ al decedir solucionar _nombre.txt_ nuevamente, el acrhivo _nombre_sol.txt_ es sobreescrito con la nueva solucion)

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
1. \https://stackoverflow.com/questions/51657128/how-to-access-the-adjacent-cells-of-each-elements-of-matrix-in-python: esto hace facil saber los indices adyacentes de los elementos del tablero (2 si es equina, 3 si es muralla, 4 si está al medio) y está implementado en el archivo functions.py en las líneas 4-14.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
