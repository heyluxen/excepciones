# Ejemplo 1 - Try-Except básico con división entre cero

```python
try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(f"El resultado es:{resultado}")
except:
    print("¡Ups! No se puede dividir entre cero.")

```
## Explicación
En este código, la división numero1 / numero2 intenta dividir 10 entre 0. En matemáticas y en programación, dividir cualquier número entre cero no está permitido. Python detecta este error y genera automáticamente una excepción llamada ZeroDivisionError.

El bloque try envuelve el código que podría fallar. Cuando ocurre el ZeroDivisionError, Python inmediatamente deja de ejecutar el resto del código dentro del try (nunca llega a ejecutar el print del resultado) y salta al bloque except. Como no especificamos ningún tipo de excepción en el except, este captura CUALQUIER error que ocurra.

## Salida
![Salida ejemplo 1](images/captura1.png)

## ¿Por qué da esa salida?
- El programa muestra "¡Ups! No se puede dividir entre cero." porque:

- La línea resultado = 10 / 0 genera un error

- El programa salta al bloque except

- Se ejecuta el print dentro del except

- El programa termina sin mostrar ningún resultado de división

# Ejemplo 2 - Excepciones especificas

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"100 dividido por {numero} es {resultado}")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes introducir un número válido.")
```


## Explicación
En este código hay dos posibles excepciones que pueden ocurrir.

Primera excepción posible: ValueError. Ocurre en la línea numero = int(input("Introduce un número: ")) cuando el usuario escribe algo que no es un número. Por ejemplo, si escribe "hola" o "tres", la función int() no puede convertir ese texto a número entero y lanza un ValueError.

Segunda excepción posible: ZeroDivisionError. Ocurre en la línea resultado = 100 / numero cuando el usuario introduce el número 0. Dividir 100 entre 0 no está permitido en matemáticas, por lo que Python lanza un ZeroDivisionError.

Lo importante de este ejemplo es que cada tipo de error tiene su propio bloque except. Si ocurre un ValueError, se ejecuta el primer except y muestra un mensaje sobre entrada inválida. Si ocurre un ZeroDivisionError, se ejecuta el segundo except y muestra un mensaje sobre división entre cero. Si no ocurre ninguna excepción, se ejecuta el print del resultado.

## Salida
![Salida 2](images/captura2.png)

# Ejemplo 3 - Accediendo a la información de la excepción

```python
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as error:
    print(f"Error:{error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")
```

## Explicación
En este código se trabaja con archivos, una operación que comúnmente genera excepciones.

El bloque try intenta abrir un archivo llamado "archivo_inexistente.txt" en modo lectura ("r"). Si el archivo no existe en la carpeta del programa, Python no puede abrirlo y genera una excepción de tipo FileNotFoundError.

La novedad de este ejemplo es el uso de "as error" después del tipo de excepción. Esto captura el objeto de la excepción y lo guarda en una variable llamada error. Dentro del bloque except podemos acceder a ese objeto para ver información detallada del error, como el mensaje original que Python habría mostrado.

Cuando se captura el error, el programa no solo muestra el mensaje de error, sino que también crea el archivo que faltaba en modo escritura ("w") y escribe contenido dentro de él. Así, la próxima vez que se ejecute el programa, el archivo ya existirá.

## Salida
![Salida ejemplo 3](images/captura3.png)

## ¿Por qué da esa salida?
Cuando se ejecuta este programa por primera vez en una carpeta donde no existe el archivo "archivo_inexistente.txt", ocurre lo siguiente:

- Paso 1: El bloque try intenta abrir el archivo en modo lectura.
- Paso 2: Python busca el archivo y no lo encuentra.
- Paso 3: Python genera una excepción FileNotFoundError con un mensaje que dice algo como "[Errno 2] No such file or directory: 'archivo_inexistente.txt'".
- Paso 4: La excepción se captura en el except y se guarda en la variable error.
- Paso 5: Se ejecuta print(f"Error:{error}") que muestra el mensaje original del error.
- Paso 6: Se muestra "Creando un archivo nuevo..."
- Paso 7: Se abre el mismo archivo pero ahora en modo escritura ("w"), lo que CREA el archivo si no existe.
- Paso 8: Se escribe "Este es un archivo nuevo" dentro del archivo.
- Paso 9: El programa termina.

Después de ejecutar el programa una vez, el archivo queda creado en la carpeta. Si se ejecuta nuevamente, ya no se generará la excepción porque el archivo existe.

# Ejemplo 4 - Combinando multiples excepciones

```python
try:
    # Intentamos abrir y leer un archivo
    archivo = open("datos.txt", "r")
    valor = int(archivo.readline().strip())
    resultado = 100 / valor
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error:{type(e).__name__}")
    print(f"Descripción:{e}")
```

## Explicación
Este código muestra cómo agrupar varios tipos de excepciones en un SOLO bloque except usando una tupla.

Dentro del bloque try hay tres operaciones que pueden fallar de diferentes maneras.

Primera operación: archivo = open("datos.txt", "r"). Si el archivo "datos.txt" no existe, se genera FileNotFoundError.

Segunda operación: valor = int(archivo.readline().strip()). Si el archivo está vacío o contiene texto que no es un número, se genera ValueError.

Tercera operación: resultado = 100 / valor. Si el valor leído del archivo es 0, se genera ZeroDivisionError.

En lugar de escribir tres bloques except separados (uno para cada error), se agrupan los tres tipos de excepción en una tupla: (FileNotFoundError, ValueError, ZeroDivisionError). Si ocurre CUALQUIERA de estos tres errores, se ejecuta el mismo bloque except.

Dentro del except se usa "as e" para capturar el objeto de la excepción. La función type(e).name devuelve el nombre del tipo de error que ocurrió (por ejemplo "FileNotFoundError", "ValueError" o "ZeroDivisionError"). Esto permite saber exactamente qué error pasó aunque todos se manejen en el mismo lugar.

## Salida 
![Salida ejemplo 4](images/captura4.png)

## ¿Por qué da esa salida?
- Paso 1: try intenta abrir "datos.txt".
- Paso 2: El archivo no existe, Python genera FileNotFoundError.
- Paso 3: Como FileNotFoundError está en la tupla, se ejecuta el except.
- Paso 4: type(e).name devuelve "FileNotFoundError".
Paso 5: e contiene el mensaje original del error.