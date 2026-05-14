def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
        # x = 1 / 0  # Descomentar para generar una excepción
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")
    
    print("5. Continuando después del bloque try")

demostrar_orden()