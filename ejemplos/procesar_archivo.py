def procesar_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError as e:
        print(f"Registrando error:{e}")
        raise  # Relanza la última excepción