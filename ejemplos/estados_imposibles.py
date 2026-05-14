def procesar_respuesta(respuesta):
    if respuesta.codigo == 200:
        return respuesta.datos
    elif respuesta.codigo == 404:
        return None
    else:
        raise RuntimeError(f"Código de respuesta no manejado:{respuesta.codigo}")