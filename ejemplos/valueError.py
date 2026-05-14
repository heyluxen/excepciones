def establecer_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")
    return edad