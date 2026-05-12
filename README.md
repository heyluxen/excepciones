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

