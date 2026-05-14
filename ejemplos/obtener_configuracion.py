def obtener_configuracion(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigurationError(f"Archivo de configuración no encontrado:{archivo}") from e