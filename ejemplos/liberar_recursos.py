conexion = None
try:
    conexion = conectar_a_base_de_datos()
    datos = conexion.ejecutar_consulta("SELECT * FROM usuarios")
    procesar_datos(datos)
except ConexionError:
    print("Error al conectar con la base de datos")
except ConsultaError:
    print("Error al ejecutar la consulta")
finally:
    if conexion:
        conexion.cerrar()  # La conexión se cierra siempre