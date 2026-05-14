try:
    1 / 0  # Genera ZeroDivisionError
except ZeroDivisionError:
    print("Capturada división por cero")
    # La excepción ha sido manejada
finally:
    # Si descomentas la siguiente línea, el ZeroDivisionError original se perderá
    # y será reemplazado por este ValueError
    # int("abc")  # Genera ValueError
    print("Bloque finally ejecutado")