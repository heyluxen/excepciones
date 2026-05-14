try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")
    archivo = open("datos.txt", "w")
    archivo.write("Archivo creado automáticamente")
else:
    print(f"Contenido leído:{contenido}")
    # Este código solo se ejecuta si no hubo excepciones
finally:
    print("Operación de archivo completada.")
    archivo.close()  # El archivo se cierra siempre, se haya abierto para leer o escribir