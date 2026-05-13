try:
    numero = int("abc")  # Intentar convertir una cadena no numérica a entero
except ValueError:
    print("La cadena no representa un número válido")