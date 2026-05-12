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
