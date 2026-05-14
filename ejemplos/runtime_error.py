def conectar_a_servidor():
    if not hay_conexion_internet():
        raise RuntimeError("No hay conexión a Internet")
    # Código para conectar al servidor