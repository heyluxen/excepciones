try:
        datos = obtener_datos_de_api()
        validar_formato(datos)
except ConexionError:
    print("No se pudo conectar con el servidor.")
except FormatoInvalidoError:
    print("Los datos recibidos tienen un formato incorrecto.")
else:
    # Solo procesamos si obtuvimos y validamos los datos correctamente
    resultados = procesar_datos(datos)
    guardar_resultados(resultados)